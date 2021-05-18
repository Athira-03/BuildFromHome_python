import tweepy
import hidden

# Authenticate to Twitter
auth = tweepy.OAuthHandler("consumer_key", 
    "consumer_secret")
auth.set_access_token("token_key", 
    "token_secret")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")