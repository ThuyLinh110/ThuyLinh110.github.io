from SpeechToText import SpeechToText
from TextToSpeech import TextToSpeech
import json
import requests
class ChatBot:
    def __init__(self):
        self.url=r" https://wsapi.simsimi.com/190410/talk"
        self.headers={
            'Content-Type':"application/json",
            'x-api-key':r"e2wqSRg0i7ppJPD8aGVLvD6EIsy6J-BzeXyxPCcf"
        }
        self.inp=SpeechToText()
        self.out=TextToSpeech('simsimi.mp3')
    def chat(self):
        while (True):   
            self.inp.changeSpeechToText() 
            self.message=self.inp.get_out()
            self.payload ="{\n\t\"utext\": \""+ self.message +"\", \n\t\"lang\": \"vi\" \n}"
            self.payload=self.payload.encode("utf-8")
            response =requests.post(self.url,data=self.payload,headers=self.headers)
            response=json.loads(response.text)
            print ("Simsimi : ",response['atext'])
            self.out.changeTextToSpeech(response['atext'])