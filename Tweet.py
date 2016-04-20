'''
Created on Apr 19, 2016

@author: Max Ruiz
'''

import utils
import random

class Tweet(object):
    def __init__(self, tweet_json_obj):

        self.twText = tweet_json_obj["text"]
        self.twBoundingBox = tweet_json_obj["place"]["bounding_box"]["coordinates"][0]
        self.twID = tweet_json_obj["id"]
        self.twRetweetCount = tweet_json_obj["retweet_count"]
        self.twRepliedTo = tweet_json_obj["in_reply_to_screen_name"]
        self.twScreenName = tweet_json_obj["user"]["screen_name"]
        self.twDate = tweet_json_obj["created_at"]


    def getLatitude(self, corner):
        return self.twBoundingBox[corner][1]

    def getLongitude(self, corner):
        return self.twBoundingBox[corner][0]

    def getRandPointInBoundingBox(self):
        latitude = random.uniform(self.getLatitude(0), self.getLatitude(1))
        longitude = random.uniform(self.getLongitude(0), self.getLongitude(2))
        return latitude, longitude
