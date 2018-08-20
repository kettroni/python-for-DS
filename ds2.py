import tweepy
import textblob

import os
from dotenv import load_dotenv
load_dotenv()

consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")

access_token = os.getenv("access_token")
access_secret = os.getenv("access_secret")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

searched = input()

public_tweets = api.search(searched)

for tweet in public_tweets:
    print(tweet.text)
    analysis = textblob.TextBlob(tweet.text)
    print(analysis.sentiment)
    print('')
