# main.py

from app.ml import Predictor
import json
from flask import Blueprint, request

main = Blueprint('main', __name__)
predictor = Predictor()


@main.route('/')
def home():
    return json.dumps('Hello')


@main.route('/explain')
def explain():
    word = request.args.get('word')
    n_words = int(request.args.get('n_words'))
    return json.dumps(predictor.explain(word=word, n_words=n_words))


@main.route('/guess')
def guess():
    words = request.args.getlist('words')
    print(words)
    n_words = int(request.args.get('n_words'))
    return json.dumps(predictor.guess(words=words, n_words=n_words))
