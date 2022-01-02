from flask import Flask, render_template 
from flask import request, url_for, redirect

import pymysql, json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/timelinr')
def timelinr():
    return render_template('nam.html')

@app.route('/graph/<graph_num>')
def graph(graph_num):
    return render_template('graph/'+graph_num+'.html')

@app.route('/contents/<contents>')
def contents(contents):
    return render_template('contents/'+contents+'.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)