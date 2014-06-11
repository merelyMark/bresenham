#Adapted from numpy code I wrote
import random

class Vector:
    def __init__(self, _x, _y):
        self.x = float(x)
        self.y = float(y)
    def __init__(self, vals):
        self.x = vals[0]
        self.y = vals[1]
        
    def sub(self, oth):
        out = Vector([self.x - oth.x, self.y - oth.y])
        return out
    def __div__(a, b):
        return Vector([a.x/float(b), a.y/float(b)])
    def __add__(a, b):
        return Vector([a.x + b.x, a.y + b.y])
    def __abs__(obj):
        return Vector([abs(obj.x), abs(obj.y)])
    
    def max(self):
        return max(self.x, self.y)
    def __str__(self):
        return str(self.x) + ' ' + str(self.y)
        
def bresenham(p1, p2):
    p = p1;
    d = p2.sub(p1)
    N = abs(d).max()
    s = d/N
    print(p1)
    for i in range(N):
       p = p+s
       print(int(round(p.x)), int(round(p.y)))
    print
    
bresenham(Vector([3,8]), Vector([9,3]))
