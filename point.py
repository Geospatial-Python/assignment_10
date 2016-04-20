'''
Created on Mar 15, 2016

@author: Max Ruiz
'''
import numpy as np
import scipy as sp
import pysal as ps


class Point(object):

    def __init__(self, x, y, mark = None):
        self.x = x
        self.y = y
        self.mark = mark

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __neg__(self):
        return Point(-self.x, -self.y)

    def check_coincident(self, point):
        return (self.x == point[0] and self.y == point[1])

    def shift_point(self, x_shift, y_shift):
        self.x += x_shift
        self.y += y_shift

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def getPoint(self):
        return (self.x, self.y)

    def getMark(self):
        return self.mark
