from flask import Flask, jsonify, request
import json
from collections import Counter
from WordCloud import WordCloud

app = Flask(__name__)

wc = WordCloud()

@app.route('/msg', methods=['GET', 'POST'])
def get_msg():
    global
    msg = request.form['Body']
    wc.handle_message(wc)
    return request.form['Body']

@app.route('/')
def index():
    return "It's working"

if __name__ == '__main__':
    app.run()