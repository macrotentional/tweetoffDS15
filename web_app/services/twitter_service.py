import os
from dotenv import load_dotenv
from tweepy import OAuthHandler, API

load_dotenv()

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# could use a function here to return our api client
# could use a class
auth = OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
print("API AUTH:", auth)

api = API(auth)
print("API CLIENT:", api)

if __name__ == "__main__":

    user = api.get_user("elonmusk")
    print("TWITTER USER:", type(user)) #> <class 'tweepy.models.User'>
    print(user.id)
    print(user.screen_name)
    print(user.name)
    # print(user.followers_count)

    tweets = api.user_timeline("elonmusk", tweet_mode="extended")
    print("TWEETS", type(tweets)) #> <class 'tweepy.models.ResultSet'>
    print(type(tweets[0])) #> <class 'tweepy.models.Status'>

    tweet = tweets[0]
    print(tweet.id)
    print(tweet.full_text)

    #breakpoint()

    #public_tweets = api.home_timeline()
    #
    #for tweet in public_tweets:
    #    print(type(tweet)) #> <class 'tweepy.models.Status'>
    #    #print(dir(tweet))
    #    print(tweet.text)
    #    print("-------------")