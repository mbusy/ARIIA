# -*- coding: utf-8 -*-

import speech_recognition as sr
from gtts import gTTS
import mp3play
import time
import urllib2

import meteo_scrapper as ms


class SpeechAnalyser:
    """
    Used to analyse the user speech
    """

    def __init__(self):
        self.answer        = None
        self.request       = list()
        self.cityList      = list()
        self.meteoScrapper = ms.MeteoScrapper()
        self.keywords      = dict()

        self.resetKeywords()

    def resetKeywords(self):

        # Keaywords Booleans dictionnaire
        self.keywords["Aria"]       = False
        self.keywords["heure"]      = False
        self.keywords["lHeure"]     = False
        self.keywords["est"]        = False
        self.keywords["date"]       = False
        self.keywords["jour"]       = False
        self.keywords["sommesNous"] = False
        self.keywords["meteo"]      = False

        # Flush keywords kists
        del self.request[:]
        del self.cityList[:]

    def analyseSpeech(self, speech):

        self.answer = ""
        self.resetKeywords()

        for word in speech.split(" "):
            self.request.append(word)

        for word in self.request:
            if word.lower() == "aria":
                self.keywords["Aria"] = True

            elif word.lower() == "heure":
                self.keywords["heure"] = True

            elif word.lower() == "l'heure":
                self.keywords["lHeure"] = True

            elif word.lower() == "est":
                self.keywords["est"] = True

            elif word.lower() == "date":
                self.keywords["date"] = True

            elif word.lower() == "jour":
                self.keywords["jour"] = True

            elif word.lower() == "sommes-nous":
                self.keywords["sommesNous"] = True
            
            elif word.lower() == unicode("météo", 'utf-8'):
                self.keywords["meteo"] = True

        if self.keywords["heure"] and self.keywords["est"] or self.keywords["heure"] or self.keywords["lHeure"]:
            self.giveHour()

        if self.keywords["date"] and self.keywords["est"] or self.keywords["date"] or self.keywords["jour"] and self.keywords["sommesNous"]:
            self.giveDate()
        
        if self.keywords["meteo"]:
            self.giveMeteo()

        if len(self.request) == 1 and self.keywords["Aria"]:
            self.basicAnswer()

        # Variable for the no keyword detection
        anyKeywordsDetected = False

        for keywordDetected in self.keywords.values():
            anyKeywordsDetected = anyKeywordsDetected or keywordDetected

        if not anyKeywordsDetected:
            self.answer = "Je ne comprends pas."

        return self.answer


    def basicAnswer(self):
        self.answer = "Oui ?"

    def giveHour(self):
        currentTime = time.localtime()
        self.answer += " Il est actuellement " + str(currentTime[3]) + " heure " + str(currentTime[4]) + "."

    def giveDate(self):
        currentTime = time.localtime()

        if currentTime[1] == 1:
            month = "janvier"
        elif currentTime[1] == 2:
            month = "fevrier"
        elif currentTime[1] == 3:
            month = "mars"
        elif currentTime[1] == 4:
            month = "avril"
        elif currentTime[1] == 5:
            month = "mai"
        elif currentTime[1] == 6:
            month = "juin"
        elif currentTime[1] == 7:
            month = "juillet"
        elif currentTime[1] == 8:
            month = "aout"
        elif currentTime[1] == 9:
            month = "septembre"
        elif currentTime[1] == 10:
            month = "octobre"
        elif currentTime[1] == 11:
            month = "novembre"
        elif currentTime[1] == 12:
            month = "decembre"
        
        self.answer += " Nous sommes le " + str(currentTime[2]) + month + str(currentTime[0]) + "."

    def giveMeteo(self):
        for word in self.request:
            if word is not "Aria":
                for letter in word:
                    letterUpper = letter.upper()
                    if letter == letterUpper:
                        self.cityList.append(word)
                    
                    break

        self.answer += u" voici la météo : ".encode('utf-8')

        for city in self.cityList:

            try:
                
                self.meteoScrapper.getMeteo(city)

                self.answer += " Il fait"
                self.answer += self.meteoScrapper.temperature
                self.answer += u" degrés à".encode('utf-8')
                self.answer += " " + city.encode('utf-8')
                self.answer += "."

            except urllib2.HTTPError:
                self.answer += u" Je n'ai pas de données météo pour la ville : ".encode('utf-8')
                self.answer += " " + city.encode('utf-8')
                self.answer += "."

            #TODO : Unicode cities




def playMp3():
    clip = mp3play.load("test.mp3")
    clip.play()
    time.sleep(clip.seconds())
    clip.stop()


def main():

    # obtain audio from the microphone
    r = sr.Recognizer()
    m = sr.Microphone()
    s = SpeechAnalyser()


    # Calibration of the noise
    print ("a moment of silence...")
    with m as source : r.adjust_for_ambient_noise(source)
    print("Minimum energy threshold set to {}".format(r.energy_threshold))


    while True:

        with m as source:
            print("Listening !")
            audio = r.listen(source)
            print ("Computing...")


        # recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            recognized_audio = r.recognize_google(audio, language='fr')
            print("You said " + recognized_audio)
            
            answer = s.analyseSpeech(recognized_audio)

            tts = gTTS(text=answer, lang="fr")
            tts.save("test.mp3")
            playMp3()

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from online service; {0}".format(e))


if __name__ == "__main__":
    main()