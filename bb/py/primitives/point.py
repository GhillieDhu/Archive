import math

class point:
    
    def __init__(self, *args):
        if ((len(args) == 1) and isinstance(args[0], point)):
            self.x = args[0].x
            self.y = args[0].y
        elif (len(args) == 2):
            self.x = float(args[0])
            self.y = float(args[1])
        
    def distance(self, other):
        return math.sqrt(math.pow(self.dispX(other), 2) + math.pow(self.dispY(other), 2))
        
    def dispX(self, other):
        return other.x - self.x
            
    def dispY(self, other):
        return other.y - self.y
    
    def midpoint(self, other):
        return point((self.x + other.x) / 2, (self.y + other.y) / 2)
        
    def shift(self, xx, yy):
        self.x += xx
        self.y += yy
        
    def rotate(self, vertex, angle):
        self.shift(-vertex.x, -vertex.y)
        newX = (self.x * math.cos(angle)) - (self.y * math.sin(angle))
        newY = (self.x * math.sin(angle)) + (self.y * math.cos(angle))
        self.x = newX
        self.y = newY
        self.shift(vertex.x, vertex.y)
        
    def __str__(self):
        return ('(' + str(self.x) + ', ' + str(self.y) + ')')