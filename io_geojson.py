import json  # for the geojson stuff

# ------------------------------------------------------------------
#
# Joseph Cruz
# io_geojson.py
#
# Stores the functions from point_pattern.py that are a form of
# utility needed for use in other functions
# ------------------------------------------------------------------


def process_tweets(input_file):
    tweets_gj = read_geojson(input_file)
    tweets_out = 0

    list_tweet_ids = []
    for j in range(len(tweets_gj)):
        list_tweet_ids.append(tweets_gj[j]['id'])

    tweets_out = {}
    for i in range(len(list_tweet_ids)):
        id_in = tweets_gj[i]['id']
        tweets_out[id_in] = tweets_gj[i]

    return tweets_out


def read_geojson(input_file):
    """
    Read a geojson file

    Parameters
    ----------
    input_file : str
                 The PATH to the data to be read

    Returns
    -------
    gj : dict
         An in memory version of the geojson
    """
    # Please use the python json module (imported above)
    # to solve this one.
    with open(input_file) as iFile:
        gj = json.load(iFile)
    return gj


def find_largest_city(gj):
    """
    Iterate through a geojson feature collection and
    find the largest city.  Assume that the key
    to access the maximum population is 'pop_max'.

    Parameters
    ----------
    gj : dict
         A GeoJSON file read in as a Python dictionary

    Returns
    -------
    city : str
           The largest city

    population : int
                 The population of the largest city
    """
    gj_features = gj['features']
    city = None
    max_population = 0
    
    for nextFeature in gj_features:
        if nextFeature['pop_max'] > max_population:
            city = nextFeature['name']
            max_population = nextFeature['pop_max']

    return city, max_population


def write_your_own(gj):
    """
    Here you will write your own code to find
    some attribute in the supplied geojson file.

    Take a look at the attributes available and pick
    something interesting that you might like to find
    or summarize.  This is totally up to you.

    Do not forget to write the accompanying test in
    tests.py!
    """
    #Counts the number of world cities
    gj_features = gj['features']
    numWorldCities = 0

    for nextFeature in gj_features:
        if nextFeature['worldcity'] != 0:
            numWorldCities += 1
    return numWorldCities
