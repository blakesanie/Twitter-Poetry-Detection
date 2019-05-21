from Sentence import Sentence
from utils import *
import tweepy
from Tweet import Tweet
from threading import Timer

class StreamListener(tweepy.StreamListener):

    # def on_connect(self):
    # def on_limit(self, track):

    def setApi(self, api):
        self.api = api
        self.canTweet = True
        #print("api set")

    def on_status(self, status):
        if self.canTweet:
            tweet = Tweet(status)
            if tweet.isAcceptable():
                sent = Sentence(tweet.cleaned)
                if isPoem(sent):
                    formatted = formatPoem(sent)
                    #
                    self.api.update_status("{}\nA life poem by @{}".format(formatted, tweet.user), tweet.id)
                    # self.canTweet = False
                    # timer = Timer(300.0, self.resetCanTweet)
                    # timer.start()

    def on_error(self, status_code):
        print("Status code: {}".format(status_code))

    def resetCanTweet(self):
        self.canTweet = True
