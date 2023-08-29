from libraries.dictionary_custom_javascript import dictionary
from libraries.dictionary_custom_react import dictionary as dictionary_react

class Dictionaries():
	def __init__(self):
		self.available_sources = [
		'javascript', 'react'
		]

		self.sources = {
		'javascript': dictionary,
		'react': dictionary_react,
		}

		self.javascript = dictionary
		self.react = dictionary_react

