#!/usr/bin/python3
"""flask"""

from flask import Flask, render_template
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


@app.route('/python',
           defaults={"text": "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """route"""
    return "Python %s" % text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """route"""
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """route"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """route"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
