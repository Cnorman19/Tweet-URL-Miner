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

    def getTweets(self, username, numberOfTweetsToCollect): 
        tweets = self.api.user_timeline(screen_name = username, count = numberOfTweetsToCollect)
        
        for tweet in tweets: # Time complexity O(N)
            print(tweet)
    
    def displayTweets(self):
        pass  

# Initializing consumeer key and secret as well as access token and secret. 
consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')

access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_SECRET')

tweetMiner = TweetMiner(consumer_key, consumer_secret, access_token, access_token_secret)