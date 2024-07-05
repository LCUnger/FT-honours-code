import setup
import numpy as np

##initiate fields
x_arr = np.linspace(0, setup.length, setup.N_x)
T_arr = np.ones(setup.N_x) * setup.T_initial
rho_arr = np.ones(setup.N_x) * setup.rho_s
lambda_arr = np.ones(setup.N_x) * setup.lambda_s
theta_arr = np.zeros(setup.N_x)
CA_arr = np.zeros(setup.N_x)

result = np.array([[[x_arr,T_arr],[x_arr,theta_arr]]])


for i in range(setup.N_t-1):
    result = np.append(result,[[[x_arr,T_arr],[x_arr,theta_arr]]],axis=0)

np.save('results', result)