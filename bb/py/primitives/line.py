import math
from point import point

class line:

    def __init__(self, *args):
        if (len(args) == 1 and isinstance(args[0], line)):
            other = args[0]
            self.a = point(other.a)
            self.b = point(other.b)
            self.slope = other.slope
            self.intercept = other.intercept
        elif (len(args) == 2 and isinstance(args[0], point)):
            if (isinstance(args[1], point)):
                p1 = args[0]
                p2 = args[1]
                self.a = point(p1)
                self.b = point(p2)
                if not(self.vertical()):
                    self.slope = (self.b.y - self.a.y) / (self.b.x - self.a.x)
                    self.intercept = self.b.y - self.slope * self.b.x
            else:
                p = args[0]
                m = args[1]
                self.a = point(p)
                self.b = point(p.x + 1, p.y + m)
                self.slope = float(m)
                self.intercept = self.a.y - self.slope * self.a.x

    def intersection(self, other):
        denominator = ((self.a.x - self.b.x) * (other.a.y - other.b.y)) - ((self.a.y - self.b.y) * (other.a.x - other.b.x))
        xNum = ((self.a.x * self.b.y - self.b.x * self.a.y) * (other.a.x - other.b.x)) - ((self.a.x - self.b.x) * (other.a.x * other.b.y - other.a.y * other.b.x))
        yNum = ((self.a.x * self.b.y - self.b.x * self.a.y) * (other.a.y - other.b.y)) - ((self.a.y - self.b.y) * (other.a.x * other.b.y - other.a.y * other.b.x))
        return point(xNum / denominator, yNum / denominator)

    def projection(self, other):
        if self.horizontal():
            return point(other.x, self.a.y)
        elif self.vertical():
            return point(self.a.x, other.y)
        else:
            normal = line(other, 1 / self.slope)
            return self.intersection(normal)

    def translate(self, other, displacement):
        if self.horizontal():
            return point(other.x + displacement, other.y)
        elif self.vertical():
            return point(other.x, other.y + displacement)
        else:
            p = point(other)
            denominator = math.sqrt(math.pow(self.slope, 2) + 1)
            p.shift(displacement / denominator, self.slope * displacement / denominator)
            return p

    def length(self):
        return self.a.distance(self.b)

    def horizontal(self):
        return self.a.y == self.b.y

    def vertical(self):
        return self.a.x == self.b.x

    def rotate(self, vertex, angle):
        self.a.rotate(vertex, angle)
        self.b.rotate(vertex, angle)
        if not(self.vertical()):
            self.slope = (self.b.y - self.a.y) / (self.b.x - self.a.x)
            self.intercept = self.b.y - self.slope * self.b.x

    def x(self, y):
        return ((y - self.intercept) / self.slope)

    def y(self, x):
        return (self.slope * x + self.intercept)