import yadisk


y = yadisk.YaDisk(token='AgAAAAA7LnbJAAYCAyDjyqmIDUXeoGtgE9eDzvM')
y.download('data/word2vec.model', 'data/word2vec.model')
y.download('data/word2vec_idx.ann', 'data/word2vec_idx.ann')
y.download('data/word2vec_idx.ann.d', 'data/word2vec_idx.ann.d')
