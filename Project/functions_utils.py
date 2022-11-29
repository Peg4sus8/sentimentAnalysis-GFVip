import copy
import re
from googletrans import Translator
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

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

# Tweet
def print_tweet(tweet):
    print("\033[1m" + "Id: " + "\033[0m" + str(tweet.getId()))
    print("\033[1m" + "Screen_name: " + "\033[0m" + tweet.getScreen_name())
    print("\033[1m" + "Created_at: " + "\033[0m" + str(tweet.getCreated_at()))
    print("\033[1m" + "Retweet: " + "\033[0m" + tweet.getRetweet())
    print("\033[1m" + "Text: " + "\033[0m" + tweet.getText())
    print("\033[1m" + "Hashtags: " + "\033[0m" + tweet.getHashtags())
    print("\033[1m" + "Sentiment: " + "\033[0m" + str(tweet.getSentiment()))
    print("\033[1m" + "Compound: " + "\033[0m" + str(tweet.getCompound()))


def calculate_and_set_compound_score_to_tweet(tweet):
    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(tweet.getText())
    compound = sentiment("compound")
    tweet.setCompound(compound)

def calculate_and_set_sentiment_score_to_tweet(tweet):
    sentimentAnalysis = Sentiment()
    tweet.setSentiment(sentimentAnalysis[0])


def print_emotion_score(tweet):
    sentimentAnalysis = Sentiment(tweet.getCompound())
    print("\033[1m" + "Risultato: " + "\033[0m" + sentimentAnalysis[1])

def Sentiment(compound):
    emotion = ""
    if (compound <= -0.5501 and compound >= -1):
        sentimentAnalysis = 1
        emotion = "Negativo"
    if (compound <= -0.2001 and compound >= -0.5500):
        sentimentAnalysis = 2
        emotion = "Tendente negativo"
    if (compound >= -0.2000 and compound <= 0.2000):
        sentimentAnalysis = 3
        emotion = "Neutro"
    if (compound >= 0.2001 and compound <= 0.5500):
        sentimentAnalysis = 4
        emotion = "Tendente positivo"
    if (compound >= 0.5501 and compound <= 1):
        sentimentAnalysis = 5
        emotion = "Positivo"

    return sentimentAnalysis, emotion
