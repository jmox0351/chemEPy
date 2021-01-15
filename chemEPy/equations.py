import pandas as pd
import math
import pkg_resources

antDf = pd.read_csv(pkg_resources.resource_filename(__name__, 'data/antoine.csv'))

def antoine(**kwargs):
    name = kwargs['name']
    info = []

    try:
        kwargs['P'] #if unknown is P
    except:
        for index, row in antDf.iterrows():
            if(name == row[0]): #We have multiple sources here so we are going to need to try multiple rows for the same name
                if(kwargs['T'] >= row[4] and kwargs['T'] <= row[5]):
                    info = row
                    break
            if(len(info) == 0): #if no exceptable options are found
                return('Temperature is outside of acceptable range or name not found see antoineNames for names and ranges')
        return(10**(info[1]-info[2]/(info[3]+kwargs['T']))) #else return pressure in mmHg
    try:
        kwargs['T']
    except:
        for index, row in antDf.iterrows(): #we are going with the first valid row for now
            if(name == row[0]):
                info = row
                break
        if(len(info) == 0):
            return('name not found see antoineNames for names and temperature ranges')
        else:
            return(-1*info[2]/(math.log10(kwargs['P'] - info[1]) - info[3]))

def antoineNames():
    for index, row in antDf.iterrows():
        print('Name:', row[0], ' Min temp (C):', row[4], ' Max temp (C):', row[5])

def antoineUnits():
    print('P is in mmHg and T is in C')
