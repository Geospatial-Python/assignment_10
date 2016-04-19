from . import utils
from point import Point

class Tweet(object):
	def __init__(self, tweet_dic):
		self.tweet = tweet_dic['text']
		self.lat = tweet_dic['place']['bounding_box']['cordinates'][0][1]
		self.lng = tweet_dic['place']['bounding_box']['cordinates'][0][0]
		self.username = tweet_dic['user']['screen_name']
		self.source = tweet_dic['source']
		self.followers = tweet_dic['followers_count']
		self.point = Point(self.lat, self.lng)

