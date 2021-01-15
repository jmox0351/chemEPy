import pandas as pd
import scipy as sp
from scipy import optimize
import pkg_resources

vdwDf = pd.read_csv(pkg_resources.resource_filename(__name__, 'data/vdw.csv'))
afDf = pd.read_csv(pkg_resources.resource_filename(__name__, 'data/acentricFactor.csv'))

def vdwInfo():
    print('a = bar*L^2/mol^2 and b = L/mol, std R is 0.08314 L*Bar*K^-1*mol^-1')
    
def idealGasInfo():
    print('solves for any of 4 unknowns P,V,n,T units are agnostic')

def idealGas(**kwargs):
    try:
        kwargs['T']
    except:
        return (kwargs['P'] * kwargs['V']/(kwargs['n']*kwargs['R']))
    try:
        kwargs['n']
    except:
        return (kwargs['P'] * kwargs['V']/(kwargs['T']*kwargs['R']))
    try:
        kwargs['P']
    except:
        return (kwargs['n'] * kwargs['R'] * kwargs['T']/kwargs['V'])
    try:
        kwargs['V']
    except:
        return (kwargs['n'] * kwargs['R'] * kwargs['T']/kwargs['P'])

def vdw(**kwargs):
    info = []
    for index, row in vdwDf.iterrows(): #get correct row from Df
        if row[1] == kwargs['name']:
            info = row
            break

    if(len(info) == 0): #check that compound is in the Df
        print('compound not found')
        return

    try:
        kwargs['T']
    except:
        return (kwargs['P'] + info[2] * kwargs['n']**2 / kwargs['V']) * (kwargs['V'] - kwargs['n']*info[3]) / \
        (kwargs['n']*kwargs['R'])
    try:
        kwargs['P']
    except:
        return (kwargs['n']*kwargs['R']*kwargs['T']) / (kwargs['V']-kwargs['n']*info[3]) -\
        (info[2]*kwargs['n']**2/kwargs['V']**2)
    try:
        kwargs['V']
    except:
        def f(v): #define f as a function of v
            return((kwargs['P']+kwargs['n']**2 * info[2]/v**2)*(v-kwargs['n']*info[3]) - kwargs['n']*kwargs['R']*kwargs['T'])
        def fprime(v): #define fprime so we can feed this to newton
            return(kwargs['P'] + (info[2]*kwargs['n']**2/v**2) -\
            (2*info[2]*kwargs['n']**2 * (-1*info[3]*kwargs['n']+v)/v**3))
        x0 = idealGas(P = kwargs['P'], n = kwargs['n'], R = kwargs['R'], T = kwargs['T']) #use ideal gas as starting point
        ans = optimize.root_scalar(f, x0 = x0, fprime = fprime, method = 'newton')
        if ans.converged:
            return ans.root
        else:
            return('vdw equation did not converge')
    try:
        kwargs['n']
    except:
        def f(n):
            return((kwargs['P']+n**2 * info[2]/kwargs['V']**2)*(kwargs['V']-n*info[3]) - n*kwargs['R']*kwargs['T'])
        def fprime(n):
            return(-1*kwargs['R']*kwargs['T'] - info[3]*(kwargs['P']+info[2]*n**2/kwargs['V']**2) +\
            (2*info[2]*n*(-1*info[3]*n+kwargs['V'])/kwargs['V']**2))
        x0 = idealGas(P = kwargs['P'], V = kwargs['V'], R = kwargs['R'], T = kwargs['T'])
        ans = optimize.root_scalar(f, x0 = x0, fprime = fprime, method = 'newton')
        if ans.converged:
            return ans.root
        else:
            return('vdw equation did not converge')

def vdwNames():
    for index, row in vdwDf.iterrows():
        print(row[1])

def pengRobinson(**kwargs):
    info = []
    for index, row in afDf.iterrows():
        if row[0] == kwargs['name']:
            info = row
            break

    if len(info) == 0:
        print('compound not found')
        return

    Tc = info[1]
    Pc = info[2]
    omega = info[4]

    kappa = 0.37464 + 1.54226*omega - 0.26992*omega**2
    try:
        kwargs['T']
        Tr = kwargs['T']/Tc
    except:
        pass
    try:
        kwargs['P']
        Pr = kwargs['P']/Pc
    except:
        pass


if __name__ == "main":
    import sys
