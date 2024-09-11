#!/usr/bin/env python3
"""
Simple babel module
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _


app = Flask(__name__)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    Config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.locale_selector_func
def get_locale():
    """
    Get locale function
    """
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """
    before req function
    """
    g.user = get_user()


@app.route('/')
def index():
    """
    Home route
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
