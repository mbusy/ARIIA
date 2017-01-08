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

class MeteoScrapper:
	"""
	Class used to retreive meteo data from the internet
	"""

	def __init__(self):
		"""
		Init the meteo scrapper
		"""

		self.city    	 = ""
		self.cityUrl 	 = ""
		self.sky         = ""
		self.temperature = ""
		self.wind        = ""

		self.skyData         = list()
		self.temperatureData = list()
		self.windData        = list()

		self.cookieJar   = cookielib.CookieJar()
		self.opener      = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookieJar))


	def meteoTranslate(self):
		"""
		Method used to translate the meteo data retreived from the website
		"""

		self.sky         = ""
		self.temperature = ""
		self.wind        = ""

		# Sky translation
		if 'Clear' in self.skyData and 'sky' in self.skyData:
			self.sky = u"dégagé".encode('utf-8')

		elif 'Fair' in self.skyData:
			self.sky = u"relativement dégagé".encode('utf-8')

		elif 'Cloudy' in self.skyData:
			self.sky = "nuageux"

		elif 'Partly' in self.skyData and 'cloudy' in self.skyData:
			self.sky = "partiellement nuageux"

		elif 'Rain' in self.skyData and 'showers' in self.skyData:
			self.sky = u"extrêmement pluvieux".encode('utf-8')

		elif 'Rain' in self.skyData:
			self.sky = "pluvieux"

		elif 'Heavy' in self.skyData and 'rain' in self.skyData:
			self.sky = u"très pluvieux".encode('utf-8')


		# Temperature translation
		self.temperature = self.temperatureData.pop()

		# Wind translation
		if 'Light' in self.windData and 'air' in self.windData:
			self.wind = u"un temps léger".encode('utf-8')

		elif 'Gentle' in self.windData and 'breeze' in self.windData:
			self.wind = "une douce brise"

		elif 'Light' in self.windData and 'breeze' in self.windData:
			self.wind = u"une légère brise".encode('utf-8')

		elif 'Moderate' in self.windData and 'breeze' in self.windData:
			self.wind = u"une moyenne brise".encode('utf-8')


	def getMeteo(self, city):
		"""
		Get the different meteo parameters for the given city

		Parameters :
			city - The targeted city

		Returns:
			sky - Data about the state of the sky
			temperature - Data about the temperature
			wind - Data about the wind
		"""

		self.city = city
		self.cityUrl = urllib2.quote(self.city.encode('utf-8'))

		url             = "http://www.yr.no/place/France/%C3%8Ele-de-France/" + self.cityUrl + "/"
		httpRequest     = urllib2.Request(url)
		page            = self.opener.open(httpRequest)
		rawdata         = page.read()
		lines_of_data   = rawdata.split('\n')
		special_lines   = [line for line in lines_of_data if line.find('og:description')>-1]
		info            = special_lines[0].replace('"','').split('content=')[1]
		sections        = info.split(':')
		sectionsRefined = sections[3].split(',')

		self.skyData         = sectionsRefined[0].split(" ")
		self.temperatureData = sectionsRefined[1].split(" ")
		self.windData        = sectionsRefined[3].split(" ")

		self.meteoTranslate()

		return self.sky, self.temperature, self.wind
		# For the debug
		# print '-----METEO-DEBUG------'
		# print self.skyData
		# print self.windData
		# print '----------------------'
