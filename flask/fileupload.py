from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/', methods = ['GET' ,'POST'])
def file_upload():
    if request.method == 'POST':
        f=request.files['f']
        f.save('/home/hp/flask/upload')
        return 'success'
    return render_template('upload.html')