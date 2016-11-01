# -*- coding: utf-8 -*-

from ariia import history_scrapper
from ariia import meteo_scrapper
from ariia import shopping_list_manager

def main():

	history = history_scrapper.HistoryScrapper()
	print "Creation of the history scrapper successful"

	meteo = meteo_scrapper.MeteoScrapper()
	print "Creation of the meteo scrapper successful"

if __name__ == "__main__":
	main()
