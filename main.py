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
def get(client_name=''):
    client_a_requests = [
        {
            "title":"Make Web App",
            "description": "Hopefully this doesn't take too long",
        },
        {
            "title":"Make Web App Again",
            "description": "Two are better than one (most of the time)",
        },
    ]

    client_b_requests = [
        {
            "title":"Cook a sandwich",
            "description": "Grilled Cheese if you please",
        },
        {
            "title":"Brew Coffee",
            "description": "Medium Roast, with cream",
        },
    ]

    client_c_requests = [
        {
            "title":"Take over the world",
            "description": "The same thing we do every night.",
        },
        {
            "title":"Retrieve the carrots",
            "description": "From the farmer's garden",
        },
    ]
    client_requests = []
    if client_name == 'client_a':
        client_requests = client_a_requests
    elif client_name == 'client_b':
        client_requests = client_b_requests
    elif client_name == 'client_c':
        client_requests = client_c_requests

    return jsonify(client_requests)
