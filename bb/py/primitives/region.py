import math
from point import point

class region:

    def parallelAxisX(self, center):
        return self.Ix + (self.area * math.pow(self.centroid.dispY(center), 2))

    def parallelAxisY(self, center):
        return self.Iy + (self.area * math.pow(self.centroid.dispX(center), 2))

    def parallelAxisXY(self, center):
        return self.Ixy + (self.area * self.centroid.dispX(center) * self.centroid.dispY(center))

    def rotate(self, angle):
        newIx = ((self.Ix + self.Iy) / 2) + ((self.Ix - self.Iy) / 2) * math.cos(2 * angle) - (self.Ixy * math.sin(2 * angle))
        newIy = ((self.Ix + self.Iy) / 2) - ((self.Ix - self.Iy) / 2) * math.cos(2 * angle) + (self.Ixy * math.sin(2 * angle))
        newIxy = ((self.Ix - self.Iy) / 2) * math.sin(2 * angle) + (self.Ixy * math.cos(2 * angle))
        self.Ix = newIx
        self.Iy = newIy
        self.Ixy = newIxy