import math
from point import point
from line import line
from region import region

class triangle(region):

    def __init__(self, p1, p2, p3):
        self.a = point(p1)
        self.b = point(p2)
        self.c = point(p3)
        ab = line(self.a, self.b)
        bc = line(self.b, self.c)
        ca = line(self.c, self.a)
        s = (ab.length() + bc.length() + ca.length()) / 2
        self.area = math.sqrt(s * (s - ab.length()) * (s - bc.length()) * (s - ca.length()))
        abc = line(self.a, self.b.midpoint(self.c))
        bac = line(self.b, self.a.midpoint(self.c))
        self.centroid = abc.intersection(bac)
        ax = self.a.dispX(self.centroid)
        ay = self.a.dispY(self.centroid)
        bx = self.b.dispX(self.centroid)
        by = self.b.dispY(self.centroid)
        cx = self.c.dispX(self.centroid)
        cy = self.c.dispY(self.centroid)
        self.Ix = (self.area / 12) * (math.pow(ay, 2) + math.pow(by, 2) + math.pow(cy, 2))
        self.Iy = (self.area / 12) * (math.pow(ax, 2) + math.pow(bx, 2) + math.pow(cx, 2))
        self.Ixy = (self.area / 12) * (ax * ay + bx * by + cx * cy)

    def getMidValue(self, j, k, l):
        if (j <= k <= l or l <= k <= j):
            return k
        elif (k <= j <= l or l <= j <= k):
            return j
        elif (j <= l <= k or k <= l <= j):
            return l

    def rotate(self, angle):
        region.rotate(self, angle)
        self.a.rotate(self.centroid, angle)
        self.b.rotate(self.centroid, angle)
        self.c.rotate(self.centroid, angle)