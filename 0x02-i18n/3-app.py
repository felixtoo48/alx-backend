#!/usr/bin/env python3
""" Flask app """

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config(object):
    """ configuring available languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


babel = Babel(app)


@babel.localeselector
def get_locale():
    """ defining accepted languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# babel.init_app(app, locale_selector=get_locale)


# Set the app's config to use the Config class
app.config.from_object(Config)


@app.route('/')
def index():
    """ index definition returning render template"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
