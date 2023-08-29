import tkinter as tk
from tkinter import ttk
import threading
import time
import queue

from concurrent.futures import ThreadPoolExecutor

from helpers.definitions import Definitions
from ai.qi import QuestionAnswering
from helpers.converter import Converter

import customtkinter as ctk

# For image processing
from PIL import ImageTk, Image
import requests
from io import BytesIO

import sys

from libraries.index import Dictionaries

class ScrollableFrame(tk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)


        canvas = tk.Canvas(self, bg='grey20', bd=0, highlightthickness=0)  # remove border from canvas
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview, width=5, bg='black')  # customize scrollbar
        self.scrollable_frame = tk.Frame(canvas, bg='grey20')  # and here

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        # Binding mouse wheel scrolling
        canvas.bind_all('<MouseWheel>', lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")



class Window:
    def __init__(self):

        self.Dictionaries = Dictionaries()

        self.text_var = None
        self.current_keyword = None
        self.defintions_text = None
        self.saved_keywords = []
        self.saved_keywords_definition = []
        self.windowRoot = None
        self.definer = Definitions() # dictionary for defining words
        self.converter = Converter()
        self.keywords_frame = None

        self.state = "loading"
        self.source = 'Default'
        self.source_values = self.Dictionaries.available_sources
        
        # controls context actions
        self.context = []
        self.context_file_only = True
        self.context_source_file = None
        self.context_source_directory = None
        self.context_source = None

        self.qa = QuestionAnswering()

        self.executor = ThreadPoolExecutor(max_workers=1)

        self.encountered_words = set()



    # updates the application state
    def change_state(self, newState):
        self.state = newState
        return self.state


    def application_start(self, loaded_aux):
        print('app start')
        loadingWindow = ctk.CTkToplevel(self.windowRoot)
        loadingWindow.title('ANeuralPulser - Loading')
        loadingWindow.configure(bg='grey14')  # Set the window background to grey
        loadingWindow.geometry("400x200")  # Set the window size
        loadingWindow.overrideredirect(True)  # Remove window decorations for a modern look
        loadingWindow.attributes("-topmost", True)  # This line makes the window stay on top

        # Center the window
        window_width = loadingWindow.winfo_reqwidth()
        window_height = loadingWindow.winfo_reqheight()
        position_right = int(loadingWindow.winfo_screenwidth()/2 - window_width/2)
        position_down = int(loadingWindow.winfo_screenheight()/2 - window_height/2)
        loadingWindow.geometry("+{}+{}".format(position_right, position_down))

        # Create a frame to hold all the widgets
        frame = tk.Frame(loadingWindow, bg='grey14')
        frame.place(relx=0.5, rely=0.5, anchor='center')

        # Title
        title = tk.Label(frame, text='NeuralPulser', font=('Helvetica', 24), bg='grey14', fg='white')
        title.pack(padx=20, pady=10)

        # Subtitle
        subtitle = tk.Label(frame, text='© 2023 Daniel Payne', font=('Helvetica', 10), bg='grey14', fg='white')
        subtitle.pack(padx=20, pady=10)

        progress_bar = ctk.CTkProgressBar(frame, width=300)
        progress_bar.pack(padx=20, pady=10)

        # Loading Text
        loading_text = tk.Label(frame, text='Loading...', font=('Roboto', 12), bg='grey14', fg='white')
        loading_text.pack(padx=20, pady=10)

        progress_bar.start()


        def load_data(fn, name, arg=None):
            result = None
            loading_text["text"] = "Loading " + name
            try:
                if arg:
                    if isinstance(arg, dict):
                        result = fn(**arg)
                    elif isinstance(arg, list) and len(arg) > 1:
                        result = fn(*arg)
                    else:
                        result = fn(arg)
                else:
                    result = fn()
                # loadingWindow.destroy()
                return result
            except:
                loading_text["text"] = "Error Loading NeuralPulser\nExiting."
                time.sleep(5)
                loadingWindow.destroy()
                self.windowRoot.quit()
                self.windowRoot.destroy()
                sys.exit()

        loaded_complete = []
        for item in loaded_aux:
            if 'args' in item:
                print(item)
                loaded_complete.append({'name': item['name'], 'result': load_data(item['fn'], item['name'], item['args'])})
            else:
                print(item)
                loaded_complete.append({'name': item['name'], 'result': load_data(item['fn'], item['name'])})
        progress_bar.stop()  # Stop indeterminate mode
        progress_bar.destroy()
        loading_text["text"] = "Loading Complete!"
        
        time.sleep(3)
        loadingWindow.destroy()
        

        
        self.loadingWindowMain = loadingWindow
        self.create_main_window()
        print(loaded_complete)
        return loaded_complete



    def create_main_window(self):
        window = self.windowRoot
        window.title("NeuralPulser")  # Set the title of the window

        # Set window background to black
        window.configure(bg='black')
        window.attributes('-alpha', 1)

        # Set minimum window size
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        window_width = int(screen_width * 1)
        window_height = int(screen_height * 1)
        window.geometry(f"{window_width}x{window_height}+{int((screen_width - window_width) / 2)}+{int((screen_height - window_height) / 2)}")
        window.update_idletasks()  # Update the window to ensure correct values
        icon_image = tk.PhotoImage(file='neuralpulser.gif')
        window.iconphoto(False, icon_image)

        

        # Create sidebar
        sidebar_width = int(window_width * 0.25)
        self.sidebar = tk.Frame(master=window, bg='grey10', width=sidebar_width)
        self.sidebar.pack(side='left', fill='y', expand=False)
        self.sidebar.pack_propagate(0)  # Prevent resizing

        self.logo = tk.PhotoImage(file='neuralpulserLogo.gif')  # Load the logo

        # Create a label with the image, don't forget to keep a reference to the image
        sidebar_logo = tk.Label(master=self.sidebar, image=self.logo, bg='grey10', fg='white')
        sidebar_logo.pack(pady=10) 

        # Create a label for the rest of the title
        # sidebar_title = tk.Label(master=self.sidebar, text='euralPulser', font=('Arial', 24), bg='grey10', fg='white')
        # sidebar_title.pack(pady=10) 

        # Create a title in the sidebar
        # sidebar_title = tk.Label(master=self.sidebar, text='NeuralPulser', font=('Arial', 24), bg='grey10', fg='white')
        # sidebar_title.pack(pady=10)  # Added padding to center vertically

        # under quote
        # sidebar_under_quote = tk.Label(master=self.sidebar, text='“Knowledge is real knowledge only when it is acquired by the efforts of your intellect,\nnot by memory.”',
        #     font=('Roboto', 8), bg='grey10', fg='white')
        sidebar_under_quote = tk.Label(master=self.sidebar, text='“Neural Pulser”',
            font=('Roboto', 8), bg='grey10', fg='white')
        sidebar_under_quote.pack(pady=0)

        # Create Detected Section
        detected_label = tk.Label(master=self.sidebar, text='Detected:', font=('Helvetica', 14), bg='grey10', fg='white')
        detected_label.pack(anchor='nw', padx=5)

        # Create a StringVar object
        self.text_var = tk.StringVar()
        self.text_var.set("Welcome. We are just finishing up a few things before we can begin...")  # Set the initial value
        label = tk.Label(master=self.sidebar, textvariable=self.text_var, font=('Helvetica', 10), bg='grey10', fg='white', wraplength=480)
        label.pack(side='top', anchor='nw', padx=5)  # Add the label to the window

         # 'Source' label
         # gets all available sources and sets it to a tk.BooleanVar()
        # for source in self.Dictionaries.available_sources:
        #     self.source_values[source] = tk.BooleanVar()
        # print(self.source_values)

        # for value, var in self.source_values.items():
        #     checkbox = tk.Checkbutton(master=self.sidebar, text=value, variable=var, onvalue=True, offvalue=False, font=('Roboto', 10), bg='grey10', fg='white', activeforeground='black')
        #     checkbox.pack(anchor='w', padx=10, pady=5)

        source_label = tk.Label(master=self.sidebar, text='Source:', font=('Roboto', 10), bg='grey10', fg='white')
        source_label.pack(pady=10)  # Adjust padding as needed

        # 'Source' combobox
        source_combobox = ctk.CTkComboBox(master=self.sidebar, values=self.source_values,
                                     command=self.combobox_callback, border_width=0, font=('Roboto', 10), dropdown_font=('Roboto', 10))
        source_combobox.pack()

        # add context button 
        context_config_window = self.create_button_basic(master=self.sidebar, 
            context='Add Context', 
            bg='grey20', 
            fg='white', 
            command=self.create_context_config_window)

        # context config window - created above


        # Create the remaining frame to fill the rest of the window
        remaining_frame = tk.Frame(master=window, bg='grey20')
        remaining_frame.pack(side='left', fill='both', expand=True)

        # Definitions
        self.defintions_text = tk.StringVar()
        self.defintions_text.set("")
        
        # Create Scrollable frame
        definitions_frame = ScrollableFrame(remaining_frame, bg='grey20')
        definitions_frame.pack(fill='both', expand=True)

        # Add definitions label to the scrollable frame
        definitions_label = tk.Label(definitions_frame.scrollable_frame, textvariable=self.defintions_text, font=('Helvetica', 12), fg='white', bg='grey20', wraplength=480, anchor='w', justify='left')
        definitions_label.pack(fill='both', expand=True, padx=10)

        # Keyword entries
        self.keyword_entries = tk.StringVar()
        self.keyword_entries.set(self.saved_keywords)
        keyword_entries_label = tk.Label(remaining_frame, textvariable=self.keyword_entries, fg='white', bg='grey10', wraplength=480)
        keyword_entries_label.pack(fill='both', side='bottom', anchor='sw')  # Add the label to the window

        # Create KeyWord Section
        keyword_section_label = tk.Label(remaining_frame, font=('Helvetica', 12), text='Current Subjects:', fg='white', bg='grey10', wraplength=480)    
        keyword_section_label.pack(fill='both')  # Add the label to the window

        self.keywords_frame = tk.Frame(remaining_frame, bg='grey10')
        self.keywords_frame.pack(side='bottom', fill='both')

         # Create a button with an arrow symbol
        self.collapse_button = tk.Button(master=self.sidebar, text='←', command=self.toggle_sidebar, bg='grey10', fg='white', relief='flat', borderwidth=0)
        self.collapse_button.place(relx=1, rely=0.5, anchor='e')

        # Create a transparency button
        self.attributes_button = tk.Button(master=self.sidebar, font=('Arial', 15), text='👁', command=lambda: self.toggle_flow(0.75), bg='grey10', fg='white', relief='flat', borderwidth=0)
        self.attributes_button.place(x=0, y=0)

        window.bind("<Button-2>", self.clear_all)

        window.bind('<Configure>', self.on_resize)
        window.deiconify()


        # Need to fix keywords filling up x axis and not wrapping to the next line. For now user needs to clear
        # keywords when it gets full

    def create_button_basic(self, master, context, bg, fg, command, pady=10):
        button = ctk.CTkButton(master=master, 
                       text=context, 
                       bg_color='grey20', 
                       fg_color=bg, 
                       command=command,
                       corner_radius=15,
                       border_width=0,
                       hover=False,
                       font=('Roboto', 10))

        button.pack(pady=pady)


    def create_window(self):
        # window = tk.Tk()  # Create a new window
        window = ctk.CTk()
        window.withdraw()

        
        
        self.windowRoot = window
        window.mainloop()  # Start the event loop

        
    def toggle_sidebar(self):
        # Get current width
        current_width = self.sidebar.winfo_width()

        # Collapse if width is large
        if current_width > 200:
            new_width = int(self.windowRoot.winfo_screenwidth() * 0.01)
            self.collapse_button.config(text='→')
        else:  # Expand if width is small
            new_width = int(self.windowRoot.winfo_screenwidth() * 0.25)
            self.collapse_button.config(text='←')

        # Change the width
        self.sidebar.configure(width=new_width)
        self.sidebar.update_idletasks()

    def toggle_flow(self, min):
        # Retrieve the current alpha attribute
        current_alpha = self.windowRoot.attributes('-alpha')

        # Change the alpha attribute based on its current value
        if current_alpha == 1.0:
            self.windowRoot.attributes('-alpha', min)
        else:
            self.windowRoot.attributes('-alpha', 1.0)

    def combobox_callback(self, choice):
        self.source = choice
        print(choice)

    def checkWindowSize(self):
        self.windowRoot.update()
        return {
        'width': self.windowRoot.winfo_width(),
        'height': self.windowRoot.winfo_height()
        }


    def on_resize(self, event):
        # print(event)
        # print('window has been resized, new size is:')
        # print(self.checkWindowSize())
        pass
    # Function to change text 
    def change_text_outside(self, new_text):
        if self.text_var is not None:
            self.text_var.set(new_text)

    def change_current_definition(self, new_text, override=False):
        if self.defintions_text is not None:
            # I am doing away with auto changing back and forth
            # once word is active in keyword directory I will no longer be calling it
            # currently_exists = [item for item in self.saved_keywords_definition if 'name' in item]
            # print(currently_exists)
            # if len(currently_exists):
            #     print(new_text + 'currently exists')
            if new_text not in self.encountered_words or override == True:
                word = self.get_definition(new_text)
                self.defintions_text.set(word)
                self.current_keyword = word # change current keyword

    def get_definition(self, word):
        definition = ''
        if self.source == 'Default' or self.source in self.source_values:
            definition = self.definer.define(word, self.source)
        elif self.source == 'Wikipedia':
            definition = self.qa.get_wikipedia_summary(word)
            print('\n\n\n\n\nDEFINTION IS:')
            print(definition)
        if word not in self.saved_keywords:
            self.add_keyword(word)
            self.saved_keywords_definition.append({'name':word, 'define': definition})
        return definition

    def add_keyword(self, keyword):
        if keyword not in self.saved_keywords:
            self.saved_keywords.append(keyword)
            self.encountered_words.add(keyword.lower())
            # Pack each keyword_label into the same keywords_frame
            keyword_label = tk.Label(self.keywords_frame, text=keyword, font=('Helvetica', 12), fg='white', bg='grey10', cursor='hand2')
            keyword_label.bind("<Button-1>", lambda event, keyword=keyword: self.keyword_label_click(event, keyword))
            keyword_label.pack(side='left', padx=5, fill='x')

            # self.create_new_window_with_image(keyword)




    def keyword_label_click(self, event, keyword):
        self.change_current_definition(keyword, True)

    # Run the GUI in a separate thread
    # Make more modular - any info detail extra component use this
    def create_new_window(self, word):
        new_window = tk.Toplevel(self.windowRoot)
        new_window.title(word + ' Image')
        new_label = tk.Label(new_window, text="This will have image")
        new_label.pack()


    def create_new_window_with_image(self, word):
        # Download the image data
        url = "https://upload.wikimedia.org/wikipedia/commons/a/a4/JavaScript_code.png"
        response = requests.get(url)
        image_data = Image.open(BytesIO(response.content))

        # Convert the image data to a format that Tkinter can understand
        tk_image = ImageTk.PhotoImage(image_data)

        # Create a new window
        new_window = tk.Toplevel(self.windowRoot)
        new_window.title(word + ' Example')
        # Position the new window relative to the root window
        new_window.geometry("+%d+%d" % (self.windowRoot.winfo_x() + 550, self.windowRoot.winfo_y() + 50))


        # Create a label in the new window and use it to display the image
        image_label = tk.Label(new_window, image=tk_image)
        image_label.image = tk_image  # Keep a reference to the image object to prevent it from being garbage collected
        image_label.pack()

    def create_context_config_window(self):
        new_window = tk.Toplevel(self.windowRoot)
        new_window.overrideredirect(True)
        new_window.configure(bg='grey10')
        # new_window.geometry("+%d+%d" % (self.windowRoot.winfo_x() + 500, self.windowRoot.winfo_y() + 500))
        new_window.geometry("400x200")
        # new_window.attributes('-topmost', True)

        # Get screen width and height
        screen_width = new_window.winfo_screenwidth()
        screen_height = new_window.winfo_screenheight()

        # Calculate position
        window_width, window_height = 700, 500
        pos_top = (screen_height // 2) - (window_height // 2)
        pos_left = (screen_width // 2) - (window_width // 2)

        new_window.geometry(f"{window_width}x{window_height}+{pos_left}+{pos_top}")

        # close this window
        def close_window():
            new_window.destroy()

        close_label = tk.Label(new_window, text="X", font=('Roboto', 12), cursor='hand2', fg='white', bg='grey10')
        close_label.bind("<Button-1>", lambda event: close_window())
        close_label.pack(anchor='ne', padx=3, pady=3)

        # Context Config Section
        title = tk.Label(new_window, text='Context Configuration', font=('Helvetica', 24), bg='grey10', fg='white')
        title.pack(padx=20, pady=10)

        # Context Config Section - info
        subtitle = tk.Label(new_window, text='help info on context config', font=('Helvetica', 10), bg='grey10', fg='white')
        subtitle.pack(pady=10)

        # context source FILE
        self.file_directory_frame = tk.Frame(new_window, bg='grey10')  # Create a new frame as a container
        self.file_directory_frame.pack(pady=10)
        file_context_title = ctk.CTkLabel(master=self.file_directory_frame, 
                     text="Context File", 
                     bg_color="grey10", 
                     )
        if self.context_source_file is None:
            self.context_source_file = tk.StringVar()
            self.context_source_file.set('None Selected')
        entry_file = ctk.CTkEntry(master=self.file_directory_frame, 
                     fg_color="grey20", 
                     text_color="white",
                     textvariable=self.context_source_file,
                     width=500)

        file_context_title.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        entry_file.grid(row=0, column=1, padx=10, pady=10)

        entry_file.bind("<Button-1>", lambda event: self.select_context_dialog_file())

        # context source DIRECTORY
        directory_context_title = ctk.CTkLabel(master=self.file_directory_frame, 
                     text="Context Directory", 
                     bg_color="grey10")
        if self.context_source_directory is None:
            self.context_source_directory = tk.StringVar()
            self.context_source_directory.set('None Selected')
        entry_directory = ctk.CTkEntry(master=self.file_directory_frame, 
                     fg_color="grey20", 
                     text_color="white",
                     textvariable=self.context_source_directory,
                     width=500)
        directory_context_title.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        entry_directory.grid(row=2, column=1, padx=10, pady=10)

        entry_directory.bind("<Button-1>", lambda event: self.select_context_dialog_directory())

        

        return new_window

    def select_context_dialog_file(self):
        file_path = tk.filedialog.askopenfilename()
        print(file_path)
        if len(file_path):
            self.context_file_only = True
            self.context_source_directory.set('None Selected')
            self.context_source_file.set(file_path)
            self.context_source = file_path
            self.context = []
            # get the data using threading. Will need to create similar for directories.
            future = self.executor.submit(self.converter.file_to_text, file_path)
            self.file_directory_frame.after(100, lambda: self.check_future(future, self.file_directory_frame, lambda result: (self.context.append({
                'name': file_path,
                'content': result
            }), print(self.context), self.qa.get_context_data(self.context[0]['content']))))



    def check_future(self, future, windowObject, followup_task=None, interval=100):
        if future.done():
            result = future.result()  # get the result of the task

            if followup_task is not None:
                # If a follow-up task is provided, we call it with the result.
                followup_task(result)
            else:
                print(result)  # If there is no follow-up task, we just print the result (or do whatever you want with it).
                return result
        else:
            # The task is not yet complete, so we schedule this function to run again in 'interval' ms.
            print('task still running')
            windowObject.after(interval, lambda: self.check_future(future, windowObject, followup_task, interval))



    # def check_future(self, future, file_path):
    #     if future.done():
    #         result = future.result()  # get the result of the task
    #         self.context.append({'name':file_path, 'content': result})
    #         print(self.context[0]['content'])
            
    #         future_qa = self.executor.submit(self.qa.get_context_data, self.context[0]['content'])
    #         self.file_directory_frame.after(100, self.check_future_qa, future_qa)
    #     else:
    #         # The task is not yet complete, so we schedule this function to run again in 100 ms.
    #         print('task still running')
    #         self.file_directory_frame.after(100, self.check_future, future, file_path)

    # def check_future_qa(self, future):
    #     if future.done():
    #         answer = future.result()  # get the result of the task
    #         print(answer)
    #         # Here you can do whatever you want with the answer.
    #         # For example, you could show it in the GUI.
    #     else:
    #         # The task is not yet complete, so we schedule this function to run again in 100 ms.
    #         # print('QA task still running')
    #         self.file_directory_frame.after(100, self.check_future_qa, future)


    def select_context_dialog_directory(self):
        directory_path = tk.filedialog.askdirectory() 
        if len(directory_path):
            print("Directory path:", directory_path)
            self.context_file_only = False
            self.context_source_directory.set(directory_path)
            self.context_source_file.set('None Selected')
            self.context_source = directory_path


    # create a different method to clear keywords already found. but remeber to sort out
    # how they can be re-added because of 'encountered_words inside speech.py'
    def clear_all(self, event):
        print('should clear all')
        self.saved_keywords 
        self.defintions_text.set("")
        self.encountered_words = set()
        
        for widget in self.keywords_frame.winfo_children():
            widget.destroy()