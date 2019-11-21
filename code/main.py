#caso esteja usando o Conda, e não conseguir instalar os pacotes, execute essas linhas uma vez.
#import os #executar só na primeira vez
#os.system("pip install chatterbot") #executar só na primeira
#os.system("pip install chatterbot-corpus") #executar só na primeira
#os.system('pip install unidecode') #executar uma ves
#import nltk
#nltk.download('punkt') #executar uma vez
#os.system("python -m spacy download pt") #executar uma vez

import pymongo
import spacy
from nltk import word_tokenize
from nltk.corpus import stopwords
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from chatterbot import ChatBot
import unidecode

from chatterbot.comparisons import levenshtein_distance

#remover caracteres especiais, acentos, stopwords
nlp = spacy.load('pt')
def pre_process_spacy(entrada):
    doc = nlp(entrada)
    x = [token.lemma_.lower() for token in doc if not (token.is_stop or token.is_punct)]
    retorno = ''.join(x)
    retorno = unidecode.unidecode(retorno) #retirar acentor
    print("spacy:"+retorno)
    return retorno

def pre_process(input):
    stop_words = set(stopwords.words('portuguese'))
    word_tokens = word_tokenize(input)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    retorno = ''.join(filtered_sentence)
    retorno = unidecode.unidecode(retorno)
    print(retorno)
    return retorno

#pegar do banco mongodb os inputs e outputs do chatbot
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["chatbot"]
mycol = mydb["chatbot"]
conversa = []
for x in mycol.find():
    conversa.append(pre_process_spacy(x['input']))
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
    resposta = bot.get_response(pre_process_spacy(pergunta))
    print('FAQ Bot: ', resposta)
    if float(resposta.confidence) > 0.1:
        print('FAQ Bot: ', resposta, resposta.confidence)
    else:
        print('FAQ Bot: Ainda não sei responder esta pergunta')