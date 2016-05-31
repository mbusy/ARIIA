# -*- coding: utf-8 -*-

from chatterbot import ChatBot
from chatterbot.training.trainers import ListTrainer

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

		self.ariiaTalker.set_trainer(ListTrainer)

		self.ariiaTalker.train([
			"comment vas-tu",
			"ça va bien merci, et toi ?",
			"très bien !",
			"moi ça va.",
			"je suis en pleine forme !",
		])

		self.ariiaTalker.train([
			"comment tu t'appelles",
			"Ariia",
		])

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