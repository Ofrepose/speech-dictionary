from docx import Document
import pandas as pd
import xmltodict
from pdfminer.high_level import extract_text
import re

class Converter:
	def __init__(self):
		pass

	def docx_to_text(self, filename):
	    doc = Document(filename)
	    return ' '.join(paragraph.text for paragraph in doc.paragraphs)

	def csv_to_text(self, filename, delimiter=','):
	    df = pd.read_csv(filename, delimiter=delimiter)
	    return df.to_string()

	def csv_to_narrative_text(self, filename):
	    # Read the CSV file
	    df = pd.read_csv(filename)

	    # Convert the dataframe to a dictionary
	    data_dict = df.to_dict('records')

	    # Initialize an empty string to hold the narrative text
	    narrative_text = ''

	    # Iterate over each record in the data dictionary
	    for record in data_dict:
	        # For each record, generate a sentence where the column name is used as a descriptor for the corresponding value
	        narrative_text += 'The '
	        narrative_text += ' '.join([f"{key} is {value}." for key, value in record.items()]) + ' '
	        narrative_text += '\n'

	    # Remove extra white spaces
	    narrative_text = re.sub(' +', ' ', narrative_text)

	    return narrative_text

	def xml_to_text(self, filename):
	    with open(filename) as file:
	        doc = xmltodict.parse(file.read())
	    return str(doc)

	def pdf_to_text(self, filename):
		return extract_text(filename)

	def file_to_text(self, filename):
	    if filename.endswith('.docx'):
	        return self.docx_to_text(filename)
	    elif filename.endswith('.csv'):
	        return self.csv_to_narrative_text(filename)
	    elif filename.endswith('.xml'):
	        return self.xml_to_text(filename)
	    elif filename.endswith('.pdf'):
	        return self.pdf_to_text(filename)
	    else:
	        raise ValueError(f'Unsupported file type: {filename}')