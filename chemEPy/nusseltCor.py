import math

def nu(**kwargs):
    forced = kwargs['forced']
    shape = kwargs['shape']
    try:
        Re = kwargs['Re']
    except:
        pass
    try:
        Pr = kwargs['Pr']
    except:
        pass
    try:
        Gz = kwargs['Gz']
    except:
        pass
    try:
        Ra = kwargs['Ra']
    except:
        pass
    try:
        general = kwargs['general']
    except:
        pass

    if(forced):
        if(shape == 'flatPlate'):
            if(Re<10**3):
                print('Reynolds number is too low')
                return
            elif(Re<5*10**5): #laminar flow over flat plate
                return(0.664*math.sqrt(Re*math.pow(Pr, 1/3)))
            else:
                return(0.036*math.pow(Re, 0.8)*math.pow(Pr, 1/3))

        elif(shape == 'sphere'):
            if(general):
                return(2+(0.4*math.sqrt(Re)+0.06*math.pow(Re, 2/3))*math.pow(Pr, 0.4)*math.pow(kwargs['muInf']/kwargs['muS'], 0.25))
            else:
                if(Re<450):
                    return(2+0.6*math.sqrt(Re)*math.pow(Pr, 1/3))
                else:
                    return(2+(0.4*math.sqrt(Re+0.06*math.pow(Re, 2/3)))*math.pow(Pr, 0.4)*math.pow(kwargs['muInf']/kwargs['muS'], 0.25))

        elif(shape == 'crossCylinder'):
            return(0.3 + (0.62*math.sqrt(Re)*math.pow(Pr,1/3)/math.pow(1+math.pow(0.4/Pr, 2/3), 0.25))*\
            math.pow(1+math.pow(Re/282000, 0.625), 0.8))

        elif(shape == 'tube'): #this part is funky will need to fully enumerate examples
            if(general):
                if(kwargs['uniform'] != 'Ts'):
                    print('general tube correlation is only valid for uniform Ts')
                    return
                if(Re > 2300):
                    print('general correlation only valid for laminar flow')
                    return
                return(3.66 + 0.0668*Gz/(1+0.04*math.pow(Gz, 2/3)))
            else:
                if(Re < 2300):
                    if(Gz < 20):
                        if(kwargs['uniform'] == 'q'):
                            return(4.36)
                        else:
                            return(3.66)
                    elif(Gz > 100):
                        if(kwargs['uniform'] == 'Ts'):
                            return(1.62*math.pow(Gz, 1/3))
                        else:
                            return(1.86*math.pow(Gz, 1/3)*math.pow(kwargs['muB']/kwargs['muW'], 0.14))
                    else:
                        print('tube is intermediate lenght, consider using general = True')
                        return
                else:
                    try:
                        heating = kwargs['heating']
                        if(heating):
                            return(0.023*math.pow(Re, 0.8)*math.pow(Pr, 0.3))
                        else:
                            return(0.023*math.pow(Re, 0.8)*math.pow(Pr, 0.4))
                    except:
                        print('for turbulent flow in tube need heating = T/F')

    else:
        if(shape == 'verticalPlate'):
            if(Ra < 10**4 or Ra > 10**13):
                return((0.825+0.387*math.pow(Ra, 1/6)/math.pow((1+math.pow(0.492/Pr, 9/16)), 8/27)**2))
            elif(Ra > 10**4 and Ra < 10**9):
                return(0.59*math.pow(Ra, 0.25))
            else:
                return(0.1*math.pow(Ra, 1/3))

        elif(shape == 'horizontalPlate'):
            if((kwargs['side']=='above' and kwargs['plateTemp']=='hot') or (kwargs['side']=='below' and kwargs['plateTemp']=='cold')):
                if(Ra < 10**5):
                    print('Rayleigh number is too low')
                    return
                elif(Ra > 10**5 and Ra < 2*10**7):
                    return(0.54*math.pow(Ra, 0.25))
                elif(Ra > 2*10**7 and Ra < 3*10**10):
                    return(0.14*math.pow(Ra, 1/3))
                else:
                    print('Rayleigh number is too high')
            else:
                if(Ra < 3*10**5):
                    print('Rayleigh number is too low')
                elif(Ra > 3*10**5 and Ra < 10**10):
                    return(0.27*math.pow(Ra, 0.25))
                else:
                    print('Rayleigh number is to high')

        elif(shape == 'cylinder'):
            if(Ra < 10**12):
                return((0.6+0.387*math.pow(Ra, 1/6)/(math.pow((1+math.pow(0.559/Pr, 9/16)), 8/27)))**2)
            else:
                print('Rayleigh number is too high')

        elif(shape == 'sphere'):
            if(Ra < 10**11):
                return(2+0.589*math.pow(Ra, 0.25/math.pow(1+math.pow(0.469/Pr, 9/16), 4/9)))
            else:
                print('Rayleigh number is too high')
        else:
            print('shape invalid')

def nuInfo():
    print('argument combos are: \n\
    forced = True, shape = flatPlate, Re, Pr \n\
    forced = True, shape = sphere, general = True, Re, Pr, muS, muInf \n\
    forced = True, shape = sphere, general = False, Re, Pr \n\
    forced = True, shape = crossCylinder, Re, Pr \n\
    forced = True, shape = tube, general = True, uniform = Ts, Gz, Re \n\
    forced = True, shape = tube, general = False, uniform = Ts, Gz, Re \n\
    forced = True, shape = tube, general = False, uniform = q, Gz, Re, muB, muW \n\
    forced = True, shape = tube, general = False, Gz, Re, Pr, heating = T/F \n\
    forced = False, shape = verticalPlate, Ra \n\
    forced = False, shape = horizontalPlate, Ra \n\
    forced = False, shape = cylinder, Ra, Pr \n\
    forced = False, shape = sphere, Ra, Pr')
