import keys
import tweepy
from StreamListener import StreamListener

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API(auth)

streamListener = StreamListener()
streamListener.setApi(api)
stream = tweepy.Stream(auth = api.auth, listener=streamListener)
stream.filter(track=["life"],languages=["en"]) # I dont want to fall behind
