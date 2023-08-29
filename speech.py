from helpers.definitions import Definitions
from helpers.window import Window
from libraries.common_tech import common_technologies
from libraries.blacklist import unwanted_words
from libraries.dictionary_custom_javascript import dictionary
from libraries.dictionary_custom_react import dictionary as dictionary_react

from libraries.index import Dictionaries

from ai.qi import QuestionAnswering

import vosk
import sys
import os
import traceback
import pyaudio
import json

import threading

import itertools

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
nltk.download('stopwords')


stop_words = set(stopwords.words('english'))


debug = False




# helpers
definer = Definitions() # dictionary for defining words
window = Window() # GUI for analyzer
qa = QuestionAnswering() # ai question query

Dictionaries = Dictionaries()

# start an threaded instance of window
threading.Thread(target=window.create_window).start()

stream = None


try:
    # Get the directory of the executed script
    print('Get the directory of the executed script')
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the Vosk model file
    print('Construct the path to the Vosk model file')
    if debug:
        model_path = os.path.join(script_dir, 'vosk-model-en-us-1/')
    else:
        model_path = os.path.join(script_dir, 'vosk-model-gigaspeech')
    if not os.path.exists(model_path):
        print("Please download a Vosk model for your language from https://alphacephei.com/vosk/models and place it in the script directory.")
        sys.exit(1)

    print('----- Loading Models -----')
    loaded_aux = [
        {
        'name': 'Models',
        'fn': vosk.Model,
        'args': model_path
        },
        {
        'name': 'Audio',
        'fn': pyaudio.PyAudio
        },
    ]

    # Get all loaded results
    loaded_complete = window.application_start(loaded_aux)

    # bind results where needed
    model = loaded_complete[0]['result']

    # Done Main Load

    audio_format = pyaudio.paInt16
    audio_channels = 1
    audio_rate = 16000
    audio_chunk = 8000

    p = loaded_complete[1]['result']

    # when I set up the input being output this will come in handy to set what we listen to. for now, ignore.
    # for i in range(p.get_device_count()):
    #     device_info = p.get_device_info_by_index(i)
    #     print(f"Device {i}: {device_info['name']}")

    stream = p.open(format=audio_format,
                   channels=audio_channels,
                   rate=audio_rate,
                   input=True,
                   frames_per_buffer=audio_chunk)
    print('----- setting up recognizer ----- ')
    recognizer = vosk.KaldiRecognizer(model, audio_rate)

    print("Listening...")
    encountered_words = set()

    # react
    dictWordsReact = [word['name'].lower() for word in Dictionaries.react['terms']]
    dictWordPairsReact = [{'trigger':word['trigger'], 'name':word['name']} for word in Dictionaries.sources['react']['terms'] if word.get('trigger') is not None]

    # js
    dictWords = [word['name'].lower() for word in Dictionaries.javascript['terms']]
    dictWordPairs = [{'trigger':word['trigger'], 'name':word['name']} for word in Dictionaries.sources['javascript']['terms'] if word.get('trigger') is not None]
    print(dictWords)

    # merge all arrays
    dictWordsAll = dictWords + dictWordsReact
    dictWordPairsAll = dictWordPairs + dictWordPairsReact

    # print(dictWordPairsAll)
    # print(dictWordsAll)



    # print([word for word in dictWords])
    while True:

        data = stream.read(audio_chunk, exception_on_overflow=False)
        
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
        else:
            result = recognizer.PartialResult()
            data = json.loads(result)
            # words = data["partial"].split()
            words = word_tokenize(data["partial"])
            # removing stop words for now (its filtering out words we have in dictionary ie: 'for'each)
            # filtered_words = [word for word in words if not word.lower() in stop_words]
            filtered_words = words
            bigrams = list(itertools.pairwise(filtered_words))
            if len(bigrams) > 1:
                for bigram in bigrams:
                    bigram_str = ' '.join(bigram)
                    for word in dictWordPairsAll:                    
                        if bigram_str.lower() == word['trigger'].lower():
                            window.change_current_definition(word['name'].lower())
                            pass;
                        elif bigram_str.split(' ')[0] in dictWordsAll:
                            window.change_current_definition(bigram_str.split(' ')[0])
                            pass;
                        elif bigram_str.split(' ')[1] in dictWordsAll:
                            window.change_current_definition(bigram_str.split(' ')[1])
                            pass;
            elif len(filtered_words) == 1 and filtered_words[0].lower() in dictWordsAll:
                window.change_current_definition(filtered_words[0])    

            # filtered_words = [word for word in words if word.lower() not in unwanted_words]
            # for filtered_word in filtered_words:
            #     # Only if the word is in common_technologies and it has not been encountered before
            #     if filtered_word.lower() in dictWords:
            #         # Add it to the encountered words
            #         # encountered_words.add(filtered_word.lower())
            #         
            #         # Process word pairs (bigrams)
            

            filtered_string = ' '.join(filtered_words)
            window.change_text_outside(filtered_string)

except Exception as e:
    if stream is not None and 'p' in locals() and p is not None:
        stream.stop_stream()
        stream.close()
        p.terminate()
    traceback_info = traceback.format_exc()
    print('traceback: ',traceback_info)
    print('major error ', e)
    os._exit(1)
    # pass