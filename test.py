#helloo world

import tweepy
import urllib.request, urllib.parse, urllib.error
import twurl
import json

key = '1393843058207203336-ajDwuNY9xVughPJdMoOJtLiKOopixx'
secret = "gAFLk9vSsNzHip2V6t1cFekO65MgQ10jut1gsRVg6iXBZ"

consumer_key = "Km9zRV1UtaDDvdiY8ZMSaQ2Jr"
consumer_secret = "Gfeckp0tn3X2iFWc9USvkJjaH4EU9MaoVVm8ICXIOG3T9HrXkx"

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)

api = tweepy.API(auth)
for tweet in tweepy.Cursor(api.search, q='tweepy').items(10):
    print(tweet.text)
