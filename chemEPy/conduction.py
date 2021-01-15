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
