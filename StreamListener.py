from Sentence import Sentence
from utils import *
import tweepy
from Tweet import Tweet
import json

class StreamListener(tweepy.StreamListener):

    def on_connect(self):
        self.queueLength = 0

    # def on_data(self, raw_data):
    #     """Called when raw data is received from connection.
    #     Override this method if you wish to manually handle
    #     the stream data. Return False to stop stream and close connection.
    #     """
    #     data = json.loads(raw_data)
    #
    #     if 'in_reply_to_status_id' in data:
    #         status = tweepy.models.Status.parse(self.api, data)
    #         if self.on_status(status) is False:
    #             return False
    #     else:
    #         print("Unknown message type: " + str(raw_data))

    def on_limit(self, track):
        self.queueLength = track
        # print("limit: {}".format(track))

    def on_status(self, status):
        #print(self.queueLength)
        tweet = Tweet(status)
        if tweet.isAcceptable():
            sent = Sentence(tweet.cleaned)
            if isPoem(sent):
                print("\n\n")
                print(formatPoem(sent))
                print("\nAn accidental poem by @{}\n\n".format(tweet.user))
                print(tweet.text)

    def on_error(self, status_code):
        print("Status code: {}".format(status_code))
        #return False
