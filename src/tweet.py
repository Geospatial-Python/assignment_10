#Create a new Tweet class or extend the existing Point class to store:

class Tweet(object):
    def __init__(self,tweet_dictionary): #wanna pass in the tweet dictionary so that you can actually store it
        #the tweet text:
        self.tweet = tweet_dictionary['text'] # get the "text field"

        if tweet_dictionary['geo'] is None: #(long,lat)
            #then get the data from the bounding box, pick a point from there:
            self.longitude = tweet_dictionary['place']['bounding_box']['coordinates'][0][0]
            self.latitude = tweet_dictionary['place']['bounding_box']['coordinates'][0][1]
        else: #that means that there was a geo value associated with the tweet, so just use that:
            #Point coordinates are in x, y order (easting, northing for projected coordinates, longitude, latitude for geographic coordinates):
            #"geo": {"coordinates": [33.46719916, -112.073], "type": "Point"}
            self.longitude = tweet_dictionary['geo']['coordinates'][0]
            self.latitude = tweet_dictionary['geo']['coordinates'][1]

        #now pick 3 other interesting ones:
        self.user_name = tweet_dictionary['user']['screen_name']
        self.follower_count = ['user']['followers_count']
        self.retweeted = tweet_dictionary['retweeted']


