import spacy as spacy
import tweepy
import datetime

from concorrenti import concGF
from functions_utils import *
from Tweet import *
from Config import *

# Login Twitter
config = DefaultConfig()
auth = tweepy.OAuthHandler(config.CONS_KEY, config.CONS_SECR)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
# client = config.BEARER
api = tweepy.API(auth)

"""     ------------------STAMPA CONCORRENTI-------------------------
for i in range(len(concGF)):
    print("-", concGF[i].getName(), concGF[i].getCognome())
"""

# variabili
tweets = []
tweetsTranslated = []
nConc = len(concGF) - 1

# Inserimento hashtag
hashtags = "#GFVip AND ("
for t in range(nConc):
    if concGF[t].getName() == "Luca" or concGF[t].getName() == "Edoardo":
        hashtags += "#" + concGF[t].getCognome()
    else:
        hashtags += "#" + concGF[t].getName()
    if t < nConc:
        hashtags += " OR "
    else:
        hashtags += " ) "

print("------------Operazioni Preliminari------------")
print("Concorrenti GFVip: \n")
for t in range(nConc):
    print("->", concGF[t].getName(), concGF[t].getCognome())
print("Hashtags: \n" + hashtags + "\n")

research = hashtags + " -filter:retweets"

print("-----------Start tweet capturing------------\n")
date_tweepy = datetime.date.today()
print("Today: ", date_tweepy)
date_to_match_in_csv = date_tweepy - datetime.timedelta(days=1)
print("Yesterday: ", date_to_match_in_csv)
"""
tmp = tweepy.Cursor(api.search_tweets, q=research, lang="it",
                    until=date_tweepy, result_type="mixed",
                    tweet_mode="extended").items(100)
"""
tmp = api.search_tweets(q=research, count="100")
print(len(tmp))
i=0
for tweet in tweepy.Cursor(api.search_tweets, q=research, lang="it",
                           tweet_mode="extended", count="100").items(500):
    print(tweet.full_text)
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

    """tt = {
        "Id": tweet.id,
        "Screen_name": tweet.user.name,
        "Created_at": tweet.created_at,
        "Retweet": str(rt_count),
        "Text": tweet.full_text,
        "Hashtags": hast,
        "Sentiment": 0,
        "Compound": 0
    }"""

    tt = Tweet(tweet.id, tweet.user.name, tweet.created_at, str(rt_count), tweet.full_text, hast, 0, 0)
    print_tweet(tt)
    if str(tt.getCreated_at()).find(str(date_to_match_in_csv)) != -1:
        tweets.append(tt)  # tweet italiani
        tweetsTranslated.append(translatorTweet(tt))  # tweet inglesi

for t in tweets:
    calculate_and_set_compound_score_to_tweet(t)
    calculate_and_set_sentiment_score_to_tweet(t)
    print_tweet(t)
    print_emotion_score(t)
    print()

print("Analisi più dettagliata dei Tweet")
nlp = spacy.load('it_core_news_sm')

print(concGF)
for tweet in tweets:
    concGF_clone = copy.deepcopy(concGF)
    doc = nlp(tweet.getText())
    print("TWEET: ")
    print("Testo tweet: " + tweet.getText())
    print("Sentiment: " + str(tweet.getSentiment()))

    ents = []
    for entity in doc.ents:
        for concorrente in concGF:
            # non mettiamo il break, a fine 'if', poichè all'interno di un soggetto potrebbero esserci più concorrenti e quindi vogliamo
            # prima estrapolare tutti i concorrenti dal soggetto e poi andare avanti col prossimo soggetto
            if ((concorrente.getName().upper() in entity.text.upper()) and (concorrente in concGF_clone)):
                ents.append(concorrente.getName())
                print("text: " + entity.text, ", concorrente_name: " + concorrente.getName())
                concorrente.addScore(tweet.getSentiment())
                concGF_clone.pop(concGF_clone.index(concorrente))
                # print("FINE " + "text: " + entity.text, "type/label: " + entity.label_)

    tweet.setEnts(ents)
    print("Ents: " + str(tweet.getEnts()))
    print()

print("LISTA CON PUNTEGGI")
for c in concGF:
    print("Name: " + c.getName())
    print("score_negativo: " + str(c.getScoreNegativo()))
    print("score_tendente_negativo: " + str(c.getScoreTendenteNegativo()))
    print("score_neutro: " + str(c.getScoreNeutro()))
    print("score_tendente_positivo: " + str(c.getScoreTendentePositivo()))
    print("score_positivo: " + str(c.getScorePositivo()))
    print()

print("Done analysis!")

