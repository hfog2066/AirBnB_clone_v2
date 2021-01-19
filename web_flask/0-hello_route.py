#!/usr/bin/python3
"""flask"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """route"""
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
