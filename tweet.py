import utils
import random


class Tweet(object):
    def __init__(self, tweet_dict):
        self.tweet = tweet_dict['text']
        self.bounds = tweet_dict['place']['bounding_box']['coordinates'][0]
        self.date = tweet_dict['created_at']
        self.username = tweet_dict['user']['name']
        self.user_description = tweet_dict['user']['description']
        self.tweet_id = tweet_dict['id']
        self.user_followers_count = tweet_dict['user']['followers_count']
        
        
    def get_lat_n(self, n):
        return self.bounds[n][1]
    
    def get_lon_n(self, n):
        return self.bounds[n][0]
    
    def gen_point_in_bounds(self):
        lat = random.uniform(self.get_lat_n(0), self.get_lat_n(1))
        lon = random.uniform(self.get_lon_n(0), self.get_lon_n(2))
        return lat, lon
    