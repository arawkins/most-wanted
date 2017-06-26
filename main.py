import os
from datetime import date
from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import asc
from wtforms import Form, DateField, StringField, IntegerField, validators

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
feature_requests = []

class FeatureRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    description = db.Column(db.Text())
    client = db.Column(db.String(24))
    priority = db.Column(db.Integer())
    target_date = db.Column(db.Date())
    product_area = db.Column(db.String(24))

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<Title %r>' % (self.title)

class FeatureRequestForm(Form):
    title = StringField('Title',[validators.InputRequired()])
    description = StringField('Description',[validators.InputRequired()])
    client = StringField('Client',[validators.InputRequired()])
    priority = IntegerField('Priority',[validators.InputRequired(), validators.NumberRange(min=1)])
    target_date = DateField('Target Date', [validators.InputRequired()], format='%m/%d/%Y')
    product_area = StringField('Product Area',[validators.InputRequired()])


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create/", methods=['POST'])
def create():
    if request.method == 'POST':
        form = FeatureRequestForm(request.form)
        if request.method == 'POST' and form.validate():

            new_request = FeatureRequest(form.title.data)
            new_request.description = form.description.data
            new_request.client = form.client.data
            new_request.priority = form.priority.data
            new_request.product_area = form.product_area.data
            new_request.target_date = form.target_date.data

            current_client_requests = FeatureRequest.query.filter_by(client=new_request.client).all()

            if new_request.priority <= 0:
                new_request.priority = 1

            if new_request.priority >= len(current_client_requests):
                new_request.priority = len(current_client_requests) + 1

            for current_req in current_client_requests:
                if current_req.priority >= new_request.priority:
                    current_req.priority += 1

            db.session.add(new_request)
            db.session.commit()

            return "success"
        else:
            print(form.errors)
            return "invalid form"
    else:
        return "no data provided"

@app.route("/get/<client_name>")
def get(client_name=''):
    client_requests = FeatureRequest.query.filter_by(client=client_name).order_by(asc(FeatureRequest.priority)).all()
    to_return = []
    for req in client_requests:
        new_request = {
            'title': req.title,
            'description': req.description,
            'client': req.client,
            'priority': req.priority,
            'target_date': req.target_date.strftime('%m/%d/%Y'),
            'product_area': req.product_area
        }
        to_return.append(new_request)
    return jsonify(to_return)
