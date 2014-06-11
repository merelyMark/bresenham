#Bresenham algo in processing.py
import random

class Vector:
    def __init__(self, vals):
        self.x = vals[0]
        self.y = vals[1]
    def __eq__(a,b):
        return a.x == b.x and a.x == b.x
        
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
        
num_clicks_stored = 2
click_number = 1
mouse_click = [Vector([i,i]) for i in range(2)]

def bresenham(p1, p2):
    #http://www.cb.uu.se/~cris/blog/index.php/archives/400

    #p1 = Vector([random.randint(0,20) for i in range(2)])
    #p2 = Vector([random.randint(0,20) for i in range(2)])

    p = Vector([p1.x, p1.y]);
    d = p2.sub(p1)
    N = d.__abs__().max()
    s = d/N
    #print(p1)
    
    pixels[int(p1.y)*width + int(p1.x)] = color(255)
    for i in range(N):
       p = p+s
       pixels[int(round(p.y))*width + int(round(p.x))] = color(255,255,255)

    
def setup():
    size(600, 600)
    
def mouseClicked():
    if (click_number >= num_clicks_stored):
        click_number = 0;
    mouse_click[click_number] = Vector([mouseX, mouseY])
    click_number+=1
    print(mouse_click[0])
    print(mouse_click[1])



def draw():
        
    background(0)
#    stroke(255)
#    line(mouse_click[0].x, mouse_click[0].y, mouse_click[1].x, mouse_click[1].y)
    loadPixels()
    bresenham(mouse_click[0], mouse_click[1])
    updatePixels()


