from collections import Counter
from profanity import profanity
from textblob import TextBlob
import json
from lru import LRU
from random import shuffle
def analyze(msg):
    analysis = TextBlob(msg)
    if analysis.sentiment.polarity > 0:
        return 'happy'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'sad'

class WordCloud(object):
    def __init__(self):
        self.count = LRU(100)
        self.emotion = LRU(100)
        self.color = {'sad':'#f44242', 'neutral': '#4141f4', 'happy': '#41f476'}

    def handle_message(self, msg):
        lower_msg = msg.lower()
        if not (lower_msg in self.count):
            self.count[lower_msg] = 0
        self.count[lower_msg] += 1
        emo = analyze(lower_msg)
        self.emotion[lower_msg] = self.color[analyze(lower_msg)]

    def transform(self, msg):
        return {'text': profanity.censor(msg), 'size': self.count[msg], 'color': self.emotion[msg]}
    def get_count(self):
        keys = self.count.keys()
        shuffle(keys)
        return json.dumps(map(self.transform, keys))


if __name__ == '__main__':
    wc = WordCloud()
    for msg in ('library sucks', 'fuck your mother', 'okay', 'sad', 'himank sucks', 'library sucks', 'library is great'):
        wc.handle_message(msg)
    print wc.get_count()