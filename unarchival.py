# Imports
import os
import tweepy

# Environments
from dotenv import load_dotenv
load_dotenv('.env')

# Keys
api_key: str = os.getenv('API_KEY')
api_secret: str = os.getenv('API_SECRET')
consumer_key: str = os.getenv('API_KEY')
consumer_secret: str = os.getenv('API_SECRET')
access_token: str = os.getenv('ACCESS_TOKEN')
access_secret: str = os.getenv('ACCESS_SECRET')
access_token_secret: str = os.getenv('ACCESS_SECRET')
bearer_token: str = os.getenv('BEARER_TOKEN')

# v1.1 Endpoint Access
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# v2 Endpoint Access
client = tweepy.Client(
    bearer_token,
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret,
    wait_on_rate_limit=True,
)

#client = tweepy.Client(bearer_token)

# Error Check
try:
    api.verify_credentials()
    print("Success! Your API call worked!")
except:
    print("Oops. Failed to connect to Twitter!")

# A link to your new Tweet
new_tweet = "A computer can never be held accountable, therefore a computer must never make a management decision. (Sent from @code w/ Python, Tweepy, and Twitter APIv2)"

# A link to your new Tweet
#print(f"https://twitter.com/user/status/{new_tweet.data['id']}")

# Try posting the tweet
try:
    # Send Tweet with Text and media ID
    client.create_tweet(text=new_tweet)
    print("Tweet posted successfully!")
except:
    print("Error occurred while posting the tweet: " + str(new_tweet))