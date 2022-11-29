import copy
import re
from googletrans import Translator

def cleanTweet(string):
    string = string.strip()     #Rimuovo spazi bianchi
    string = string.replace('#', ' ')
    string = string.replace('\n', '')
    string = re.sub("(\@(\w)*: )|(\@(\w)*)*", '', string)
    string = re.sub('http://\S+|https://\S+', '', string)
    return string

def cleanHashtags(string):
    string = string.replace('\n', '')
    string = re.sub('(\@(\w)*: )|(\@(\w)*)*', '', string)
    string = re.sub('http://\S+|https://\S+', '', string)
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"
                               u"\U0001F300-\U0001F5FF"
                               u"\U0001F680-\U0001F6FF"
                               u"\U0001F1E0-\U0001F1FF"
                               u"\U00002500-\U00002BEF"
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    string = emoji_pattern.sub(r'', string)
    return string

def translatorTweet(string):
    tweet = ""
    tweet = copy.deepcopy(string)
    trans = Translator()
    tweet.setText((trans.translate(tweet.getText(), src="it", dest="en")).text)
    return tweet



