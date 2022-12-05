import tweepy
import datetime

from concorrenti import concGF
from functions_utils import *
from Tweet import *
from Config import *

# --------- Login --------
configuration = DefaultConfig()
auth = tweepy.OAuthHandler(configuration.API_KEY, configuration.API_SECR)
auth.set_access_token(configuration.ACCESS_TOKEN, configuration.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# -------- Variabili --------
nConc = len(concGF)
query = "#GFVip AND ("

#date_tweepy = datetime.date.today()
#date_to_match_in_csv = date_tweepy - datetime.timedelta(days=1)
date_tweepy = "2022-12-04"
date_to_match_in_csv = "2022-12-03"

tweets = []
tweetsTranslated = []

# -------- Creazione Query ---------
for i in range(nConc):
    for h in range(len(concGF[i].getHashtags())):
        query += concGF[i].hashtags[h]
        if i < (nConc - 1):
            query += " OR "
        else:
            query += ")"
query += "-filter:retweet"
print(query)

# ------- tweet capturing------
for tweet in tweepy.Cursor(api.search_tweets, q=query, lang="it", until=date_tweepy, tweet_mode="extended", count=100).items(5000):
    if 'retweeted_status' in dir(tweet):
        text = tweet.retweeted_status.full_text
    else:
        text = tweet.full_text

    p2 = ["", text]
    hast = ""
    a = text.count("#")
    if a >= 0:
        for c in range(a):
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
        text = cleanTweet(text)
        hast = cleanHashtags(hast)
        provv = Tweet(tweet.id, tweet.user.screen_name, tweet.created_at, str(tweet.retweet_count), text, hast, 0, 0)

    if str(provv.getCreated_at()).find(str(date_to_match_in_csv)) != -1:
        tweets.append(provv)  # tweet italiani
        #tweetsTranslated.append(translatorTweet(provv))  # tweet inglesi

print(len(tweets))

for i in range(len(tweets)):
    calculate_and_set_compound_score_to_tweet(tweets[i])
    calculate_and_set_sentiment_score_to_tweet(tweets[i])
    #print_tweet(tweets[i])
    #print_emotion_score(tweets[i])




