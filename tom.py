import re
import speech_recognition as sr 
from gtts import gTTS
import os
from playsound import playsound

r = sr.Recognizer()
with sr.Microphone () as source:
    print('speak any thing:')
    audio = r.listen(source)

language = 'en'
words = r.recognize_google(audio)
output = gTTS(text=words, lang=language, slow=False)

output.save("hello.mp3")
playsound("hello.mp3")