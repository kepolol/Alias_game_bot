from app import create_app
import os
import yadisk


if __name__ == "__main__":
    y = yadisk.YaDisk(token='AgAAAAA7LnbJAAYCAyDjyqmIDUXeoGtgE9eDzvM')
    y.download('data/word2vec.model', 'data/word2vec.model')
    y.download('data/word2vec_idx.ann', 'data/word2vec_idx.ann')
    y.download('data/word2vec_idx.ann.d', 'data/word2vec_idx.ann.d')
    app = create_app()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
