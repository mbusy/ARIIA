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
		self.historicResume = ""

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
		rawHistoricResume  = ""

		if len(self.historicName) == 1:															# Historic name treatement
			historicNameURL = historicName.pop()
		
		else:
			historicNameURL = historicName.pop()

			for element in historicName:
				preHistoricNameURL += element + "_"

			historicNameURL = preHistoricNameURL + historicNameURL

		historicNameURL = urllib2.quote(historicNameURL.encode('utf-8'))
		
		
		url             = "https://fr.wikipedia.org/wiki/" + historicNameURL
		httpRequest     = urllib2.Request(url)
		page            = self.opener.open(httpRequest)
		rawdata         = page.read()
		
		lines_of_data   = rawdata.split('\n')													# Treatement on rawdata
		
		special_lines = list()																	# Keep the resume
		startIntro    = False
		endIntro      = False

		for line in lines_of_data:
			if line.find('<p><b>') > -1:
				startIntro = True

			if startIntro:
				special_lines.append(line)
				if line.find('</p>'):
					endIntro = True

			if endIntro:
				startIntro = False
				endIntro   = False
				break

		
		for line in special_lines:																# Get the resume
			rawHistoricResume += line

		soup = BeautifulSoup(rawHistoricResume)

		for script in soup(["script", "style"]):												# kill all script and style elements
			script.extract()    																# rip it out
		
		text                = soup.get_text()													# get text
		lines               = (line.strip() for line in text.splitlines())						# break into lines and remove leading and trailing space on each
		chunks              = (phrase.strip() for line in lines for phrase in line.split("  "))	# break multi-headlines into a line each
		text                = '\n'.join(chunk for chunk in chunks if chunk) 					# drop blank lines
		text                = text.encode('utf-8', 'ignore')		
		self.historicResume = text.decode('utf-8')
		# print text.decode('utf-8')


