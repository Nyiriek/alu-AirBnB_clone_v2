#!/usr/bin/python3
"""
A script that starts a Flask application,
which listens on 0.0.0.0, port 5000.

Routes:
    /: Displays 'Hello HBNB'
    /hbnb: Displays 'HBNB'
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Defines a route for /hbnb to display HBNB"""
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
