from . import utils
import random

class Tweet(object):
    def __init__(self, tweet_dict):

        self.tweet = tweet_dict['text']
        self.coords = tweet_dict['place']['bounding_box']['coordinates'][0]
        self.follower_count = tweet_dict['user']['followers_count']
        self.screen_name = tweet_dict['user']['screen_name']
        self.freinds = tweet_dict['user']['friends_count']
        
