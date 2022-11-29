import tweepy
import datetime

from concorrenti import concGF
from functions_utils import *
from Tweet import Tweet
from Config import *

#Login Twitter
config = DefaultConfig()
auth = tweepy.OAuthHandler(config.CONS_KEY, config.CONS_SECR)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
client = config.BEARER
api = tweepy.API(auth)

"""     ------------------STAMPA CONCORRENTI-------------------------
for i in range(len(concGF)):
    print("-", concGF[i].getName(), concGF[i].getCognome())
"""

#variabili
tweets = []
tweetsTranslated = []
nConc = len(concGF) - 1

#Inserimento hashtag
hashtags = "#GFVip AND ( "
for i in range(nConc):
    if concGF[i].getName() == "Luca" or concGF[i].getName() == "Edoardo":
        hashtags += "#" + concGF[i].getCognome()
    else:
        hashtags += "#" + concGF[i].getName()
    if i < nConc:
        hashtags += " OR "
    else:
        hashtags += " ) "

print("------------Operazioni Preliminari------------")
print("Concorrenti GFVip: \n")
for i in range(nConc):
    print("->", concGF[i].getName(), concGF[i].getCognome())
print("Hashtags: \n" + hashtags + "\n")

research = hashtags + " -filter:retweets"

print("-----------Start tweet capturing------------\n")
date_tweepy = datetime.date.today()
print("", date_tweepy)
date_to_match_in_csv = date_tweepy - datetime.timedelta(days=1)
print("", date_to_match_in_csv)
for tweet in tweepy.Cursor(api.search_tweets, q=research, lang="it",
                           until=date_tweepy, result_type="mixed",
                           tweet_mode="extended").items(100):
    rt_count = tweet.retweet_count
    p2 = ["", tweet.full_text]
    hast = ""
    a = tweet.full_text.count("#")
    if a >= 0:
        p1 = p2[1].split("#", 1)
        try:
            if p1[1].find(" ") < 0:
                hast += "#" + p1[1]
                hast = hast.replace("\n", "")
                break
            else:
                p2 = p1[1].split(" ", 1)
                hast += "#" + p2[0]
                hast = hast.replace("\n", "")
        except IndexError:
            hast += "#" + p1[0]

    tweet.full_text = cleanTweet(tweet.full_text)
    hast = cleanHashtags(hast)

    tt = {
        "Id": tweet.id,
        "Screen_name": tweet.user.name,
        "Created_at": tweet.created_at,
        "Retweet": str(rt_count),
        "Text": tweet.full_text,
        "Hashtags": hast,
        "Sentiment": 0,
        "Compound": 0
    }
    tt = Tweet(tweet.id, tweet.user.name, tweet.created_at, str(rt_count), tweet.full_text, hast, 0, 0)
    if str(tt.Tweet.getCreated_at()).find(date_to_match_in_csv) != -1:
        tweets.append(tt)   #tweet italiani
        tweetsTranslated.append(translatorTweet(tt))    #tweet inglesi

