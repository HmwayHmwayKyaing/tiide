from flask import Flask

app = Flask(__name__)

@app.route("/hmwayhmway")
def hmwayhmway():
    return "Hello hmwayhmway"

@app.route("/tiide")
def tiide():
    return "Welcome to TIIDE World"
