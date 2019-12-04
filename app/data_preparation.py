import gensim.downloader as api
import gensim
from nltk.stem import WordNetLemmatizer, PorterStemmer
import re
from gensim.models import Word2Vec
from os import cpu_count


def lemmatize_stemming(sentence):
    stemmer = PorterStemmer()
    return stemmer.stem(WordNetLemmatizer().lemmatize(sentence, pos='v'))


def preprocess(sentence):
    result=[]
    for token in gensim.utils.simple_preprocess(sentence) :
        if token not in gensim.parsing.preprocessing.STOPWORDS:
            result.append(lemmatize_stemming(token))
    return result


def text2sentences(text):
    without_header = '\n'.join(text.split('\n\n')[1:])
    u = re.sub(r'(^[\t]+|[\t]+|[\n]{2,}|[\^]+|[><]+|[0-9]+|[\'\"]+|`|'
               r'[\(\)\[\]]+|[\\/_\|\:;]+)', '', without_header)
    l = re.sub(r'([-]+|\n)', ' ', u)
    n = re.sub(r'\s\.', '.', l)
    m = re.sub(r'[\w\._\+\-]+@[\w\._\+\-]+|[\.]{2,}|,', '', n)
    r = re.sub(r'[\s]{2,}', ' ', m)
    o = re.split(r'\.|\?!|!\?|[!\?]+', r)
    ans = [sentence.strip().lower() for sentence in o if (sentence.strip() != '') & (len(sentence.strip())>3)]
    return ans


if __name__ == '__main__':
    data = api.load("20-newsgroups", return_path=False)
    all_sentences = []
    for text in data:
        all_sentences.extend(text2sentences(text['data']))
    preprocessed_sentences = []
    for sentence in all_sentences:
        preprocessed_sentences.append(preprocess(sentence))
    w2v_model = Word2Vec(min_count=20, window=2, size=300, sample=6e-5, alpha=0.03,
                         min_alpha=0.0007, negative=20, workers=cpu_count())
    w2v_model.build_vocab(preprocessed_sentences, progress_per=1)
    w2v_model.train(preprocessed_sentences, total_examples=w2v_model.corpus_count, epochs=60, report_delay=1.0)
    w2v_model.init_sims(replace=True)
    w2v_model.save("data/word2vec.model")
