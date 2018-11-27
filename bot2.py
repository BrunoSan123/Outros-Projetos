# -*- coding: utf-8 -*-

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot("Maquina que fala")

convI = ["oi", "oi meu chapa/minha chapa", "tudo bem?", "sim e com vc?","Vou otimo!!!!"]
convF = ["Que filmes gosta", "de varios", "que massa"]
bot.set_trainer(ListTrainer)

bot.train(convI)
bot.train(convF)




while True:
     quest = input("voce: ")

     response = bot.get_response(quest)


     print("bot: ",response)



