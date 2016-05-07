import math
import random
from . point import Point
from . import analytics
from . import utils
import numpy as np

class PointPattern(object):

    def __init__(self):
        self.thePoints = []

    def averageNearestNeighborDistance(self, marks=None):
        return analytics.average_nearest_neighbor_distance(self.points, marks)

    def coincidentPoints(self):
        counter = 0
        coincidentList = []

        for c in range(len(self.thePoints)):
            for o in range(len(self.thePoints)):
                if c in coincidentList:
                    continue
                elif c == o:
                    continue
                elif self.thePoints[c] == self.thePoints[o]:
                    counter = counter + 1;
                    coincidentList.append(o)

        return counter

    def listMarks(self):
        markList = []

        for points in self.thePoints:
            if points.mark not in markList:
                markList.append(points.mark)

        return markList

    def subsetPoints(self, mark):
        subsetList = []

        for points in self.thePoints:
            if points.mark == mark:
                subsetList.append(points)

        return subsetList

    def randomPoints(self, none = None):
        randomList = []

        if none is None:
            none = len(self.thePoints)
        self.marks = ['James', 'Paul', 'Sarah', 'Michael', 'Nancy', 'Henry']

        for n in range(none):
            randomList.append(Point(random.randint(1,50), random.randint(1,50), random.choice(self.marks)))

        return randomList

    def realizationPoints(self, k):
        return analytics.num_permutations(self.marks, k)

    def criticalPoints(self, marks):
        return utils.critical_points(self.realizationPoints(50))

    def add(self, points):
        self.thePoints.append(points)

    def Gfunction(self, nsteps):
        ds = np.linspace(0, 50, nsteps)
        sum = 0

        for s in range(nsteps):
            oI = ds[s]
            minimumDistance = None
            for g in range(len(ds)):
                temp = abs(g - oI)

                if g is not s:
                    continue
                if minimumDistance is None:
                    minimumDistance = temp
                if minimumDistance > temp:
                    minimumDistance = temp
                else:
                    continue
            sum = sum + minimumDistance

        return sum / nsteps