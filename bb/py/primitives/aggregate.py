import math
from point import point
from region import region

class aggregate(region):

    def __init__(self):
        self.area = 0
        self.centroid = point(0, 0)
        self.Ix = 0
        self.Iy = 0
        self.Ixy = 0

    def add(self, *sections):
        for section in sections:
            if isinstance(section, region):
                newarea = self.area + section.area
                newCentroid = point(self.centroid)
                newCentroid.shift(self.centroid.dispX(section.centroid) * section.area / newarea, self.centroid.dispY(section.centroid) * section.area / newarea)
                self.Ix = self.parallelAxisX(newCentroid) + section.parallelAxisX(newCentroid)
                self.Iy = self.parallelAxisY(newCentroid) + section.parallelAxisY(newCentroid)
                self.Ixy = self.parallelAxisXY(newCentroid) + section.parallelAxisXY(newCentroid)
                self.area = newarea
                self.centroid = newCentroid

    def subtract(self, *sections):
        for section in sections:
            if isinstance(section, region):
                newarea = self.area - section.area
                newCentroid = point(self.centroid)
                newCentroid.shift(-self.centroid.dispX(section.centroid) * section.area / newarea, -self.centroid.dispY(section.centroid) * section.area / newarea)
                self.Ix = self.parallelAxisX(newCentroid) - section.parallelAxisX(newCentroid)
                self.Iy = self.parallelAxisY(newCentroid) - section.parallelAxisY(newCentroid)
                self.Ixy = self.parallelAxisXY(newCentroid) - section.parallelAxisXY(newCentroid)
                self.area = newarea
                self.centroid = newCentroid
