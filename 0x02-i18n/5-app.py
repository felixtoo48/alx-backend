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
    # Check if locale parameter is present in the request's query parameters
    requested_locale = request.args.get('locale', '')

    # Check if the requested locale is in the list of supported languages
    if requested_locale and requested_locale in app.config['LANGUAGES']:
        return requested_locale

    # If no locale parameter or an unsupported locale is provided
    # fall back to the previous behavior
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# babel.init_app(app, locale_selector=get_locale)


# Set the app's config to use the Config class
app.config.from_object(Config)


@app.route('/')
def index():
    """ index definition returning render template"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
