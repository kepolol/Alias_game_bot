# main.py

from app.ml import Predictor
import json
from flask import Blueprint, render_template, request, redirect

main = Blueprint('main', __name__)
predictor = Predictor()


@main.route('/explain')
def explain():
    print(request.args)
    word = request.args.get('word')
    n_words = int(request.args.get('n_words'))

    return json.dumps(predictor.explain(word=word, n_words=n_words))


@main.route('/guess')
def guess():
    words = request.args.getlist('words')
    n_words = int(request.args.get('n_words'))
    return json.dumps(predictor.guess(words=words, n_words=n_words))
