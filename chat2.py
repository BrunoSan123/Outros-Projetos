
#-*-coding:utf-8-*-

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot


import speech_recognition as sr

import pyttsx3


bot =ChatBot("Logo")

chats = ["hi","hello","how are you?", "im fine", "thanks"]
bot.set_trainer(ListTrainer)
bot.train(chats)

r = sr.Recognizer()

with sr.Microphone() as s:
    r.adjust_for_ambient_noise(s)


while True:
    print("say something")
    audio = r.listen(s)
    speech = r.recognize_google(audio)

    
    print(bot.get_response(speech))


