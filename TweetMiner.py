import os , re , sys , tweepy
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

class TweetMiner:
    def __init__(self, consumer_key = None, consumer_secret = None, access_token = None, access_token_secret = None, api = None):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.api = api

    def authenticate(self):
        # Handling authentication using tweepy OAuthHandler Method
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(auth)
        return self.api

    def getTweets(self, username): 
        self.api.user_timeline(screen_name = username, count = numberOfTweetsToCollect)
    
    def displayTweets(self):
        pass  

# Initializing consumeer key and secret as well as access token and secret. 
consumer_key = os.environ.get('c_k')
consumer_secret = os.environ.get('c_s')

access_token = os.environ.get('a_t')
access_token_secret = os.environ.get('a_s')

tweetMiner = TweetMiner(consumer_key, consumer_secret, access_token, access_token_secret)