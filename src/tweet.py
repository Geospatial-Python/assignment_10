#Create a new Tweet class or extend the existing Point class to store:
import src.point
import numpy as np
import random

class Tweet(object):
    def __init__(self,tweet_dictionary):
        #want pass in the tweet dictionary so that you can actually store it
        #the tweet text:
        self.tweetText = tweet_dictionary['text'] # get the "text field"
        numberoftweetsmapped= 0
        if tweet_dictionary['geo'] is not None: #(long,lat)
            #that means that there was a geo value associated with the tweet, so just use that:
            #Point coordinates are in x, y order (easting, northing for projected coordinates, longitude, latitude for geographic coordinates):
            #"geo": {"coordinates": [33.46719916, -112.073], "type": "Point"}
            self.latitude = tweet_dictionary['geo']['coordinates'][0]
            self.longitude = tweet_dictionary['geo']['coordinates'][1]
            print("geo!")
            print(tweet_dictionary['geo']['coordinates'][0])
            print(tweet_dictionary['geo']['coordinates'][1])

        else:
        #then get the data from the bounding box, pick a point from there:
            print("bounding box")
            print(tweet_dictionary['place']['bounding_box']['coordinates'])
            print(tweet_dictionary['place']['bounding_box']['coordinates'][0])
            #coordinates[0] = [[-111.842244, 33.204608], [-111.842244, 33.385822], [-111.634889, 33.385822], [-111.634889, 33.204608]]


            #So, the trick is to get the minimum and maximum values from the bounding box:
            toStack = tweet_dictionary['place']['bounding_box']['coordinates'][0]
            coorStack = np.vstack(toStack)
            #now find the max and min of the longitude/latitude
            coorMax = np.amax(coorStack,axis=0) #[x,y]
            coorMin = np.amin(coorStack,axis=0)

            #now randomly distribute the points within the polygon:
            self.longitude = random.uniform(coorMin[0],coorMax[0])
            self.latitude = random.uniform(coorMin[1],coorMax[1])

          #  self.longitude = tweet_dictionary['place']['bounding_box']['coordinates'][0][0][0]
        #    self.latitude = tweet_dictionary['place']['bounding_box']['coordinates'][0][0][1]




        print("long and lat: ")
        print(self.longitude)
        print(self.latitude)


        self.geoPoint = src.point.Point(self.latitude,self.longitude)
        #now pick 3 other interesting ones:
        self.user_name = tweet_dictionary['user']['screen_name']
        self.follower_count = tweet_dictionary['user']['followers_count']
        self.retweeted = tweet_dictionary['retweeted']


