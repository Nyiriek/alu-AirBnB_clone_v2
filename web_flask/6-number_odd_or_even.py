#!/usr/bin/python3
"""
A script that starts a Flask application,
which listens on 0.0.0.0, port 5000.

Routes:
    /: Displays 'Hello HBNB'
    /hbnb: Displays 'HBNB'
    /c/<text>: display “C ” followed by the value of\
        the text variable (replace underscore _ symbols with a space )
    /python/(<text>): display “Python ”, followed by the value\
        of the text variable (replace underscore _ symbols with a space )
    /number/<n>: display “n is a number” only if n is an integer
    /number_template/<n>: display a HTML page only if n is an integer:
    /number_odd_or_even/<n>: display a HTML page only if n is an integer:
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Defines a route for /hbnb to display HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of <text>"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Defines a route for '/python/<text>' with a default\
        value of 'is cool'"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Displays “n is a number” only if n is an integer"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays a HTML page only if n is an integer"""
    return render_template("5-number.html", n=n)


@app.route("number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """
    Displays a HTML page only if n is an integer.
    States whether n is odd or even. 
    """
    return render_template("6-number_odd_or_even.html", n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
