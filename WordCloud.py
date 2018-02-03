from collections import Counter
from profanity import profanity

class WordCloud(object):
    def __init__(self):
        self.count = Counter()

    def handle_message(self, msg):
        lower_msg = msg.lower()
        self.count[lower_msg] += 1

    def get_count(self):
        return map(lambda k: (profanity.censor(k),self.count[k]), self.count.keys())
    
    

if __name__ == '__main__':
    wc = WordCloud()
    for msg in ('library sucks', 'fuck your mother', 'okay', 'sad', 'himank sucks', 'library sucks'):
        wc.handle_message(msg)
    print(wc.get_count())