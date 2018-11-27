from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('test')

conversa = ['Oi','Olá', 'Tudo Bem?','Eu estou Bem']

bot.set_trainer(ListTainer)
bot.train(conversa)

