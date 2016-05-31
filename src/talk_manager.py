# -*- coding: utf-8 -*-

from chatterbot import ChatBot
from chatterbot.training.trainers import ChatterBotCorpusTrainer

class TalkManager:
	"""
	Class Managing the discussions held by Ariia
	and her training.
	"""

	def __init__(self):
		"""
		Constructor
		"""

		self.ariiaTalker = ChatBot("Ariia")
		self.talk        = None



	def getTalk(self, dialog):
		"""
		Specify the speech answering the user's dialog
		
		Parameters :
			dialog - The dialog held by the user
		"""

		self.talk = unicode(self.ariiaTalker.get_response(dialog))
		self.talk = self.talk.encode('utf-8')
		print type(self.talk)
		return self.talk