# Importing necessary dependencies
import os , re , sys , tweepy
from sys import *

""" Please Read! Try catch for this module in particular. 
Can't exactly remember off the top of my head why I implemented a try catch here. 
I believe it was to deal with an error relating to current python version """
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

#--------------------------------------------------------------------------
# Initializing consumeer key and secret as well as access token and secret. 
consumer_key = os.environ.get('c_k')
consumer_secret = os.environ.get('c_s')
#--------------------------------------------------------------------------
access_token = os.environ.get('a_t')
access_token_secret = os.environ.get('a_s')
#--------------------------------------------------------------------------

# Handling authentication using tweepy OAuthHandler Method
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Initializing api utilizing tweepy api method passing in auth object
api = tweepy.API(auth)

# Grabbing username from system arguments
username = str(argv[1])

# Making sure all urls grabbed are actually from twitter
substring = ["www.twitter.com" , "twitter.com"]

# Creating a list to store found urls 
finalUrl = []

# This method takes the username given through system arguments 
# and collects links from said users timeline 
def get_tweets(username): 

    # creating tweets variable containting the list of the given users timeline  
    tweets = api.user_timeline(screen_name = username , count = 20000 , include_entities = True, tweet_mode="extended") 

    # looping through the aformentioned list        
    for tweet in tweets:

            # urls variable storing a list of found urls in each tweet found on the given users timeline
            urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet.full_text)

            # looping through each url in the list of urls
            for url in urls:

                # filtering out urls that do not pertain to the twitter domain
                finalList = [url for url in urls if "twitter" not in url]
                res = urllib2.urlopen(url)
                actual_url = res.geturl()

                # for testing purposes print(actual_url)
                for x in actual_url:
                    if substring in x:
                        del x
                    else:
                        finalUrl.append(x)

# Calling get_tweets function passsing in username variable
get_tweets(username)