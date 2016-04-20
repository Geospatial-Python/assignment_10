import random
import math
import numpy as np
import scipy.spatial as ss
import pysal as ps
import io_geojson as iogj
import folium


# [Joseph] I decided to have Tweet incorporate a Point class
# I can avoid inheritance and just use point data and methods
# as if it were an attribute of Tweet.
class Tweet:
    def __init__(self):
        self.point_data = Point()
        self.text = ""
        self.latitutde = 0.0
        self.longitutde = 0.0
        self.interesting = []


class TweetPattern:
    def __init__(self):
        self.Tweets = []

    def assign_lat_long(self, input_file):
        set_tweets = iogj.process_tweets(input_file)
        new_tweet = Tweet()

        for key in set_tweets:
            in_text = set_tweets[key]['text']

            lat_min = 999
            lat_max = -999
            long_min = 999
            long_max = -999

            for i in range(4):
                if i == 0:
                    long_min = set_tweets[key]['place']['bounding_box']['coordinates'][0][i][0]
                    long_max = set_tweets[key]['place']['bounding_box']['coordinates'][0][i][0]

                    lat_min = set_tweets[key]['place']['bounding_box']['coordinates'][0][i][1]
                    lat_max = set_tweets[key]['place']['bounding_box']['coordinates'][0][i][1]
                else:
                    if set_tweets[key]['place']['bounding_box']['coordinates'][0][i][0] > long_max:
                        long_max = set_tweets[key]['place']['bounding_box']['coordinates'][0][i][0]
                    if set_tweets[key]['place']['bounding_box']['coordinates'][0][i][0] < long_min:
                        long_min = set_tweets[key]['place']['bounding_box']['coordinates'][0][i][0]

                    if set_tweets[key]['place']['bounding_box']['coordinates'][0][i][1] > lat_max:
                        lat_max = set_tweets[key]['place']['bounding_box']['coordinates'][0][i][1]
                    if set_tweets[key]['place']['bounding_box']['coordinates'][0][i][1] < lat_min:
                        lat_min = set_tweets[key]['place']['bounding_box']['coordinates'][0][i][1]

            x = random.uniform(long_min, long_max)
            y = random.uniform(lat_min,lat_max)

            new_tweet.latitude = y
            new_tweet.longitutde = x
            new_tweet.text = in_text
            self.Tweets.append(new_tweet)


    def build_folium_map(self):
        map_tweets = folium.map(location=[33.42,-112.065])
        for j in range(len(self.Tweets)):
            folium.marker([self.Tweets[j].y,self.Tweets[j].x],popup = self.Tweets[j].text)

class Point:
    """
    For whatever reason, cannot get import to work, just moved functionality
    into this file instead.
    """
    def __init__(self,x = 0,y = 0,mark = ""):
        self.x = x
        self.y = y
        self.mark = mark

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        direction = ""
        if self.y > other.y:
            direction += "N"
        elif self.y == other.y:
            direction += "-"
        else:
            direction += "S"
        if self.x > other.x:
            direction += "E"
        elif self.x == other.y:
            direction += "-"
        else:
            direction += "W"

        return direction

    def __neg__(self):
        return Point(-self.x,-self.y,self.mark)

    def shift_point(self,x_move,y_move):
        this_point = (self.x,self.y)
        self.x += x_move
        self.y += y_move

    """
    Made redundant by __eq__
    def coincident(self, check_point):
        if check_point.x == self.x and check_point.y == self.y:
            return True
        else:
            return False
    """


class PointPattern:
    def __init__(self):
        self.set_of_points = []

    def avg_nearest_neighbor_dist(self,mark):
        average_nearest_neighbor_distance(self.set_of_points, mark)

    def num_coincident_points(self):
        coincident_points = 0
        len_list = len(self.set_of_points)
        for i in range(len_list):
            if i == len_list-1:
                break
            for j in range(len_list+1):
                if self.set_of_points[i] == self.set_of_points[j]:
                    coincident_points += 1

        return coincident_points

    def list_marks(self):
        mark_list = []
        len_list = len(self.set_of_points)
        for i in range(len_list):
            if not mark_list:
                mark_list.append(self.set_of_points[i].mark)
            elif self.set_of_points[i].mark not in mark_list:
                mark_list.append(self.set_of_points[i].mark)

        return mark_list

    def list_mark_subsets(self):
        mark_list = PointPattern.list_marks(self)
        mark_count = []
        sub_set = []
        for i in range(len(mark_list)):
            sub_set = []
            for j in range(len(self.set_of_points)):
                if mark_list[i] == self.set_of_points[j].mark:
                    sub_set.append(self.set_of_points[j])
            mark_count.append(sub_set)

        return mark_count

    def create_random_points(self, n=100, marks = []):
        if not marks:
            self.set_of_points = create_random_unmarked_points(n)
        else:
            self.set_of_points = create_random_marked_points(n,marks)

    def k_realizations(self,k = 99):
        return permutations(k,n = 100)

    def critical_points(self,realizations):
        return find_crit_points(realizations)

    def compute_g(self, min_dist):
        gs = 0
        len_list = len(self.set_of_points)
        all_pts_min_dists = []
        for i in range(len_list):
            local_nn = 0
            for j in range(len_list):
                if i != j:
                    new_distance = euclidean_distance(self.set_of_points[i],self.set_of_points[j])
                    if local_nn == 0:
                        local_nn = new_distance
                    elif new_distance < local_nn:
                        local_nn = new_distance

                    all_pts_min_dists.append(local_nn)

        for k in range(len(all_pts_min_dists)):
            if all_pts_min_dists[k]<=min_dist:
                gs += 1

        return gs
    """
    Assignment 8 stuff
    """

    def nearest_neighbor_kdtree(self, mark=""):
        buffer = build_np_array(self.set_of_points, mark)
        kdtree = ss.KDTree(buffer)
        calc_distances = []
        values = []
        for i in buffer:
            nn_distance, nn = kdtree.query(i, k=2)
            #do we remove the first one since it is the coincident?
            calc_distances.append(nn_distance[1])
            values.append(nn)
        distances = np.array(calc_distances)
        return distances

    def nn_kdtree_avg(self, mark=""):
        return np.mean(self.nearest_neighbor_kdtree(mark))

    def np_compute_g(self, min_dist, mark=""):
        buffer = build_np_array(self.set_of_points, mark)
        g = 0
        n = len(self.set_of_points)
        list_of_min_dists = []
        for i in range(len(self.set_of_points)):
            local_nn = 0
            for j in range(len(self.set_of_points)):
                if i != j:
                    new_dist = ss.distance.euclidean(buffer[i],buffer[j])
                    if local_nn == 0:
                        local_nn = new_dist
                    elif new_dist < local_nn:
                        local_nn = new_dist
            list_of_min_dists.append(local_nn)

        for k in range(len(list_of_min_dists)):
            if list_of_min_dists[k] <= min_dist:
                g += 1

        return g/n

    def np_gen_random_points(self, n = 100, dom_spec = False):
        lop = []
        if dom_spec:
            lx,ly,mx,my = minimum_bounding_rectangle(self.set_of_points)
            for i in range(n):
                x = np.random.uniform(lx, mx)
                y = np.random.uniform(ly, my)
                n_p = Point(x,y)
                lop.append(n_p)
        else:
            for i in range(n):
                tuples = np.random.uniform(0,1,(1,2))
                n_p = Point(tuples[0][0],tuples[0][1])
                lop.append(n_p)

        return lop


"""
Assignment_08
"""


def build_np_array(points, mark=""):
    if not points:
        return "No Points in List"
    point_buffer = []

    if mark == "":
        for i in range(len(points)):
            new_tuple = [points[i].x,points[i].y]
            point_buffer.append(new_tuple)

    else:
        for i in range(len(points)):
            if points[i].mark == mark:
                new_tuple = [points[i].x,points[i].y]
                point_buffer.append(new_tuple)

    return np.array(point_buffer)


def nn_kdtree(points):
    tree = ss.KDTree(points)
    distances = []
    values = []
    for i in points:
        nn_distance, nn = tree.query(i, k=2)
        distances.append(nn_distance)
        values.append(nn)

    return distances,values


def np_create_rand_points(self, n, specified):
    lop = []
    if not specified:
        for i in range(n):
            tup = np.random.uniform(0,1,(1,2))
            point_n = Point(tup[0],tup[1])
            lop.append(point_n)
    else:
        minimum_bounding_rectangle(self.set_of_points)

    return lop


"""
Old Assignment
"""


def create_random_marked_points(n, marks = []):
    list_of_tuples = [(random.uniform(0,1), random.uniform(0,1)) for i in range(n)]
    list_of_marks = [random.choice(marks) for i in range(n)]
    list_of_points = []
    for j in range(n):
        new_point = Point(list_of_tuples[j][0],list_of_tuples[j][1],list_of_marks[j])
        list_of_points.append(new_point)

    return list_of_points


def create_random_unmarked_points(n):
    list_of_tuples = [(random.uniform(0,1), random.uniform(0,1)) for i in range(n)]
    list_of_points = []
    for j in range(n):
        new_point = Point(list_of_tuples[j][0],list_of_tuples[j][1], "")
        list_of_points.append(new_point)

    return list_of_points


def euclidean_distance(a, b):
    distance = math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)
    return distance


def average_nearest_neighbor_distance(points, mark=""):
    mean_d = 0
    total = 0
    local_nn = 0
    num_of_points = len(points)

    if not mark:
        for i in range(num_of_points):
            local_nn = 0
            for j in range(num_of_points):
                if i != j:
                    new_distance = euclidean_distance(points[i],points[j])
                    if local_nn == 0:
                        local_nn = new_distance
                    elif new_distance < local_nn:
                        local_nn = new_distance

            total += local_nn

    else:
        for i in range(num_of_points):
            local_nn = 0
            for j in range(num_of_points):
                if i != j and points[i].mark == points[j].mark:
                    new_distance = euclidean_distance(points[i],points[j])
                    if local_nn == 0:
                        local_nn = new_distance
                    elif new_distance < local_nn:
                        local_nn = new_distance

            total += local_nn

    mean_d = total/num_of_points

    return mean_d


def permutations(p = 99, n = 100):
    list_means = []

    for i in range(p):
        marks = ["elf", "dwarf", "human", "orc"]
        rand_points = create_random_marked_points(n, marks)
        newMean = average_nearest_neighbor_distance(rand_points)
        list_means.append(newMean)

    return list_means


def find_crit_points(list_means):
    entries = list_means
    maxEntry = 0
    minEntry = 2
    for i in range(len(list_means)):
        if entries[i] > maxEntry:
            maxEntry = entries[i]
        if entries[i] < minEntry:
            minEntry = entries[i]

    return minEntry,maxEntry


def crit_point_check(minEntry, maxEntry, observed):
    if observed < minEntry or observed > maxEntry:
        return True
    else:
        return False

def minimum_bounding_rectangle(points):
    """
    Given a set of points, compute the minimum bounding rectangle.

    Parameters
    ----------
    points : list
             A list of points in the form (x,y)

    Returns
    -------
     : list
       Corners of the MBR in the form [xmin, ymin, xmax, ymax]
    """
    mbr = [0,0,0,0]
    numOfPoints = len(points)
    for i in range(numOfPoints):
        #Check for min and max x
        if points[i][0] < mbr[0]:
            mbr[0] = points[i][0]
        if points[i][0] > mbr[2]:
            mbr[2] = points[i][0]
        #Check for min and max y
        if points[i][1] < mbr[1]:
            mbr[1] = points[i][1]
        if points[i][1] > mbr[3]:
            mbr[3] = points[i][1]

    return mbr