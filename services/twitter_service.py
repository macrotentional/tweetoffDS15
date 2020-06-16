import tweepy
import os
from dotenv import load_dotenv

auth = tweepy

load_dotenv()

TWITTER_API_KEY = os.getenv("gEZuPPXNPcSMA9mbL8m2lF0Lh")
TWITTER_API_SECRET = os.getenv("VLsKcV1xULN2ob9S3A4iDXXqbpwRAGPUJ1lUiPrrNLVjz3HLir")
TWITTER_ACCESS_TOKEN = os.getenv("52950762-jkslImkDKKK23oPX7xwkSOCvVvkOj1RJJmjXJXB3L")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("5DXG3cBJgmgx20YyK4YvZkktQBatAdSa87IOAor8jIauc")

def twitter_api():
    auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    print("AUTH", auth)
    api = tweepy.API(auth)
    print("API", api)
    #print(dir(api))
    return api

if __name__ == "__main__":

    api = twitter_api()
    user = api.get_user("elonmusk")
    print("USER", user)
    print(user.screen_name)
    print(user.name)
    print(user.followers_count)

    #breakpoint()

    #public_tweets = api.home_timeline()
    #
    #for tweet in public_tweets:
    #    print(type(tweet)) #> <class 'tweepy.models.Status'>
    #    #print(dir(tweet))
    #    print(tweet.text)
    #    print("-------------")