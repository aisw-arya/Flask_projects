from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route("/home/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/<username>/')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'