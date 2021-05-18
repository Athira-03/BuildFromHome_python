
#python libraries
import datetime
import csv
import tweepy

key = '139.............................moylzIju65f'
secret = "LB0nB.................................GqhMyo"

consumer_key = "rQM6ra......................ce17"
consumer_secret = "tLEmpaA...........................wBfnq"

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

print("Hey there /n Enter the following Details : ")
print("User name: ")
name = input()
print("from date ..................enter in yy-mm-dd  format : ")
from_d = input()
print("to until date ..................enter in yy-mm-dd  format : ")
until_d = input()
for tweet in tweepy.Cursor(api.search,
                           q=name,
                           since=from_d,
                           until=until_d,
                           lang="en").items():
    print(tweet.created_at, tweet.text)
