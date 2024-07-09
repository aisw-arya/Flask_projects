from flask import *

app = Flask(__name__)

# @app.route('/',methods=['POST', 'GET'])
# def index():
#     if request.method == 'POST':
#         username = request.form['username']

#         resp = make_response(render_template('success.html',data=username))
#         resp.set_cookie('username',username)
#         return resp



#     return render_template('index.html')
#     # username= request.cookies.get('username')

@app.route('/', methods= ['GET','POST'])
def register():
    if request.method == 'POST':
        uname=request.form['username']
        pswd = request.form['password']
        resp = make_response(render_template('register.html'))
        resp.set_cookie('username',uname)
        resp.set_cookie('password',pswd)
    return render_template('register.html')

@app.route('/show')
def show():
    cu=request.cookies.get('username')
    cp=request.cookies.get('password')
    return f'{cu},{cp}'
