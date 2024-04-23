# Imports
import os
import tweepy

# Environments
from dotenv import load_dotenv
load_dotenv('.env')

# Keys
api_key: str = os.getenv('API_KEY')
api_secret: str = os.getenv('API_SECRET')
access_token: str = os.getenv('ACCESS_TOKEN')
access_secret: str = os.getenv('ACCESS_SECRET')
bearer_token: str = os.getenv('BEARER_TOKEN')

# v1.1 Endpoint Access
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# v2 Endpoint Access
client = tweepy.Client(
    bearer_token,
    api_key,
    api_secret,
    access_token,
    access_secret,
    wait_on_rate_limit=True,
)

# Error Check
try:
    api.verify_credentials()
    print("Success! Your API call worked!")
except:
    print("Oops. Failed to connect to Twitter!")

# Your Tweet Logic
new_tweet = "test. (Sent from @code w/ Python, Tweepy, and Twitter APIv2)"

# Upload image to Twitter. Replace 'filename' your image filename.
media_id = api.media_upload(filename="bigthree.png").media_id_string
print(media_id)

# Post your Tweet!
try:
    # Send Tweet with Text and media ID
    client.create_tweet(text=new_tweet, media_ids=[media_id])
    print("Tweet posted successfully!")
except:
    print("Error occurred while posting the tweet: " + str(new_tweet))