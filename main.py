from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create/")
def create():
    if request.method == 'POST':
        return "create request"
    else:
        return "no data submitted"
