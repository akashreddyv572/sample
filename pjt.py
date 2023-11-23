from flask import Flask

app = Flask(__name__)

@app.route("/statement")
def hello_world():
    return "<p>Hello, all!</p>"