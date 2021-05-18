import tweepy
import hidden

# Authenticate to Twitter
auth = tweepy.OAuthHandler("consumer_key", "consumer_secret")
auth.set_access_token("token_key", "token_secret")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)


timeline = api.home_timeline()
for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}")