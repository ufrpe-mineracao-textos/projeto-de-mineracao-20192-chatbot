from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd
import numpy as np
import os

path = ''
#data_list = os.listdir(path)


data = pd.read_csv('text-label.csv', encoding='utf8', index_col=False)

data_text = data['text']
data_label = data['label'].drop_duplicates()
print("Labels ", data_label[0])
print('Text sample: ', data_text[0])

tf_idf_dic = {}
# Applying count vectorizer

for label in data_label:
    text = data[data['label'] == label]['text']

    print(label)
    count = CountVectorizer()
    count_vec = count.fit_transform(text.values.astype('U'))
    print("Counting shape: ", count_vec.shape)

    # Applying TF_IDF transform

    tf_idf = TfidfTransformer()
    tf_idf_vec = tf_idf.fit_transform(count_vec)
    print("TF-IDF shape: ", tf_idf_vec.shape)

    tf_idf_dic[label] = tf_idf_vec


