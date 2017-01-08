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

from ariia import shopping_list_manager


class ShoppingListManagerTest(unittest.TestCase):
	"""
	Unitests for the shopping list manager
	"""


	def setUp(self):
		"""
		Setup for the test
		"""

        logging.basicConfig(filename='unittests/logs/shopping_list_manager_test.log',
			level=logging.DEBUG,
			format='%(levelname)s %(relativeCreated)6d %(threadName)s %(message)s (%(module)s.%(lineno)d)',
			filemode='w')


	def test_constructor(self):
		"""
		Test the creation of the object
		"""

		# TODO : better handling of the audio signals, thanks to pydispatcher.
		# No audio should be directly handled from the shopping list manager.
		pass
