import numpy as np

def planeWall(**kwargs):
    deltaT = kwargs['tInner'] - kwargs['tOuter']
    del(kwargs['tInner'])
    del(kwargs['tOuter'])
    qOverall = 0
    for vertSec in kwargs:
        tempAr = np.array(kwargs[vertSec])
        try:
            rows = tempAr.shape[1]
        except:
            rows = 1
            tempAr = np.array([tempAr])

        area = tempAr[0][0]
        denom = 0
        for horzSec in range(rows):
            denom += tempAr[horzSec][1]/tempAr[horzSec][2] #L_n/k_n in series

        qOverall += area*deltaT/denom #now we add A*deltaT/series part all in pararell

    return(qOverall)

def planeWallInfo():
    print('args are tInner, tOuter, and a set of lists defined by k1 = [area1, length1, k1],\
    k2 = [[area2, length_2a, k_2a],[area2, length_2b, k2_2b]], ...')

class rectangle:
    def __init__(self, pt1, pt2, pt3, pt4):
        self.pt1 = pt1
        self.pt2 = pt2
        self.pt3 = pt3
        self.pt4 = pt4

        self.planeEq = lambda x,y,z: a*x + b*y + c*z == d

class rectPrism:
    def __init__(self, blf, trr):
        #I am naming 8 points A-H starting with the bottom left front and the going clockwise then bottom left back and going clockwise
        #this allows for a rectPrism to be defined using only 2 points
        A = np.array(blf)
        B = np.array([blf[0], blf[1], trr[2]])
        C = np.array([trr[0], blf[1], trr[2]])
        D = np.array([trr[0], blf[1], blf[2]])
        E = np.array([blf[0], trr[1], blf[2]])
        F = np.array([blf[0], trr[1], trr[2]])
        G = np.array(trr)
        H = np.array([trr[0], trr[1], blf[2]])

        face1 = rectangle(pt1 = A, pt2 = B, pt3 = C, pt4 = D)
        face2 = rectangle(pt1 = D, pt2 = C, pt3 = G, pt4 = H)
        face3 = rectangle(pt1 = E, pt2 = F, pt3 = G, pt4 = H)
        face4 = rectangle(pt1 = A, pt2 = B, pt3 = F, pt4 = E)
        face5 = rectangle(pt1 = B, pt2 = C, pt3 = F, pt4 = G)
        face6 = rectangle(pt1 = A, pt2 = D, pt3 = E, pt4 = H)

        self.sides = [face1, face2, face3, face4, face5, face6]
        self.neighbors = []

    def updateNeighbors(self, new):
        for n in new:
            self.neighbors.append(n)

class layer:
    def __init__(self, **kwargs):
        self.

class model:
    def __init__(self, cords, dim):
        self.cords = cords
        self.dim = dim
        self.layers = []
        self.allSS = True

    def addLayer(self, **kwargs):
