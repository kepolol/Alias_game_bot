# main.py

from app.ml import Player_guess, Player_explain
import json
from flask import Blueprint, request

main = Blueprint('main', __name__)
g = Player_guess()
e = Player_explain()
print('Model ready!')


@main.route('/')
def home():
    return json.dumps('Hello')


@main.route('/explain')
def explain():
    word = request.args.get('word')
    n_words = int(request.args.get('n_words'))
    return json.dumps(e.explain(word=word, n_words=n_words))


@main.route('/guess')
def guess():
    words = request.args.getlist('words')
    n_words = int(request.args.get('n_words'))
    return json.dumps(g.guess(words=words, n_words=n_words))
