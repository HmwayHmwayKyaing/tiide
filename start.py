from flask import Flask

app = Flask(__name__)

@app.route("/hmway")
def hmway():
    return "Hello World"

@app.route("/hmway")
def hmway():
    return "Welcome to TIIDE World"
