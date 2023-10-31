#!/usr/bin/env python3
""" Flask app """

from flask import Flask, render_template
from app import app

app = Flask(__name__)


@app.route('/')
# @app.route('/index')

def index():
    """ index defin returning render template"""
    return render_template('templates/0-index.html')
