#Create a new Tweet class or extend the existing Point class to store:
import src.point
class Tweet(object):
    def __init__(self,tweet_dictionary):
        #want pass in the tweet dictionary so that you can actually store it
        #the tweet text:
        self.tweetText = tweet_dictionary['text'] # get the "text field"
        #if tweet_dictionary['geo'] is None: #(long,lat)
        #then get the data from the bounding box, pick a point from there:
        self.longitude = tweet_dictionary['place']['bounding_box']['coordinates'][0][0][0]
        self.latitude = tweet_dictionary['place']['bounding_box']['coordinates'][0][0][1]
        print("long and lat: ")
        print(self.longitude)
        print(self.latitude)

        #that means that there was a geo value associated with the tweet, so just use that:
        #    #Point coordinates are in x, y order (easting, northing for projected coordinates, longitude, latitude for geographic coordinates):
        #    #"geo": {"coordinates": [33.46719916, -112.073], "type": "Point"}
        #    self.longitude = tweet_dictionary['geo']['coordinates'][0]
        #    self.latitude = tweet_dictionary['geo']['coordinates'][1]

        self.geoPoint = src.point.Point(self.latitude,self.longitude)
        #now pick 3 other interesting ones:
        self.user_name = tweet_dictionary['user']['screen_name']
        self.follower_count = tweet_dictionary['user']['followers_count']
        self.retweeted = tweet_dictionary['retweeted']


