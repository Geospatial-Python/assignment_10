from . import utils
import random
import analytics
import numpy as np
import scipy.spatial as ss
import pysal as ps

class Point(object):
    def __init__(self, x, y, mark={}):
        self.x = x
        self.y = y
        self.mark = mark

    #implement magic methods

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __neg__(self):
        return Point(-self.x, -self.y)

    def coincidentPoint(self, point1):
        point2 = (self.x, self.y)
        return utils.check_coincident(point1, point2)

    def shiftPoint(self,xShift, yShift):
        thePoint = (self.x, self.y)
        self.x, self.y = utils.shift_point(thePoint,xShift,yShift)

    def numpyPoint(self, x = 0, y = 0, n = 1000):
        numpyArray = np.random.uniform(x, y, (n, 2))
        list = []
        marks = ['James', 'Sarah', 'Nick', 'Michael']
        for i in range(len(numpyArray)):
            list.append(Point(numpyArray[i][0]))
            numpyArray[i][1], random.choice(marks)
            return list