onServer = False
try:
    import keys
except ImportError:
    onServer = True

import tweepy
from StreamListener import StreamListener
from os import environ

consumer_key = environ.get('consumer_key') if onServer else keys.consumer_key
consumer_secret = environ.get('consumer_secret') if onServer else keys.consumer_secret
access_token = environ.get('access_token') if onServer else keys.access_token
access_token_secret = environ.get('access_token_secret') if onServer else keys.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

streamListener = StreamListener()
streamListener.setApi(api)
stream = tweepy.Stream(auth = api.auth, listener=streamListener)
stream.filter(track=["life"],languages=["en"]) # I dont want to fall behind
