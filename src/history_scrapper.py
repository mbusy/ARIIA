# -*- coding: utf-8 -*-

import urllib2
import cookielib

from bs4 import BeautifulSoup
import unicodedata2


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
			historicNameURL = historicName.pop()
		else:
			historicNameURL = historicName.pop()

			for element in historicName:
				preHistoricNameURL += element + "_"

			historicNameURL = preHistoricNameURL + historicNameURL

		historicNameURL = urllib2.quote(historicNameURL.encode('utf-8'))
		
		url = "https://fr.wikipedia.org/wiki/" + historicNameURL
		httpRequest     = urllib2.Request(url)
		page            = self.opener.open(httpRequest)
		rawdata         = page.read()
		
		# Treatement on rawdata
		

		soup            = BeautifulSoup(rawdata)

		# kill all script and style elements
		for script in soup(["script", "style"]):
			script.extract()    # rip it out
		
		# get text
		text = soup.get_text()
		
		# break into lines and remove leading and trailing space on each
		lines = (line.strip() for line in text.splitlines())
		# break multi-headlines into a line each
		chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
		# drop blank lines
		text = '\n'.join(chunk for chunk in chunks if chunk)
		
		# text = unicodedata2.normalize('NFKD', text).encode('utf-8','ignore')
		text = text.encode('latin1', 'ignore')
		print text
