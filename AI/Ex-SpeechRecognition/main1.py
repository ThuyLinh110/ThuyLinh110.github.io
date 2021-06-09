from gtts import gTTS
inp =input("write something: ")
tts = gTTS(inp)
tts.save('hello.mp3')