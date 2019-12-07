from gensim.models import Word2Vec
from app.data_preparation import lemmatize_stemming
import os
import nltk
nltk.data.path.append(os.getcwd())


class Predictor:
    def __init__(self):
        self.model = Word2Vec.load('data/word2vec.model')
        self.vocab = self.model.wv.vocab

    def explain(self, word, n_words):
        try:
            ans_words = self.model.wv.most_similar(positive=[lemmatize_stemming(word)], topn=n_words)
            return [word[0] for word in ans_words]
        except KeyError:
            return 'Wrong word'

    def guess(self, words, n_words):
        try:
            ans_words = self.model.wv.most_similar(
                positive=[lemmatize_stemming(word) for word in words
                          if lemmatize_stemming(word) in vocab], topn=n_words)
            return [word[0] for word in ans_words]
        except ValueError:
            return 'Wrong word'
