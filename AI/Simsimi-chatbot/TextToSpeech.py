from gtts import gTTS
import playsound
import os
class TextToSpeech:
    def __init__(self,file):
        self.file=file
    def changeTextToSpeech(self,inp):
        tts=gTTS(text=inp,lang='vi')
        tts.save(self.file)
        playsound.playsound(self.file)
        os.remove(self.file)
