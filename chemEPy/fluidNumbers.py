def biot(**kwargs):
    return(kwargs['h']*kwargs['k']/kwargs['L'])

def biotInfo():
    print('arguments are h, k, and L')

def graetz(**kwargs):
    try:
        kwargs['rho']
        return(kwargs['D']**2 * kwargs['rho'] * kwargs['u'] * kwargs['cp'] / (kwargs['L']*kwargs['k']))
    except:
        pass
    try:
        kwargs['nu']
        return(kwargs['D']**2 * kwargs['mu'] * kwargs['u'] * kwargs['cp'] / (kwargs['L']*kwargs['k']*kwargs['nu']))
    except:
        pass
    return(kwargs['D']*kwargs['Re']*kwargs['Pr']/kwargs['L'])

def graetzInfo():
    print('arguments are D, rho, u, cp, L, k OR D, mu, u, cp, L, k, nu OR D, Re, Pr, L')

def grashoff(**kwargs):
    if (kwargs['idealGas']==True): #if an ideal gas then use beta = 1/T_avg approximation
        return(kwargs['g']*(1/((kwargs['Ts']+kwargs['Tinf'])/2)*(kwargs['Ts']-kwargs['Tinf'])*kwargs['L']**3/kwargs['nu']**2))
    else:
        return(kwargs['g']*kwargs['beta']*(kwargs['Ts']-kwargs['Tinf'])*kwargs['L']**3/kwargs['nu']**2)

def grashoffInfo():
    print('arguments are g(m/s^2), Ts(K), Tinf(K), L(m), nu(m^2/s), idealGas=True OR g(m/s^2), beta(K^-1), Ts(K), Tinf(K),'
    ' L(m), nu(m^2/s), idealGas=False')

def nusselt(**kwargs):
    return(kwargs['h']*kwargs['k']/kwargs['L'])

def nusseltInfo():
    print('arguments are h, k, L')

def peclet(**kwargs):
    try:
        kwargs['Re']
        return(kwargs['Re']*kwargs['Pr'])
    except:
        pass
    try:
        kwargs['alpha']
        return(kwargs['L']*kwargs['u']/kwargs['alpha'])
    except:
        pass
    return(kwargs['L']*kwargs['u']*kwargs['rho']*kwargs['cp']/kwargs['k'])

def pecletInfo():
    print('arguments are Re, Pr OR L, u, alpha, OR L, u, rho, cp, k')

def rayleigh(**kwargs):
    try:
        kwargs['Gr']
        return(kwargs['Gr']*kwargs['Pr'])
    except:
        return(kwargs['g']*kwargs['beta']*(kwargs['Ts']-kwargs['Tinf'])*kwargs['L']**3/(kwargs['nu']*kwargs['alpha']))

def rayleighInfo():
    print('arguments are Gr, Pr OR g, beta, Ts, Tinf, L, nu, alpha')

def prandtl(**kwargs):
    try:
        kwargs['alpha']
        return(kwargs['nu']/kwargs['alpha'])
    except:
        return(kwargs['cp']*kwargs['mu']/kwargs['k'])

def prandtlInfo():
    print('arguments are nu, alpha OR cp, mu, k')

def reynolds(**kwargs):
    try:
        kwargs['rho']
        return(kwargs['rho']*kwargs['u']*kwargs['L']/kwargs['mu'])
    except:
        return(kwargs['u']*kwargs['L']/kwargs['nu'])

def reynoldsInfo():
    print('arguments are rho, u, L, mu OR u, L, nu')

def thermalDiffusivity(**kwargs):
    return(kwargs['k']/(kwargs['rho']*kwargs['cp']))

def thermalDiffusivityInfo():
    print('arguments are k, rho, cp')
