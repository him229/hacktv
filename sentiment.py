from textblob import TextBlob
class Sentiment(object):
    def __init__(self):
        pass
    def analyze(self, msg):
        analysis = TextBlob(msg)
        if analysis.sentiment.polarity > 0:
            return 1
        elif analysis.sentiment.polarity == 0:
            return 0
        else:
            return -1