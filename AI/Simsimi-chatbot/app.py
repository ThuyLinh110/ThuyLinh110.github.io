import speech_recognition as sr
from gtts import gTTS
import json
import requests
import playsound
import os
import keyboard
class SpeechToText:
    def __init__(self):  
        with sr.Microphone() as source:   
            print("Press Enter to say ")
            while True: 
             try: 
                if keyboard.is_pressed('Enter'):
                    print("say something.....")
                    r= sr.Recognizer()  
                    self.__inp = r.record(source,duration=2)
                    break  
             except:
                 break

    def changeSpeechToText(self):
        try:
            self.__out=sr.Recognizer().recognize_google(self.__inp,language="vi")
            print("You said: "+ self.__out)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            self.__out=" "
            print("You said: "+ self.__out)
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition")
    def get_out(self):
        return self.__out

class TextToSpeech:
    def __init__(self,inp):
        self.__inp=inp
    def changeTextToSpeech(self):
        tts=gTTS(text=self.__inp,lang='vi')
        tts.save('simsimi.mp3')
        playsound.playsound('simsimi.mp3')
        os.remove('simsimi.mp3')
class ChatBot:
    def __init__(self):
        self.__url=r" https://wsapi.simsimi.com/190410/talk"
        self.__headers={
            'Content-Type':"application/json",
            'x-api-key':r"e2wqSRg0i7ppJPD8aGVLvD6EIsy6J-BzeXyxPCcf"
        }
    def chat(self):
        while (True):
            voice= SpeechToText()    
            voice.changeSpeechToText() 
            self.__message=voice.get_out()
            self.__payload ="{\n\t\"utext\": \""+ self.__message +"\", \n\t\"lang\": \"vi\" \n}"
            self.__payload=self.__payload.encode("utf-8")
            response =requests.post(self.__url,data=self.__payload,headers=self.__headers)
            response=json.loads(response.text)
            print ("Simsimi : ",response['atext'])
            voice1=TextToSpeech(response['atext'])
            voice1.changeTextToSpeech()
chatbot=ChatBot()
chatbot.chat()


