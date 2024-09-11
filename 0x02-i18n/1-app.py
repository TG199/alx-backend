#!/usr/bin/env python3
"""
Simple route module
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """
    Home route
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
