from flask import Flask,render_template,request
app = Flask(__name__)


@app.route("/", methods=['GET'])
def square_num():
    if request.method == 'GET':
        if request.args.get('num') == None :
            return render_template('squarenum.html')
        elif request.args.get('num') == '':
            return "<html><body> <h1>Invalid number</h1></body></html>"
        else:
            number =  request.args.get('num')
            sq = int(number) * int(number)
            return render_template('answer.html',squarenum=sq, num=number)