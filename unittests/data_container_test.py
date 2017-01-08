# -*- coding: utf-8 -*-
# !/usr/bin/env python

# MIT License
#
# Copyright (c) 2017 Maxime Busy
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import logging
import unittest

from ariia import data_container

class DataContainerTest(unittest.TestCase):
	"""
	Unittests for the data container
	"""


	def setUp(self):
		"""
		Setup for the test
		"""

        pass


	def test_loadingDataContainer(self):
		"""
		Test the loading of the components of data container
		"""
		hour 	 	 = None
		date 	 	 = None
		meteo    	 = None
		history  	 = None
		shopping     = None
		triggerDict  = None
		keywordsDict = None

		logging.info("Try to load the data container components")
		try:
			hour 		 = data_container.HOUR
			date 		 = data_container.DATE
			meteo 		 = data_container.METEO
			history 	 = data_container.HISTORY
			shopping     = data_container.SHOPPING
			triggerDict  = data_container.TRIGGER_DICT
			keywordsDict = data_container.KEYWORDS_DICT

		except NameError:
			logging.info("Loading of at least one component failed")
			pass

		self.assertIsNotNone(hour)
		self.assertIsNotNone(date)
		self.assertIsNotNone(meteo)
		self.assertIsNotNone(history)
		self.assertIsNotNone(shopping)
		self.assertIsNotNone(triggerDict)
		self.assertIsNotNone(keywordsDict)
		logging.info("Successfully loaded all the components")



	def test_Keys(self):
		"""
		Test the keys of the data container (such as HOUR, DATE, etc...)
		"""

		logging.info("Test the type of data container's keys")
		self.assertIsInstance(data_container.HOUR, str)
		self.assertIsInstance(data_container.DATE, str)
		self.assertIsInstance(data_container.METEO, str)
		self.assertIsInstance(data_container.HISTORY, str)
		self.assertIsInstance(data_container.SHOPPING, str)
		logging.info("The types are correct")



	def test_triggerDict(self):
		"""
		Test the trigger dictionnary from the data container
		"""

		triggerDict = data_container.TRIGGER_DICT

		logging.info("Test the type of the trigger dict")
		self.assertIsInstance(triggerDict, dict)
		logging.info("trigger dict is a dictionnary")

		logging.info("Test each key and each linked value in the dictionnary")
		for key, value in triggerDict.items():
			self.assertIsInstance(key, str)
			self.assertIsInstance(value, list)

			for wordList in value:
				self.assertIsInstance(wordList, list)

				for word in wordList:
					self.assertIsInstance(word, str)
		logging.info("All the components of the trigger dict has been tested")



	def test_keywordDict(self):
		"""
		Test the keywords dictionnary
		"""

		keywordsDict = data_container.KEYWORDS_DICT

		logging.info("Test the type of the keywords dict")
		self.assertIsInstance(keywordsDict, dict)
		logging.info("The keywords dict is a dictionnary")

		logging.info("Test each key and linked value of the dictionnary")
		for key, value in keywordsDict.items():
			self.assertIsInstance(key, str)
			self.assertFalse(value)
		logging.info("All the components of the keywords dict has been tested")



	def test_keyInclusion(self):
		"""
		Test if the keys of the data container are in the keys of the trigger
		dict
		"""

		triggerDict = data_container.TRIGGER_DICT

		logging.info("Assert the presence of data_container's keys in the keys\
			of the trigger dictionnary")
		self.assertIn(data_container.HOUR, triggerDict)
		self.assertIn(data_container.DATE, triggerDict)
		self.assertIn(data_container.METEO, triggerDict)
		self.assertIn(data_container.HISTORY, triggerDict)
		self.assertIn(data_container.SHOPPING, triggerDict)
		logging.info("All the keys are included in the trigger dictionnary")



	def test_keywordsInclusion(self):
		"""
		Test if all the words in the trigger dictionnary's lists are mentionned in
		the keywords dictionnary
		"""

		triggerDict     = data_container.TRIGGER_DICT
		keywordsDict    = data_container.KEYWORDS_DICT
		wordsInTriggers = list()

		logging.info("Assert the presence of the trigger dict's keywords in the\
			keys of the keywords dictionnary")
		for value in triggerDict.values():
			for wordList in value:
				for word in wordList:
					if not word in wordsInTriggers:
						wordsInTriggers.append(word)

		for word in wordsInTriggers:
			self.assertIn(word, keywordsDict.keys())
		logging.info("All the trigger keywords are included in the keywords\
			dictionnary")


if __name__ == "__main__":
	logging.basicConfig(filename='unittests/logs/data_container_test.log',
		level=logging.DEBUG,
		format='%(levelname)s %(relativeCreated)6d %(threadName)s %(message)s (%(module)s.%(lineno)d)',
		filemode='w')
		
	unittest.main()
