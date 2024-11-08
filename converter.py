def GravitationalPotential(Mass,Height,Grav):
    GPE = Mass*Height*Grav
    return(GPE)
def KineticEnergy(Mass,Velocity):
    KE = Mass*Velocity*Velocity*0.5
    return(KE)
def PowerPT(Time,Power):
    P = Power/Time
    return(P)
def ElasticPotential(SpringConstant,Extension):
    EP = SpringConstant*Extension*Extension*0.5
    return(EP)
def ChangeInThermalEnergy(Mass,SHC,Change):
    CITE = Mass*SHC*Change
    return(CITE)
def ChargeFlow(Current,Time):
    CF = Current*Time
    return(CF)
def PotentialDifference(Current,Resistance):
    PD = Current*Resistance
    return(PD)
def PowerCPD(Current,PotentialDifference):
    P = Current*PotentialDifference
    return(P)
def PowerCR(Current,Resistance):
    P = Current*Current*Resistance
    return(P)
def EnergyTransferedPT(Power,Time):
    ET = Power*Time
    return(ET)
def EnergyTransferedCFPD(Current,PotentialDifference):
    ET = Current*PotentialDifference
    return(ET)
def Density(Volume,Mass):
    D = Volume*Mass
    return(D)
def ThermalEnergyForAChangeInState(Mass,SpecificLatentHeat):
    TEFACIS = Mass*SpecificLatentHeat
    return(TEFACIS)
def GasPressureConstant(Pressure,Volume):
    GPC = Pressure*Volume
    return(GPC)
def WaveSpeed(WaveLength,Frequency):
    WS = WaveLength*Frequency
    return(WS)
def TimePeriod(Frequency):
    TP = 1/Frequency
    return(TP)
def Magnification(ImageHeight,ObjectHeight):
    M = ImageHeight/ObjectHeight
    return(M)
def MagnetForce(MagneticFluxDensity,Current,LengthOfConductorInMagneticFeild):
    MF = MagneticFluxDensity*Current*LengthOfConductorInMagneticFeild
    return(MF)