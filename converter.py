def GravitationalPotential(Mass,Height,Grav):
    GPE = Mass*Height*Grav
    return(GPE)
def KineticEnergy(Mass,Velocity):
    KE = Mass*Velocity*Velocity*0.5
    return(KE)
def Power(Time,Power):
    P = Power/Time
    return(P)