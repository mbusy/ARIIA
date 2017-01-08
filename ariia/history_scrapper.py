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

		Parameters:
			historicName - The given historic name

		Returns:
			historicResume - The historic resume from wikipedia
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

		return self.historicResume
		# print text.decode('utf-8')
