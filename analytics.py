import math
import random
from .utils import euclidean_distance, random_points

def mean_center(points):
    """
    Given a set of points, compute the mean center
    Parameters
    ----------
    points : list
         A list of points in the form (x,y)
    Returns
    -------
    x : float
        Mean x coordinate
    y : float
        Mean y coordinate
    """
    #x = None
    #y = None

    x = [i[0] for i in points]
    y = [i[1] for i in points]

    sumX = (sum(x) / len(points))
    sumY = (sum(y) / len(points))

    x = sumX
    y = sumY

    return x, y


def average_nearest_neighbor_distance(points):
    """
    Given a set of points, compute the average nearest neighbor.
    Parameters
    ----------
    points : list
             A list of points in the form (x,y)
    Returns
    -------
    mean_d : float
             Average nearest neighbor distance
    References
    ----------
    Clark and Evan (1954 Distance to Nearest Neighbor as a
     Measure of Spatial Relationships in Populations. Ecology. 35(4)
     p. 445-453.
    """
    mean_d = 0

    shortDistanceList = []

    for firstPoint in points:
        pointInList = 500
        for secondPoint in points:
            if firstPoint is not secondPoint:
                distance = euclidean_distance(firstPoint, secondPoint)
                if (pointInList > distance):
                    pointInList = distance

        shortDistanceList.append(pointInList)

    mean_d = sum(shortDistanceList) / len(points)

    return mean_d


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

    xmin = 0
    ymin = 0
    xmax = 0
    ymax = 0

    for i in points:
        if i[0] < xmin:
            xmin = i[0]
        if i[1] < ymin:
            ymin = i[1]
        if i[0] > xmax:
            xmax = i[0]
        if i[1] > ymax:
            ymax = i[1]

    mbr = [xmin,ymin,xmax,ymax]


    return mbr


def mbr_area(mbr):
    """
    Compute the area of a minimum bounding rectangle
    """
    area = 0

    length = mbr[3] - mbr[1]
    width = mbr[2] - mbr [0]
    area = length * width

    return area


def expected_distance(area, n):
    """
    Compute the expected mean distance given
    some study area.
    This makes lots of assumptions and is not
    necessarily how you would want to compute
    this.  This is just an example of the full
    analysis pipe, e.g. compute the mean distance
    and the expected mean distance.
    Parameters
    ----------
    area : float
           The area of the study area
    n : int
        The number of points
    """

    expected = 0

    expected = (math.sqrt(area/n)) * (0.5)

    return expected

def num_permutations(p = 99, n= 100):

    ListOfNum = []

    for i in range(p):
        ListOfNum.append(average_nearest_neighbor_distance(random_points(n)))

    return ListOfNum