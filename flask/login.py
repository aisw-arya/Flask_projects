from flask import Flask,render_template,request
app = Flask(__name__)




@app.route("/", methods=['GET','POST'])
def userlogin():
    d={}
    d.update({'shalu':'one','sumi':'two','pravi':'three'})
    if request.method=='POST':
        name = request.form['n']
        password = request.form['p'] 
        for i in d:
            if name in d.keys() and password in d.values():
                return render_template('success.html',username=name)
            else:
                 return render_template('failed.html')
                
    return render_template('login.html')