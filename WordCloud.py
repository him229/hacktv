from collections import Counter
from profanity import profanity
from textblob import TextBlob
import json

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
        self.count = Counter()
        self.emotion = {}
        self.color = {'happy':'#f44242', 'sad': '#4141f4', 'neutral': '#41f476'}

    def handle_message(self, msg):
        lower_msg = msg.lower()
        self.count[lower_msg] += 1
        emo = analyze(lower_msg)
        self.emotion[lower_msg] = self.color[analyze(lower_msg)]

    def transform(self, msg):
        return {'text': profanity.censor(msg), 'size': self.count[msg], 'color': self.emotion[msg]}
    def get_count(self):
        return json.dumps(map(self.transform, self.count.keys()))


if __name__ == '__main__':
    wc = WordCloud()
    for msg in ('library sucks', 'fuck your mother', 'okay', 'sad', 'himank sucks', 'library sucks', 'library is great'):
        wc.handle_message(msg)
    print wc.get_count()