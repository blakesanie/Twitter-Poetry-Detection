import keys
import tweepy
from StreamListener import StreamListener

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API(auth)

streamListener = StreamListener()
stream = tweepy.Stream(auth = api.auth, listener=streamListener)
stream.filter(track=["i"])







# sent = Sentence("Tell me not, in mournful numbers, Life is but an empty dream!— For the soul is dead that slumbers, And things are not what they seem.")
#
# if isPoem(sent):
#     print(formatPoem(sent))
# else:
#     print("no poem")
