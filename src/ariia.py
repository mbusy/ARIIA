# -*- coding: utf-8 -*-
#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
from gtts import gTTS
import mp3play
import time
import urllib2
import cookielib

class SpeechAnalyser:
    """
    Used to analyse the user speech
    """

    def __init__(self):
        self.answer    = None
        self.request   = list()
        self.cookieJar = cookielib.CookieJar()
        self.opener    = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookieJar))

        self.resetKeywords()

    def resetKeywords(self):

        # Keaywords Booleans
        self.bAria       = False
        self.bHeure      = False
        self.bLHeure     = False
        self.bEst        = False
        self.bDate       = False
        self.bJour       = False
        self.bSommesNous = False
        self.bMeteo      = False

        #Keywords Lists
        self.cityList = list()

    def analyseSpeech(self, speech):

        self.answer = ""
        self.resetKeywords()

        for word in speech.split(" "):
            self.request.append(word)

        for word in self.request:
            if word.lower() == "aria":
                self.bAria = True

            elif word.lower() == "heure":
                self.bHeure = True

            elif word.lower() == "l'heure":
                self.bLHeure = True

            elif word.lower() == "est":
                self.bEst = True

            elif word.lower() == "date":
                self.bDate = True

            elif word.lower() == "jour":
                self.bJour = True

            elif word.lower() == "sommes-nous":
                self.bSommesNous = True
            
            elif word.lower() == unicode("météo", 'utf-8'):
                self.bMeteo = True

        if self.bHeure and self.bEst or self.bHeure or self.bLHeure:
            self.giveHour()

        if self.bDate and self.bEst or self.bDate or self.bJour and self.bSommesNous:
            self.giveDate()
        
        if self.bMeteo:
            self.giveMeteo()

        elif self.bAria:
            self.basicAnswer()

        else:
            self.answer = "Je ne comprends pas"

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

        self.answer += u" voici la météo. ".encode('utf-8')

        for city in self.cityList:
            # Works for the Ile de France cities, in France, for now
            url = "http://www.yr.no/place/France/%C3%8Ele-de-France/" + city + "/"
            httpRequest = urllib2.Request(url)
            page = self.opener.open(httpRequest)
            rawdata = page.read()
            lines_of_data = rawdata.split('\n')
            special_lines = [line for line in lines_of_data if line.find('og:description')>-1]
            info = special_lines[0].replace('"','').split('content=')[1]
            sections = info.split(':')
            sectionsRefined = sections[3].split(',')
            
            for temperatureData in sectionsRefined[1].split(" "):
                pass

            self.answer += " Il fait"
            self.answer += temperatureData
            self.answer += u" degrés à".encode('utf-8')
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