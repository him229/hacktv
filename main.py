from flask import Flask, jsonify, request, render_template
import json
from collections import Counter
from WordCloud import WordCloud


app = Flask(__name__)

wc = WordCloud()

@app.route('/msg', methods=['GET', 'POST'])
def get_msg():
    global wc
    msg = request.form['Body']
    wc.handle_message(wc)
    return request.form['Body']


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
