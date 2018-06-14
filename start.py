from flask import Flask

myapp = Flask(__name__)

@myapp.route("/hmwayhmway")
def hmwayhmway():
    return "Hello hmwayhmway"

@myapp.route("/tiide")
def tiide():
    return "Welcome to TIIDE World"
