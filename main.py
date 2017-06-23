from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
feature_requests = [
    {
        "title":"Make Web App",
        "description": "Hopefully this doesn't take too long",
        "client": "client_a",
        "priority":1,
        "target_date":1504288565,
        "product_area":"Claims"
    },
    {
        "title":"Make Web App Again",
        "description": "Two are better than one (most of the time)",
        "client": "client_a",
        "priority":2,
        "target_date":1505238965,
        "product_area":"Policies"
    },
    {
        "title":"Cook a sandwich",
        "description": "Grilled Cheese if you please",
        "client": "client_b",
        "priority":1,
        "target_date":1507830965,
        "product_area":"Policies"
    },
    {
        "title":"Brew Coffee",
        "description": "Medium Roast, with cream",
        "client": "client_b",
        "priority":2,
        "target_date":1508349365,
        "product_area":"Billing"
    },
    {
        "title":"Take over the world",
        "description": "The same thing we do every night.",
        "client": "client_c",
        "priority":1,
        "target_date":1582048565,
        "product_area":"Policies"
    },
    {
        "title":"Retrieve the carrots",
        "description": "From the farmer's garden",
        "client": "client_c",
        "priority":2,
        "target_date":1589824565,
        "product_area":"Billing"
    },
]


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create/",methods=['POST'])
def create():
    if request.method == 'POST':
        return "create request"
    else:
        return "no data submitted"

@app.route("/get/<client_name>")
def get(client_name=''):
    client_requests = []
    for req in feature_requests:
        if req['client'] == client_name:
            client_requests.append(req)

    return jsonify(client_requests)
