import os
import tweepy

from dotenv import load_dotenv

load_dotenv('.env')

test: str = os.getenv('ABC')
app_name: str = os.getenv('APP_NAME')

print(test)
print(app_name)

#auth = tweepy.OAuthHandler("API_KEY", "API_SECRET_KEY")
#auth.set_acess_token("ACCESS_TOKEN", "SECRET_ACESS_TOKEN")
