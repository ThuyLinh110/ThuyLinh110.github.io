import speech_recognition as sr
import keyboard
class SpeechToText:
    def __init__(self):   
        self.inp=None
    def changeSpeechToText(self):
        
        while True:  
            r =sr.Recognizer()
            try:
                print("say something...")
                with sr.Microphone() as source:   
                    self.inp= r.record(source,duration=5)
                    self.out= r.recognize_google(self.inp,language="vi")
                    print("You : ",self.out)
                    break
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
                print("Press Enter to say again !" )
                keyboard.wait("\n")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition")
                print("Press Enter to say again !")
                keyboard.wait("\n")
            r =sr.Recognizer()
    def get_out(self):
        return self.out