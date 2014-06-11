#Adapted from Cris Luengo's MATLAB code at
#http://www.cb.uu.se/~cris/blog/index.php/archives/400
#For python with numpy
import numpy as np

def bresenham(p1, p2):

    #p1 = np.rint(np.random.rand(2)*20).astype(np.int);
    #p2 = np.rint(np.random.rand(2)*20).astype(np.int);

    p = p1;
    d = p2-p1
    N = max(abs(d))
    s = d.astype(np.float32)/N.astype(np.float32)
    print(p1)
    for i in range(N):
       p = p+s
       print(np.rint(p).astype(np.int))
    print
    
np.random.seed(0)
bresenham(np.array([3,8]), np.array([9,3]))
