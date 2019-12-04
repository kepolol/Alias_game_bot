# main.py

import requests
import json
from flask import Blueprint, render_template, request, redirect

main = Blueprint('main', __name__)


@main.route('/explain')
def explain():
    print(request.args)
    word = request.args.get('word')
    n_words = int(request.args.get('n_words'))

    return json.dumps(player.explain(word=word, n_words=n_words))


@main.route('/guess')
def guess():
    words = request.args.getlist('words')
    n_words = int(request.args.get('n_words'))
    return json.dumps(player.guess(words=words, n_words=n_words))
