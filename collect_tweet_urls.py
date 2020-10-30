import os , re , sys , tweepy
from sys import *

try:
                import urllib.request as urllib2
except ImportError:
                import urllib2

consumer_key = os.environ.get('c_k')
consumer_secret = os.environ.get('c_s')

access_token = os.environ.get('a_t')
access_token_secret = os.environ.get('a_s')


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

username = str(argv[1])
substring = ["www.twitter.com" , "twitter.com"]
finalUrl = []


def get_tweets(username): 
                
                tweets = api.user_timeline(screen_name = username , count = 20000 , include_entities = True, tweet_mode="extended") 

                
                for tweet in tweets:

                        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet.full_text)

                        for url in urls:

                            finalList = [url for url in urls if "twitter" not in url]
                            
                            res = urllib2.urlopen(url)
                            actual_url = res.geturl()
                            # for testing purposes print(actual_url)

                            for x in actual_url:
                                if substring in x:
                                    del x
                                else:
                                    finalUrl.append(x)
                               
get_tweets(str(sys.argv[1]))