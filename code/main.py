import os
#os.system("pip install chatterbot")
#os.system("pip install chatterbot-corpus")
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer
#from chatterbot import chatterbot_corpus

bot = ChatBot(
    'TW Chat Bot',
    #storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=['chatterbot.logic.BestMatch'],
    #database_uri='mongodb://localhost:27017/faq'
    )

#conversa = ['Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo', 'Você gosta de programar?', 'Sim, eu programo em Python']
#trainer = ListTrainer(bot)
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.Portuguese")

while True:
    pergunta = input("Usuário: ")
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.2:
        print('FAQ Bot: ', resposta)
    else:
        print('TW Bot: Ainda não sei responder esta pergunta')