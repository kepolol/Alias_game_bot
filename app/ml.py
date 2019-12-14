from gensim.models import Word2Vec
from gensim.similarities.index import AnnoyIndexer
from app.data_preparation import lemmatize_stemming
import os
import nltk
nltk.data.path.append(os.getcwd())


class Predictor:
    def __init__(self):
        self.model = Word2Vec.load('data/word2vec.model')
        self.vocab = self.model.wv.vocab
        self.annoy_index = AnnoyIndexer()
        self.annoy_index.load('data/word2vec_idx.ann')
        self.annoy_index.model = self.model

    def explain(self, word, n_words):
        try:
            ans_words = self.model.wv.most_similar(positive=[lemmatize_stemming(word)],
                                                   topn=n_words, indexer=self.annoy_index)
            return [word[0] for word in ans_words]
        except KeyError:
            return 'Wrong word'

    def guess(self, words, n_words):
        try:
            ans_words = self.model.wv.most_similar(
                positive=[lemmatize_stemming(word) for word in words
                          if lemmatize_stemming(word) in self.vocab], topn=n_words)
            return [word[0] for word in ans_words]
        except ValueError:
            return 'Wrong word'
