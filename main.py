from flask import Flask, jsonify, request, render_template, redirect, url_for
import json
from collections import Counter
from WordCloud import WordCloud


app = Flask(__name__)

wc = WordCloud()

@app.route('/msg', methods=['GET', 'POST'])
def get_msg():
    global wc
    msg = request.form['Body']
    print msg
    wc.handle_message(msg)
    return msg

@app.route('/wordcloud', methods=['GET'])
def get_wordcloud():
    global wc
    return render_template("index.html", words_json=wc.get_count())

@app.route('/')
def index():
    context = [{"text": "soylent", "size": 50}, {"text": "himank", "size": 20}, {"text": "sorry", "size": 40}, {"text": "beautiful", "size": 80}]
    context = json.dumps(context)
    print context
    return render_template("index.html", words_json=context)


if __name__ == '__main__':
    app.run(debug=True)
