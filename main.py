from flask import Flask, request, render_template, jsonify

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

@app.route("/get/<client_name>")
def get(client_name):
    client_requests = [
        {
            "title":"Make Web App",
            "description": "Hopefully this doesn't take too long",
        },
        {
            "title":"Make Web App Again",
            "description": "Two are better than one (most of the time)",
        },
    ]
    return jsonify(client_requests)
