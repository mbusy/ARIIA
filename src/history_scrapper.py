# -*- coding: utf-8 -*-

import urllib2
import cookielib

class HistoryScrapper:
	"""
	Class to retreive the historic data from the internet
	"""

	def __init__(self):
		"""
		Constructor
		"""

		self.historicName = ""

		self.cookieJar   = cookielib.CookieJar()
		self.opener      = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookieJar))


	def getHistoricDescription(self, historicName):
		"""
		Get the historic description for the given historic name

		Parameters :
			historicName - The given historic name
		""" 

		self.historicName  = historicName
		historicNameURL    = ""
		preHistoricNameURL = ""

		# Historic name treatement
		if len(self.historicName) == 1:
			historicNameURL = str(historicName.pop())
		else:
			historicNameURL = historicName.pop()

			for element in historicName:
				preHistoricNameURL += element + "_"

			historicNameURL = preHistoricNameURL + historicNameURL

		print historicNameURL