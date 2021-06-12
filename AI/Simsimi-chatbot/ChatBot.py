from SpeechToText import SpeechToText
from TextToSpeech import TextToSpeech
import json
import requests
class ChatBot:
    def __init__(self):
        self.url=r" https://wsapi.simsimi.com/190410/talk"
        self.headers={
            'Content-Type':"application/json",
            'x-api-key':r"iNMdtwZ9J997_ARhm06s3LMcvgWIdBq7vt3ejYMf"
        }
        self.inp=SpeechToText()
        self.out=TextToSpeech('simsimi.mp3')
    def chat(self):
        while (True):   
            self.inp.changeSpeechToText() 
            self.message=self.inp.get_out()
            if self.message=='dừng lại':
                break
                print("The conversation stopped")
            self.payload ="{\n\t\"utext\": \""+ self.message +"\", \n\t\"lang\": \"vi\" \n}"
            self.payload=self.payload.encode("utf-8")
            response =requests.post(self.url,data=self.payload,headers=self.headers)
            if response.status_code==200:
                response=json.loads(response.text)
                print ("SIMSIMI : ",response['atext'])
                self.out.changeTextToSpeech(response['atext'])