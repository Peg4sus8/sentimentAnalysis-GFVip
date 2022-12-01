class Tweet:
    # Metodo costruttore
    def __init__(self, tid, screen_name, created_at, retweet, text,
                 hashtags, sentiment, compound):
        self.tweetId = tid
        self.screen_name = screen_name
        self.created_at = created_at
        self.retweet = retweet
        self.text = text
        self.hashtags = hashtags
        self.sentiment = sentiment
        self.compound = compound
        self.ents = []

    # Getter
    def getId(self):
        return self.tweetId

    def getScreen_name(self):
        return self.screen_name

    def getCreated_at(self):
        return self.created_at

    def getRetweet(self):
        return self.retweet

    def getText(self):
        return self.text

    def getHashtags(self):
        return self.hashtags

    def getSentiment(self):
        return self.sentiment

    def getCompound(self):
        return self.compound

    def getEnts(self):
        return self.ents

    # Setter
    def setId(self, id):
        self.tweetId = id

    def setScreenName(self, screen_name):
        self.screen_name = screen_name

    def setCreatedAt(self, created_at):
        self.created_at = created_at

    def setRetweet(self, retweet):
        self.retweet = retweet

    def setText(self, testo):
        self.text = testo

    def setHashtags(self, hashtags):
        self.hashtags = hashtags

    def setSentiment(self, sentiment):
        self.sentiment = sentiment

    def setCompound(self, compound):
        self.compound = compound

    def setEnts(self, ents):
        self.ents = ents

    # toString
    def __str__(self):
        return "\033[1m" + "Id: " + "\033[0m" + str(self.tweetId) + \
               "\033[1m" + "Screen_name: " + "033[0m" + self.screen_name + \
               "\033[1m" + "Created_at: " + "\033[0m" + str(self.created_at) + \
               "\033[1m" + "Retweet: " + "\033[0m" + self.retweet + \
               "\033[1m" + "Text: " + "\033[0m" + self.text + \
               "\033[1m" + "Hashtags: " + "\033[0m" + self.hashtags + \
               "\033[1m" + "Sentiment: " + "\033[0m" + str(self.sentiment) + \
               "\033[1m" + "Compound: " + "\033[0m" + str(self.compound) + \
               "\033[1m" + "Ents: " + "\033[0m" + str(self.ents)
