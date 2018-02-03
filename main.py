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
    print msg
    wc.handle_message(msg)
    return msg

@app.route('/wordcloud', methods=['GET'])
def get_wordcloud():
    global wc
    return wc.get_count()


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
