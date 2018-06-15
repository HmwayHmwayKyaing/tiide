from flask import Flask

app = Flask(__name__)

@app.route("/tiide")
def hello():
    return "Hello World"

@app.route("/tiide")
def tiide():
    return "Welcome to TIIDE World"
