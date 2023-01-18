import os

class DefaultConfig:
    #Twitter keys
    API_KEY = os.environ.get("ApiKey", "")
    API_SECR = os.environ.get("ApiSecret", "")
    ACCESS_TOKEN = os.environ.get("AccessToken", "720553502-")
    ACCESS_TOKEN_SECRET = os.environ.get("AccessTokenSecret", "")
    BEARER = os.environ.get("BearerToken", "")
