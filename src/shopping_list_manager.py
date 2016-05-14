# -*- coding: utf-8 -*-

import dill


class ShoppingListManager:
	"""
	Manage the user shopping list
	"""

	def __init__(self):
		"""
		Constructor
		"""

		self.shoppingLists = dict()
		self.loopFlag      = True
		self.answer        = ""
		self.speech        = ""
		self.request       = list()

		self.loadShoppingLists()



	def loadShoppingLists(self, file="../ressources/shopping_lists"):
		"""
		Load the shopping lists from a ressource file.

		Parameters :
			file - The file where the data is storred,
				   shopping_list is the default value.
		"""

		try:
			self.shoppingLists = dill.load(open(file))
			self.answer        = u"Je détecte ".encode('utf-8')
			self.answer		  += len(self.shoppingLists)
			self.answer       += " listes de courses."

		except Exception:
			self.answer = "Il n'y a pas de listes de courses pour le moment"
	


	def saveShoppingLists(self, file="../ressources/shopping_lists"):
		"""
		Save the shopping lists in a file.

		Parameters :
			file - The file where the data is saved,
				   shopping_lists is the default value.
		"""

		try:
			dill.dump(self.shoppingLists, open(file, "w"))
			self.answer = u"Votre liste a été correctement enregistrée.".encode('utf-8')

		except Exception:
			self.answer = "Il y a une erreur dans la sauvegarde."



	def manageShoppingLists(self, speech):
		"""
		Manage the user's speech and the shopping lists.

		Parameters :
			speech - The speech of the user.
		"""

		del self.request[:]
		self.speech = speech

		for word in self.speech.split(" "):
			self.request.append(word)

		if unicode("Créer", 'utf-8') in self.request and "nouvelle" in self.request and "liste" in self.request:
			self.createNewShoppingList() 

		elif "Quitter" in self.request and "l'application" in self.request:
			self.loopFlag = False
			
			if len(self.shoppingLists) is not 0:
				self.saveShoppingLists()


	def createNewShoppingList(self):
		"""
		Creates a new shopping list
		"""
