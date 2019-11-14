import os
#os.system("pip install chatterbot")
#os.system("pip install chatterbot-corpus")
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from chatterbot import ChatBot
import pymongo
#from chatterbot.trainers import ChatterBotCorpusTrainer
#from chatterbot import chatterbot_corpus
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["chatbot"]
mycol = mydb["chatbot"]
conversa = []
for x in mycol.find():
  conversa.append(x['input'])
  conversa.append(x['output'])

bot = ChatBot(
    'TW Chat Bot',
    #storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=['chatterbot.logic.BestMatch'],
    #database_uri='mongodb://localhost:27017/faq'
    )

trainerList = ListTrainer(bot)
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.Portuguese")
trainerList.train(conversa)

while True:
    pergunta = input("Usuário: ")
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.2:
        print('FAQ Bot: ', resposta)
    else:
        print('TW Bot: Ainda não sei responder esta pergunta')