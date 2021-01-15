import math
import numpy as np
import scipy as sp
from scipy import optimize
from .fluidNumbers import reynolds, prandtl, graetz
from .nusseltCor import nu as nu

def areaLM(r1, r2, l1, l2):
    a1 = math.pi*r1**2*l1
    a2 = math.pi*r2**2*l2
    return((a2-a1)/math.log(a2/a1))

def cylFunc(r3, rho, u, mu, Pr, kOuter, r1, r2, L, kInner, tInner, tOuter, q, hInner):
    return((2/(0.3 + (0.0004202729100991299*Pr^(1/3)*math.sqrt((rho *r3* u)/mu) (14100 + 10^(1/8)*141^(3/8)*\
    ((rho *r3* u)/mu)^(5/8))^(4/5))/(1 + 0.5428835233189814*(1/Pr)^(2/3))^(1/4)) + math.log(r3/r2))/(2*kOuter*L/math.pi)+\
    1/(2*r1*L*math.pi*hInner) + (r2-r1)/(kInner*areaLM(r1,r2,L,L)) - (tInner-tOuter)/q)

def singlePipe(**kwargs):
    try:
        ub = kwargs['ub']
    except:
        ub = 1

    need = ['rhoInner', 'rhoOuter', 'uInner', 'uOuter', 'muInner', 'muOuter', 'PrInner', 'PrOuter', 'kInner', 'kOuter',\
    'r1', 'r2', 'L', 'tInner', 'tOuter', 'q']
    allNeeds = True
    for check in need: #checks all the required args are included if not print and then return
        if(check in kwargs):
            continue
        else:
            print('you are missing argument:', check)
            allNeeds = False
    if(not allNeeds):
        return

    rhoInner = kwargs['rhoInner']
    rhoOuter = kwargs['rhoOuter']
    uInner = kwargs['uInner']
    uOuter = kwargs['uOuter']
    muInner = kwargs['muInner']
    muOuter = kwargs['muOuter']
    PrInner = kwargs['PrInner']
    PrOuter = kwargs['PrOuter']
    r1 = kwargs['r1']
    r2 = kwargs['r2']
    L = kwargs['L']
    kInner = kwargs['kInner']
    kOuter = kwargs['kOuter']
    tInner = kwargs['tInner']
    tOuter = kwargs['tOuter']
    q = kwargs['q']
    ReInner = chemEPy.fluidNumbers.reynolds(rho = rhoInner, u = uInner, L = 2*r1, mu = muInner)
    Gz = chemEPy.fluidNumbers.graetz(D = 2*r1, Re = ReInner, Pr = PrInner, L = L)
    a1 = 2*math.pi*L*r1

    if(tInner > tOuter):
        heat = True
    else:
        heat = False

    hInner = nu(forced = True, shape = tube, uniform = Ts, Re = Re, Gz = Gz, heating = heat)*kInner/(2*r1)
    rGuess = np.linspace(0,ub,101)
    stepSize = rGuess[1] - rGuess[0]
    #now we run the cylFunc with each rGuess, look for the sign change and then use the midpoint as an initial guess
    prev = cylFunc(0, rhoOuter, uOuter, muOuter, PrOuter, kOuter, r1, r2, L, kInner, tInner, tOuter, q, hInner)
    rUpper, rLower = 1, 1
    for i in rGuess:
        nex = cylFunc(0, rhoOuter, uOuter, muOuter, PrOuter, kOuter, r1, r2, L, kInner, tInner, tOuter, q, hInner)
        if(prev * nex <= 0):
            rUpper = i # we have found an good initial guess
            rLower = i - stepSize
            break
        else:
            prev = nex
        if(i == ub): #if we get to the upper bound and still have not found a sign change
            print('upper bound is not large enough')
            return

    sol = sp.optimize.root_scalar(cylFunc, args = (rhoOuter, uOuter, muOuter, PrOuter, kOuter, r1, r2, L, kInner,\
    tInner, tOuter, q, hInner), bracket = [rLower, rUpper], method = 'toms748')

    if(not sol.flag): #if this did not converge
        print('bracket did not converge')
    else:
        return(sol.root)

def singlePipeInfo():
    print('need the following args. Will return r3 the radius to the outer edge of the insulation \n\
    rhoInner, rhoOuter, uInner, uOuter, muInner, muOuter, PrInner, PrOuter, kInner, kOuter, r1, r2, L, tInner, tOuter, q')
