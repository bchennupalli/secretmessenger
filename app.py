from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import random
import string

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    pin = db.Column(db.String(8), unique=True, nullable=False)

    @staticmethod
    def generate_pin():
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

# Instead of using @app.before_first_request
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create', methods=['GET', 'POST'])
def create_message():
    message = None
    if request.method == 'POST':
        message_content = request.form['message']
        message_pin = Message.generate_pin()
        new_message = Message(content=message_content, pin=message_pin)
        db.session.add(new_message)
        db.session.commit()
        message = new_message
    return render_template('create.html', message=message)

@app.route('/view', methods=['GET', 'POST'])
def view_message():
    message = None
    if request.method == 'POST':
        pin = request.form['pin']
        message = Message.query.filter_by(pin=pin).first()
    return render_template('view.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
