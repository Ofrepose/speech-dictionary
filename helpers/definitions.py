from PyDictionary import PyDictionary

# all dictionaries
from libraries.index import Dictionaries


class Definitions:
	def __init__(self):
		self.dictionary = PyDictionary()
		self.Dictionaries = Dictionaries()
		self.allDictionaries = {}
		for source in self.Dictionaries.available_sources:
			self.allDictionaries[source] = self.Dictionaries.sources[source]
			self.allDictionaries[source]['allTerms'] = [word['name'].lower() for word in self.Dictionaries.sources[source]['terms']]


	def define(self, word, source):
		if source in self.Dictionaries.available_sources:
			if word in self.allDictionaries[source]['allTerms']:
				definition = [term for term in self.allDictionaries[source]['terms'] if word.lower() == term['name'].lower()]
				return word+':\n' + definition[0]['define'] + '\n\nExample:\n'+ definition[0]['example']
		else:
			return self.dictionary.meaning(word)