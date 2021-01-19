#!/usr/bin/python3
"""flask"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """route"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """route"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """route"""
    return "C %s" % text.replace("_", " ")

if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
