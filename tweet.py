import tweepy
from keys import api_secret, api_key, bearer_token, access_token, access_token_secret

# Using the keys from my hidden keys.py file post a tweet to the Faux News Account...
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Post a tweet to @thefauxnewsbot Twitter page.
def post_tweet(parody, url):
    client.create_tweet(text=parody + " " + url)
