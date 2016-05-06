# -*- coding: utf-8 -*-

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
		self.temperature = 0.0

		self.cookieJar   = cookielib.CookieJar()
		self.opener      = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookieJar))

	def getMeteo(self, city):
		"""
		Get the different meteo parameters for the given city

		Parameters :
			city - The city targeted
		"""

		for letter in city:
			if letter.lower().encode("utf-8") == u"é".encode("utf-8"):
				self.cityUrl += "%C3%89"
			else:
				self.cityUrl += letter


		url             = "http://www.yr.no/place/France/%C3%8Ele-de-France/" + self.cityUrl + "/"
		httpRequest     = urllib2.Request(url)
		page            = self.opener.open(httpRequest)
		rawdata         = page.read()
		lines_of_data   = rawdata.split('\n')
		special_lines   = [line for line in lines_of_data if line.find('og:description')>-1]
		info            = special_lines[0].replace('"','').split('content=')[1]
		sections        = info.split(':')
		sectionsRefined = sections[3].split(',')
                
		for temperatureData in sectionsRefined[1].split(" "):
			pass

		self.temperature = temperatureData
