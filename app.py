from flask import Flask, request, render_template
from bs4 import BeautifulSoup as bs
import requests
app = Flask(__name__)

@app.route('/')
def index():
    return render_template ( "index.html")

@app.route('/안녕하세요')
def hello ():
    'Hello, world!'

@app.route('/img')
def myimage():
    return render_template("myimage.html")

@app.route('/index')
def facetype():
    return render_template("index.html")

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return "GET으로 전달"
    else:
        
        return render_template("myimage.html")

if __name__ == '__main__':
    app.run(debug=True)