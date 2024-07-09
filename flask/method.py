from flask import Flask
from markupsafe import escape
app = Flask(__name__)
from flask import request

@app.route('/user/', methods=['GET', 'POST'])
def show_user_profile():
    if request.method == 'GET':
        return "Listing all users"
    elif request.method == 'POST':
        return "Createing a new user"


@app.route('/log/<int:user_id>', methods=['GET', 'POST','PATCH'])
def haii(user_id):
    if request.method == 'GET':
        return f"listing all the users {user_id}"
    elif  request.method == "POST" :
        return f"creating new user {user_id}"
    elif request.method == 'PATCH' :
        return f"updates {user_id}"
