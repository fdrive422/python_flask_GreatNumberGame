from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)

app.secret_key = "b'^\xf3\xe05L\x82\xa0\xa58\x8cH\xb8/\x14\xd5-\x95\xbb\xfbc"

@app.route('/')
def index():
    if "num" not in session:
        session['num'] = random.randint(1,100)
    return render_template("index.html")

@app.route('/guess',methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)