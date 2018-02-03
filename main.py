from flask import Flask, jsonify, request, render_template
import json
from wordcloud import WordCloud
from time import sleep


app = Flask(__name__)


def show_wordcloud(text):
    wordcloud = WordCloud(background_color="white").generate_from_text(text)
    image = wordcloud.to_image()
    image.show()
    return image


# junk = "ready to drink meail with chai soulent cafe chai natural and artificial flavors complete meal 20 percent daily nutrition 20 grams protein caffeine plus one dash theanine 14 fluid ounces"
# show_wordcloud(junk)
# sleep(2)
# junk += "cat cat cat cat cat cat cat cat cat cat cat cat"
# show_wordcloud(junk)


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
