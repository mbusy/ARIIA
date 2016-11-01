# -*- coding: utf-8 -*-

from ariia import ariia
from ariia import audio_device_manager
from ariia import history_scrapper
from ariia import meteo_scrapper
from ariia import shopping_list_manager

def main():

	history = history_scrapper.HistoryScrapper()
	print "Creation of the history scrapper successful"

	meteo = meteo_scrapper.MeteoScrapper()
	print "Creation of the meteo scrapper successful"

	shopping = shopping_list_manager.ShoppingListManager(audioDevice)
	print "Creation of the shopping list manager successful"

if __name__ == "__main__":
	main()
