from Sentence import Sentence
from isPoem import isPoem
from formatPoem import formatPoem
import tweepy
from Tweet import Tweet
#override tweepy.StreamListener to add logic to on_status
class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        tweet = Tweet(status)
        if tweet.isAcceptable():
            sent = Sentence(tweet.cleaned())
            if isPoem(sent):
                print("\n\n")
                print(formatPoem(sent))
                print("\n\n")
