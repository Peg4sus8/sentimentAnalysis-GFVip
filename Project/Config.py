import os

class DefaultConfig:
    #Twitter keys
    CONS_KEY = os.environ.get("ConsumerKey", "")
    CONS_SECR = os.environ.get("ConsumerSecret", "")
    ACCESS_TOKEN = os.environ.get("AccessToken", "")
    ACCESS_TOKEN_SECRET = os.environ.get("AccessTokenSecret", "")
