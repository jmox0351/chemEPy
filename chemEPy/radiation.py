def q(**kwargs):
    try:
        imperial = kwargs['imperial']
        if(imperial):
            sigma = 0.1714*10**-8
        else:
            sigma = 5.676*10**-8
    except:
        sigma = 5.676*10**-8

    body1 = kwargs['body1']
    body2 = kwargs['body2']
    a = kwargs['area']
    t1 = kwargs['t1']
    t2 = kwargs['t2']
    try:
        ep1 = kwargs['epsilon1']
    except:
        ep1 = 1
    try:
        ep2 = kwargs['epsilon2']
    except:
        ep2 = 1
    try:
        f = kwargs['viewFactor']
    except:
        f = 1
    try:
        a2 = kwargs['area2']
    except:
        a2 = a

    if(body1 == 'black' and body2 == 'black'):
        return(a*f*sigma*(t1**4-t2**4))
    elif((body1 == 'black' and body2 == 'grey') or (body1 == 'grey' and body2 == 'black')):
        return(a*ep1*sigma*(t1**4-t2**4))
    else:
        return(a * compositeVF(f, ep1, ep2, a, a2) * simga * (t1**4-t2**4))

def compositeVF(f, ep1, ep2, a1, a2):
    return(1/(1/f + 1/ep1 - 1 + a1/a2 * (1/ep2-1)))

def qInfo():
    print('arguments are body1(grey/black), body2(grey/black), area, t1, t2, epsilon1, epsilon2.\n\
    Optional args are imperial(T/F) default is False \n\
    viewFactor default is 1 \n\
    epsilon1 default is 1 (black body) \n\
    epsilon2 default is 1 \n\
    area2 if doing 2 grey bodies default is area2 = area')
