from flask import url_for
from flask import Flask
from markupsafe import escape
app = Flask(__name__)
@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
