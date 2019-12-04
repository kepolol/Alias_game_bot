# main.py

import requests
import json
from flask import Blueprint, render_template, request, redirect

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return 'OK'
