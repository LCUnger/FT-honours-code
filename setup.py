import numpy as np
import matplotlib.pyplot as plt

##constants of paraffine
lambda_l = 0.15 #thermal conductivity of liquid paraffine [W/mK]
lambda_s = 0.15 #thermal conductivity of solid paraffine [W/mK]
rho_l = 780 #density of liquid paraffine [kg/m^3]
rho_s = 860 #density of solid paraffine [kg/m^3]
c_l = 2100 #specific heat of liquid paraffine [J/kgK]
c_s = 2900 #specific heat of solid paraffine [J/kgK]
mu = 0.205 #dynamic viscosity of liquid paraffine [Pa s]
L = 2.1e5 #latent heat of paraffin [J/kg]
T_m = 54*273.15 #melting temperature of paraffin [K]

##constants of the system
length = 0.1 #length of the system [m]
T_initial = 293.15 #initial temperature of the system [K]

T_boundary = 373.15 #boundary temperature of the system [K]

##constants of the simulation
delta_T = 0.1 #temperature grid space [K]
delta_x = 0.001 #space grid space [m]
N_x = int(length//delta_x) #number of space grid
N_t = 100 #number of time steps
T_ref = T_m - delta_T #reference temperature


##set initial conditions


##support functions
def lambda_func(theta_l):
    return (1-theta_l)*lambda_s + theta_l*lambda_l

def rho_func(theta_l):
    return (1-theta_l)*rho_s + theta_l*rho_l

def theta_l_func(T):
    if T >= T_m + delta_T:
        return 1
    elif T <= T_m - delta_T:
        return 0
    else:
        return (T-T_m + delta_T)/(2*delta_T)
    

def derivative_theta_l_T(T):
    if (T >= T_m + delta_T) or (T <= T_m - delta_T):
        return 0
    else:
        return 1/(2*delta_T)

def CA_func(T,theta_l):
    theta_s = 1-theta_l
    return theta_s*rho_s*c_s + theta_l*rho_l*c_l + ((rho_l*c_l - rho_s*c_s)(T-T_ref) + rho_l*L)*derivative_theta_l_T(T)

