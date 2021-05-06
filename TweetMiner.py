import os , re , sys , tweepy
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

class TweetMiner:
    def __init__(self, consumer_key = None, consumer_secret = None, access_token = None, access_token_secret = None):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret

    def authenticate(self):
        # Handling authentication using tweepy OAuthHandler Method
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        return self.api

    def get_tweets(self, username):  
        pass

# Initializing consumeer key and secret as well as access token and secret. 
consumer_key = os.environ.get('c_k')
consumer_secret = os.environ.get('c_s')

access_token = os.environ.get('a_t')
access_token_secret = os.environ.get('a_s')

tweetMiner = TweetMiner(consumer_key, consumer_secret, access_token, access_token_secret)