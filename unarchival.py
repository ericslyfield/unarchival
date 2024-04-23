import os
import tweepy

from dotenv import load_dotenv

load_dotenv('.env')

api_key: str = os.getenv('API_KEY')
api_secret: str = os.getenv('API_SECRET')
access_token: str = os.getenv('ACCESS_TOKEN')
access_secret: str = os.getenv('ACCESS_SECRET')

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Success! Your API call worked!")
except:
    print("Oops. Something went wrong!")