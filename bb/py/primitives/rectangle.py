import math
from point import point
from region import region

class rectangle(region):

    def __init__(self, *args):
        if len(args) == 2:
            self.a = point(args[0])
            self.b = point(args[1].x, args[0].y)
            self.c = point(args[1])
            self.d = point(args[0].x, args[1].y)
            self.area = abs(self.a.dispX(self.b)) * abs(self.b.dispY(self.c))
            self.centroid = self.a.midpoint(self.c)
            bb = abs(self.a.dispX(self.b))
            hh = abs(self.b.dispY(self.c))
            self.Ix = bb * math.pow(hh, 3) / 12
            self.Iy = hh * math.pow(bb, 3) / 12
            self.Ixy = 0
        elif len(args) == 3:
            self.a = point(args[0])
            self.b = point(args[1])
            self.c = point(args[2])
            angle = math.atan(self.a.dispY(self.b) / self.a.dispX(self.b))
            self.b.rotate(self.a, -angle)
            self.c.rotate(self.a, -angle)
            self.c.shift(self.c.dispX(self.b), 0)
            simpler = rectangle(self.a, self.c)
            oldA = point(self.a)
            simpler.rotate(angle)
            self.area = simpler.area
            self.centroid = simpler.centroid
            self.centroid.shift(self.a.dispX(oldA), self.a.dispY(oldA))
            self.a = simpler.a
            self.b = simpler.b
            self.c = simpler.c
            self.d = simpler.d
            self.Ix = simpler.Ix
            self.Iy = simpler.Iy
            self.Ixy = simpler.Ixy

    def rotate(self, angle):
        region.rotate(self, angle)
        self.a.rotate(self.centroid, angle)
        self.b.rotate(self.centroid, angle)
        self.c.rotate(self.centroid, angle)
        self.d.rotate(self.centroid, angle)