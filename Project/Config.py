import os

class DefaultConfig:
    #Twitter keys
    API_KEY = os.environ.get("ApiKey", "mtI3aZCC2TutQeg1aOdG4USgG")
    API_SECR = os.environ.get("ApiSecret", "bGMZTyzRarHHkFxViPNmwYq2fEp5DFnkdnuPnf1jSot7BctYH2")
    ACCESS_TOKEN = os.environ.get("AccessToken", "720553502-YoYchcNujXC0KcGlfEohRLCw7pOEnyqaE10bsrKM")
    ACCESS_TOKEN_SECRET = os.environ.get("AccessTokenSecret", "y54NfOfAIMnCaFeCHO2Md2G8m8G3b91KTjPx5yVAlQWkD")
    BEARER = os.environ.get("BearerToken", "AAAAAAAAAAAAAAAAAAAAACe8jgEAAAAAWPlIcX8SOX6JABjADZY6eXoHrkk%3DuUJGfr2ilHXN4LHjsSwJbJYuOEBjb3HdDm2YNA0B22T9Vq3QrM")
