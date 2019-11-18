#import os
#os.system("pip install chatterbot")
#os.system("pip install chatterbot-corpus")
import re
import string
import numpy as np
import pymongo
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from chatterbot import ChatBot
from chatterbot.comparisons import levenshtein_distance


def clear_text(text):
    print(text)
    pattern = "[{}]".format(string.punctuation)
    text = [word.lower() for word in text]
    text = [[re.sub(pattern, "", word) for word in words.split()] for words in text]
    text = [[word for word in words if len(word)>1] for words in text]
    print(text)
    return text

#pegar do banco mongodb os inputs e outputs do chatbot
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["chatbot"]
mycol = mydb["chatbot"]
conversa = []
for x in mycol.find():
    print(x['input'])
    conversa.append(clear_text(x['input']))
    conversa.append(x['output'])

#inicialização do chatbnot
bot = ChatBot(
    'FAQ Bot',
    logic_adapters=['chatterbot.logic.BestMatch'],
    #statement_comparison_function=levenshtein_distance
    )

#treinar o chatbot com o corpus (pré-definido) e com a "conversa" que foi montada usando o mongodb
trainerList = ListTrainer(bot)
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.Portuguese.greetings")
trainer.train("chatterbot.corpus.Portuguese.compliment")
trainerList.train(conversa)

#executando
while True:
    pergunta = input("Usuário: ")
    resposta = bot.get_response(pergunta)
    print('FAQ Bot: ', resposta)
    if float(resposta.confidence) > 0.1:
        print('FAQ Bot: ', resposta)
    else:
        print('FAQ Bot: Ainda não sei responder esta pergunta')