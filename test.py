#python libraries
import datetime
import csv
import tweepy

key = '13938430......................................84........................moylzIju65f'
secret = "LB0nB.....................................................Myo"

consumer_key = "rQM6ra............................................hmce17"
consumer_secret = "tLEmpa............................................cwBfnq"

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

# Open/create a file to append data to
csvFile = open('My Twitter Tweets.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)

print("Hey there /n Enter the following Details : ")
print("User name: ")
name = input()
print("from date ..................enter in yyyy-mm-dd  format : ")
from_d = input()
print("to until date ..................enter in yyyy-mm-dd  format : ")
until_d = input()
for tweet in tweepy.Cursor(api.search,
                           q=name,
                           since=from_d,
                           until=until_d,
                           lang="en").items():

    # Write a row to the CSV file. I use encode UTF-8
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    print
    tweet.created_at, tweet.text
csvFile.close()
