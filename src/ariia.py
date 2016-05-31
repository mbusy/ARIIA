# -*- coding: utf-8 -*-

import time
import urllib2
 
import audio_device_manager as adm
import key_event_listener as kel
import talk_manager as tm
import meteo_scrapper as ms
import history_scrapper as hs
import shopping_list_manager as slm


class Ariia:
    """
    Motherclass of the project, the domotic assistant
    """


    def __init__(self):
        """
        Constructor
        """
        
        self.keyEventListener   = kel.KeyEventListener()
        self.audioDeviceManager = adm.AudioDeviceManager(self.keyEventListener)
        self.talkManager        = tm.TalkManager()
        self.audio              = None
        self.speech             = None

        self.answer             = None
        self.request            = list()
        self.cityList           = list()
        self.meteoScrapper      = ms.MeteoScrapper()
        self.historyScrapper    = hs.HistoryScrapper()
        self.keywords           = dict()

        self.resetKeywords()



    def cleanStop(self):
        """
        Used to correctly stop all the active tasks 
        """

        self.keyEventListener.unregisterListener()



    def interaction(self):
        """
        Interact with the user, main interface 
        between Ariia and the user.
        """
        
        self.speech = self.audioDeviceManager.listenAndCreateSpeech()
        self.analyseSpeech()
        self.audioDeviceManager.speakAnswer(self.answer)



    def resetKeywords(self):
        """
        Reset the keywords
        """

        # Keaywords Booleans dictionnaire
        self.keywords["Aria"]       = False
        self.keywords["date"]       = False
        self.keywords["jour"]       = False
        self.keywords["heure"]      = False
        self.keywords["meteo"]      = False        
        self.keywords["lHeure"]     = False
        self.keywords["liste"]      = False
        self.keywords["courses"]    = False

        self.keywords["est"]        = False
        self.keywords["es"]         = False
        self.keywords["sommesNous"] = False
        self.keywords["es-tu"]      = False
        self.keywords["etait"]      = False
        self.keywords["suis-je"]    = False
        self.keywords["tAppelles"]  = False
        self.keywords["sais"]       = False

        self.keywords["comment"]    = False
        self.keywords["qui"]        = False

        self.keywords["faire"]      = False

        self.keywords["tu"]         = False

        self.keywords["de"]         = False

        # Flush keywords kists
        del self.request[:]
        del self.cityList[:]



    def analyseSpeech(self):
        """
        Analyse the speech of the user and trigger answering methods
        """

        self.answer = ""
        self.resetKeywords()


        try:
            assert self.speech is not None

        except AssertionError:
            self.speech = "nsSpeechText"


        for word in self.speech.split(" "):
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

            elif word.lower() == "comment":
                self.keywords["comment"] = True

            elif word.lower() == "t'appelles":
                self.keywords["tAppelles"] = True

            elif word.lower() == "sais":
                self.keywords["sais"] = True

            elif word.lower() == "faire":
                self.keywords["faire"] = True

            elif word.lower() == "es":
                self.keywords["es"] = True

            elif word.lower() == "qui":
                self.keywords["qui"] = True

            elif word.lower() == "tu":
                self.keywords["tu"] = True

            elif word.lower() == "es-tu":
                self.keywords["es-tu"] = True

            elif word.lower() == "suis-je":
                self.keywords["suis-je"] = True

            elif word.lower() == unicode("était", 'utf-8'):
                self.keywords["etait"] = True

            elif word.lower() == "liste":
                self.keywords["liste"] = True

            elif word.lower() == "de":
                self.keywords["de"] = True

            elif word.lower() == "courses":
                self.keywords["courses"] = True


        if self.keywords["heure"] and self.keywords["est"] or self.keywords["heure"] or self.keywords["lHeure"]:
            self.giveHour()

        if self.keywords["date"] and self.keywords["est"] or self.keywords["date"] or self.keywords["jour"] and self.keywords["sommesNous"]:
            self.giveDate()
        
        if self.keywords["meteo"]:
            self.giveMeteo()

        if self.keywords["qui"] and self.keywords["etait"]:
            self.giveHistory()

        if self.keywords["liste"] and self.keywords["de"] and self.keywords["courses"]:
            self.manageShoppingLists()

        # if self.keywords["comment"] and self.keywords["tAppelles"]:
        #     self.basicAnswer("aria")

        # if len(self.request) == 1 and self.keywords["Aria"]:
        #     self.basicAnswer("oui")

        # if self.keywords["tu"] and self.keywords["sais"] and self.keywords["faire"]:
        #     self.basicAnswer("jeSaisFaire")

        # if self.keywords["qui"] and self.keywords["es-tu"]:
        #     self.basicAnswer("presentationAria")

        # if self.keywords["qui"] and self.keywords["suis-je"]:
        #     self.basicAnswer("presentationHumain")

        if self.answer == "":
            self.answer = self.talkManager.getTalk(self.speech)

        return self.answer



    def basicAnswer(self, answerFlag):
        """
        Gives a basic answer

        Parameters :
            answerFlag - The flag given for a specific answer
        """

        if answerFlag == "oui":
            self.answer = "Oui ?"

        elif answerFlag == "aria":
            self.answer = " Je m'appelle Aria, avec deux iii."

        elif answerFlag == "jeSaisFaire":
            self.answer = u"Pour le moment, je ne sais pas faire grand chose. Mais je vais m'améliorer ! ".encode('utf-8')

        elif answerFlag == "presentationAria":
            self.answer = "Je m'appelle Aria, et je suis une assistance domotique."

        elif answerFlag == "presentationHumain":
            self.answer = u"Je suis presque sûre que tu es un humain !".encode('utf-8')



    def giveHour(self):
        """
        Gives the hour
        """
        currentTime = time.localtime()
        self.answer += " Il est actuellement " + str(currentTime[3]) + " heure " + str(currentTime[4]) + "."



    def giveDate(self):
        """
        Gives the date
        """

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
        """
        Gives meteo data for a specific city

        Note : For now this method is in alpha version, can retreive meteo data from cities in "ile de france"
        """

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
                self.answer += u" à ".encode('utf-8') + city.encode('utf-8') + ": "

                if self.meteoScrapper.sky is not "":
                    self.answer += " le ciel est "
                    self.answer += self.meteoScrapper.sky
                    self.answer += ", "

                if self.meteoScrapper.temperature is not "":
                    self.answer += " Il fait"
                    self.answer += self.meteoScrapper.temperature
                    self.answer += u" degrés".encode('utf-8')
                    self.answer += ", "

                if self.meteoScrapper.wind is not "":
                    self.answer += " Il y a "
                    self.answer += self.meteoScrapper.wind
                    self.answer += "."

            except urllib2.HTTPError:
                self.answer += u" Je n'ai pas de données météo pour la ville : ".encode('utf-8')
                self.answer += " " + city.encode('utf-8')
                self.answer += "."



    def giveHistory(self):
        """
        Gives historical data
        """

        historicName    = list()
        historicNameStr = ""

        for word in self.request:
            if word is not "Aria":
                for letter in word:
                    letterUpper = letter.upper()
                    if letter == letterUpper:
                        historicName.append(word)
                        historicNameStr += word + " "
                    
                    break

        try:
            
            self.historyScrapper.getHistoricDescription(historicName)
            self.answer += self.historyScrapper.historicResume

        except Exception:
            self.answer += u"Je n'ai pas de données historiques pour le personnage : ".encode('utf-8')
            self.answer += historicNameStr.encode('utf-8')
            self.answer += u", ou ces données sont corrompues.".encode('utf-8')



    def manageShoppingLists(self):
        """
        Manage the shopping lists of the user.
        """

        self.shoppingListManager = slm.ShoppingListManager(self.audioDeviceManager)
        self.shoppingListManager.manageShoppingLists()    
        self.answer = "Je ferme mon application de liste de courses."


def main():
    """
    Main method to launch ARIIA
    """

    ariia = Ariia()

    try:
        while True:
            ariia.interaction()

    except KeyboardInterrupt:
        print "exiting..."
        ariia.cleanStop()

if __name__ == "__main__":
    main()