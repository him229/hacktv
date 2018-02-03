from flask import Flask, jsonify, request, render_template
import json


app = Flask(__name__)


@app.route('/msg', methods=['GET', 'POST'])
def get_msg():
    msg = request.form['Body']
    print(msg)
    return request.form['Body']


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
