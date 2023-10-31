#!/usr/bin/env python3
""" Flask app """

from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone, UnknownTimeZoneError

app = Flask(__name__)


class Config(object):
    """ configuring available languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """ defining accepted languages"""
    # Check if locale parameter is present in the request's query parameters
    requested_locale = request.args.get('locale', '')

    # Check if the requested locale is in the list of supported languages
    if requested_locale and requested_locale in app.config['LANGUAGES']:
        return requested_locale

    # Locale from user settings
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    # Locale from request header
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config['LANGUAGES']:
        return header_locale

    # If no locale parameter or an unsupported locale is provided
    # fall back to the previous behavior
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# babel.init_app(app, locale_selector=get_locale)


# Set the app's config to use the Config class
app.config.from_object(Config)


def get_user():
    """returns user dictionary or None if ID cannot be found """
    login_id = request.args.get("login_as")

    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request():
    """ run before request """
    g.user = get_user()


@babel.timezoneselector
def get_timezone():
    """Get user timezone
    """
    # timezone parameter from URL parameters
    tz = request.args.get('timezone', '').strip()
    if not tz and g.user:
        # timezone from the user settings
        tz = g.user['timezone']
    try:
        return timezone(tz).zone
    except UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def login():
    """ index definition returning render template"""
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
