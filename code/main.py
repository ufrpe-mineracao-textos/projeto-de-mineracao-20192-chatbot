import os
os.system("pip install chatterbot")
os.system("pip install chatterbot-corpus")
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
#from chatterbot import chatterbot_corpus

bot = ChatBot('TW Chat Bot')

conversa = ['Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo',
            'Você gosta de programar?', 'Sim, eu programo em Python']

trainer = ListTrainer(bot)
trainer.train(conversa)

while True:
    pergunta = input("Usuário: ")
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('TW Bot: ', resposta)
    else:
        print('TW Bot: Ainda não sei responder esta pergunta')