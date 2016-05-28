# -*- coding: utf-8 -*-

import dill


class ShoppingListManager:
	"""
	Manage the user shopping list
	"""

	def __init__(self, audioDeviceManager):
		"""
		Constructor.

		Parameters :
			audioDeviceManager - The audio device manager used by the motherclass
		"""

		self.shoppingLists      = dict()
		self.currentDict        = None
		self.loopFlag           = True
		self.answer             = ""
		self.speech             = ""
		self.request            = list()
		self.audioDeviceManager = audioDeviceManager

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
			self.answer		  += str(len(self.shoppingLists))
			self.answer       += " nom de listes de courses."

		except Exception, e:
			self.answer = "Il n'y a pas de listes de courses pour le moment"


		finally:
			self.audioDeviceManager.speakAnswer(self.answer)
	


	def saveShoppingLists(self, file="../ressources/shopping_lists"):
		"""
		Save the shopping lists in a file.

		Parameters :
			file - The file where the data is saved,
				   shopping_lists is the default value.
		"""

		if len(self.shoppingLists) is not 0:
			try:
				dill.dump(self.shoppingLists, open(file, "w"))
				self.answer = u"Votre liste a été correctement enregistrée.".encode('utf-8')

			except Exception:
				self.answer = "Il y a une erreur dans la sauvegarde."

		else:
			self.answer = u"Je n'ai pas de listes à enregistrer.".encode('utf-8')

		self.audioDeviceManager.speakAnswer(self.answer)



	def manageShoppingLists(self):
		"""
		Manage the user's speech and the shopping lists.
		"""

		# self.audioDeviceManager.speakAnswer(u"Pour quitter l'application, dites j'ai fini.".encode('utf-8'))
		# self.audioDeviceManager.speakAnswer(u"Vous pouvez ajouter une liste de courses en disant ajouter liste de courses. Vous pouvez en supprimer une en disant supprimer une liste de courses. Vous pouvez changer de liste en disant changer de liste. Vous pouvez également ajouter ou retirer un élément d'une liste de courses".encode('utf-8'))

		while self.loopFlag:

			print self.shoppingLists

			del self.request[:]
			self.speech = self.audioDeviceManager.listenAndCreateSpeech()


			try:
				assert self.speech is not None

			except AssertionError:
				self.speech = "ndSpeechText"


			for word in self.speech.split(" "):
				self.request.append(word.lower())

			if "ajouter" in self.request and "liste" in self.request or unicode("créer", 'utf-8') in self.request and "liste" in self.request or "nouvelle" in self.request and "liste" in self.request:
				self.createNewShoppingList()

			elif unicode("éditer", 'utf-8') in self.request and "liste" in self.request or "modifier" in self.request and "liste" in self.request:
				self.editShoppingList()

			elif unicode("supprimer", 'utf-8') and "liste" in self.request:
				self.deleteShoppingList()

			elif "j'ai" in self.request and "fini" in self.request:
				self.loopFlag = False
				self.saveShoppingLists()



	def createNewShoppingList(self):
		"""
		Creates a new shopping list
		"""

		self.audioDeviceManager.speakAnswer("Donnez moi le nom de votre nouvelle liste : ")
		newListName = self.audioDeviceManager.listenAndCreateSpeech().lower()

		self.shoppingLists[newListName] = list()



	def deleteShoppingList(self):
		"""
		Deletes an existing shopping list
		"""

		self.audioDeviceManager.speakAnswer(u"Donnez moi le nom de la liste à supprimer : ".encode('utf-8'))
		deleteListName = self.audioDeviceManager.listenAndCreateSpeech().lower()

		if deleteListName in self.shoppingLists.keys():
			del self.shoppingLists[deleteListName.encode('utf-8')]
			self.answer = u"La liste ".encode('utf-8') + deleteListName.encode('utf-8') + u" a été suprimée.".encode('utf-8')

		else:
			self.answer = u"La liste ".encode('utf-8') + deleteListName.encode('utf-8') + u" n'existe pas.".encode('utf-8')

		self.audioDeviceManager.speakAnswer(self.answer)
	


	def editShoppingList(self):
		"""
		Allows the user to edit an active shopping list
		"""

		bKeepEditingList = True
		speechEdit       = ""
		requestEdit      = list()

		self.audioDeviceManager.speakAnswer(u"Quelle liste voulez vous éditer ?".encode('utf-8'))
		activeListName = self.audioDeviceManager.listenAndCreateSpeech().lower()

		if activeListName not in self.shoppingLists.keys():
			self.audioDeviceManager.speakAnswer(u"Cette liste n'existe pas.".encode('utf-8'))
			return

		self.audioDeviceManager.speakAnswer(u"OK, on modifie la liste ".encode('utf-8') + activeListName)

		while bKeepEditingList:
			speechEdit = self.audioDeviceManager.listenAndCreateSpeech()

			for word in speechEdit.split(" "):
				requestEdit.append(word.lower())

			if "c'est" in requestEdit and "bon" in requestEdit or "j'ai" in requestEdit and "fini" in requestEdit:
				self.audioDeviceManager.speakAnswer(u"Très bien.".encode('utf-8'))
				return

			elif "ajouter" in requestEdit or "ajoute" in requestEdit or "rajoute" in requestEdit:
				self.addElements(requestEdit, activeListName)

			elif "supprimer" in requestEdit or "supprime" in requestEdit or unicode("enlève", 'utf-8') in requestEdit:
				return



	def addElements(self, requestEdit, activeListName):
		"""
		Add an element to an existing list

		Parameters :
			requestEdit - The user's request
			activeList  - The active list name
		"""

		banishedWords = ['ajouter','ajoute','rajoute','du','la','les','le','des','une','un','et', 'de']
		newElements = list()

		for element in requestEdit:
			if element not in banishedWords:
				newElements.append(element)

		if len(newElements) == 0:
			self.audioDeviceManager.speakAnswer("Je n'ajoute rien à la liste.")
			return

		self.answer = u"J'ajoute les elements : ".encode('utf-8')

		for element in newElements:
			self.answer += element.encode('utf-8') + ', '

		self.answer += u" à la liste de courses ".encode('utf-8') + activeListName.encode('utf-8')
		self.audioDeviceManager.speakAnswer(self.answer)

		self.shoppingLists[activeListName].extend(newElements)
		return



