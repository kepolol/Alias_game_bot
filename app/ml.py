import gensim.downloader as api
import gensim
from nltk.stem import WordNetLemmatizer, PorterStemmer
import re
from gensim.models.phrases import Phrases, Phraser
from gensim.models import Word2Vec
from time import time
from os import cpu_count
from app.data_preparation import lemmatize_stemming


class Predictor:
    def __init__(self):
        self.model = Word2Vec.load('data/word2vec.model')

    def explain(self, word, n_words):
        ans_words = self.model.wv.most_similar(positive=[lemmatize_stemming(word)], topn=n_words)
        return [word[0] for word in ans_words]


    def guess(self, words, n_words):
        ans_words = self.model.wv.most_similar(positive=[lemmatize_stemming(word) for word in words], topn=n_words)
        return [word[0] for word in ans_words]
