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

import unittest
import logging

import meteo_scrapper_test
import data_container_test
import history_scrapper_test


if __name__ == "__main__":

	logging.basicConfig(filename='unittests/logs/unittests.log',
		level=logging.DEBUG,
		format='%(levelname)s %(relativeCreated)6d %(threadName)s %(message)s (%(module)s.%(lineno)d)',
		filemode='w')

	testClasses = [meteo_scrapper_test.MeteoScrapperTest,
		data_container_test.DataContainerTest,
		history_scrapper_test.HistoryScrapperTest]

	testsList  = list()
	loader 	   = unittest.TestLoader()

	for testClass in testClasses:
		testsList.append(loader.loadTestsFromTestCase(testClass))

	finalTestList = unittest.TestSuite(testsList)
	testRunner 	  = unittest.TextTestRunner()
	results 	  = testRunner.run(finalTestList)
