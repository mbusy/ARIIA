# -*- coding: utf-8 -*-

import speech_recognition as sr
from gtts import gTTS
import mp3play
import time

class AudioDeviceManager:
	"""
	Class using the micrphone to listen to the user
	and converting the string answers to mp3 files.

	The class also have the option to play the mp3 files.
	"""

	def __init__(self, keyEventListener=None):
		"""
		Constructor

		Parameters :
			keyEventListener - A listener for the key events, None if not specified
		"""

		self.keyEventListener = keyEventListener
		self.recognizer 	  = sr.Recognizer()
		self.microphone 	  = sr.Microphone()
		self.audio      	  = None
		self.speech     	  = None
		self.minThresh  	  = 350

		self.noiseCalibration()



	def noiseCalibration(self):
		"""
		Calibration of the noise for the
		microphone
		"""
		
		print ("a moment of silence...")
		with self.microphone as source : self.recognizer.adjust_for_ambient_noise(source)
		
		if self.recognizer.energy_threshold < self.minThresh:
			self.recognizer.energy_threshold = self.minThresh

		print("Minimum energy threshold set to {}".format(self.recognizer.energy_threshold))



	def callback(self, recognizer, audio):
		"""
		Callback method allowing to stop the recording

		Parameters :
			recognizer - The recognizer (not used here, we use self.recognizer)
			audio - The audio (not used here, we use self.audio)
		"""

		try:
			self.speech += recognizer.recognize_google(audio, language='fr') + " "

		except sr.UnknownValueError:
			print "Could not understand audio"

		except sr.RequestError as e:
			print "Could not request results from online services : " + str(e)



	def listenAndCreateSpeech(self):
		"""
		Get an audio signal and convert it to an exploitable speech
		"""

		self.speech = ""

		if self.keyEventListener is not None:
			self.keyEventListener.waitKeyEvent()

		print "------------"
		print "listening"

		stopListening = self.recognizer.listen_in_background(self.microphone, self.callback)

		if self.keyEventListener is not None:
			self.keyEventListener.waitKeyEvent()
		
		print "------------"
		print "computing"
		stopListening()

		print "You said : " + self.speech
		return self.speech



	def speakAnswer(self, answer, file="../ressources/tts.mp3"):
		"""
		Speak the answer through the speakers

		Parameters :
			answer - The answer to be spoken
			file - File where the mp3 data is storred, 
				   ../ressources/tts.mp3 is the default value.
		"""

		try:
			tts = gTTS(text=answer, lang='fr')
			tts.save("../ressources/tts.mp3")

			self.playMp3File()

		except sr.UnknownValueError:
			print "Could not understand audio"

		except sr.RequestError as e:
			print "Could not request results from onlin services : " + str(e)



	def playMp3File(self, file="../ressources/tts.mp3"):
		"""
		Play an mp3 file
		
		Paramters :
			file - File where the mp3 data is storred, 
				   ../ressources/tts.mp3 is the default value.        
		"""

		try:
			clip = mp3play.load(file)
			clip.play()
			time.sleep(clip.seconds())
			clip.stop()

		except Exception:
			print "Could not play the mp3 file"