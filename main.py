import setup
import numpy as np

##initiate fields
x_arr = np.linspace(0, setup.length, setup.N_x)
T_arr = np.ones(setup.N_x) * setup.T_initial
rho_arr = np.ones(setup.N_x) * setup.rho_s
lambda_arr = np.ones(setup.N_x) * setup.lambda_s
theta_arr = np.zeros(setup.N_x)
CA_arr = np.zeros(setup.N_x)

result = np.array([[x_arr,T_arr,theta_arr]])

for i in range(setup.N_t-1):
    result = np.append(result,[[x_arr,T_arr,theta_arr]],axis=0)

while theta_arr[-1]<1:
    T_arr = setup.T_initial + (setup.T_boundary - setup.T_initial) * x_arr / setup.length
    theta_arr = np.array([setup.theta_l_func(T) for T in T_arr])
    CA_arr = np.array([setup.CA_func(T,theta_l) for T,theta_l in zip(T_arr,theta_arr)])
    lambda_arr = np.array([setup.lambda_func(theta_l) for theta_l in theta_arr])
    rho_arr = np.array([setup.rho_func(theta_l) for theta_l in theta_arr])
    T_arr_new = np.zeros(setup.N_x)
    for j in range(1,setup.N_x-1):
        T_arr_new[j] = T_arr[j] + setup.delta_T * (lambda_arr[j] * (T_arr[j+1] - 2 * T_arr[j] + T_arr[j-1]) / setup.delta_x**2 - CA_arr[j] * (T_arr[j] - setup.T_ref)) / (rho_arr[j] * setup.delta_x)
    T_arr = T_arr_new
    result = np.append(result,[[x_arr,T_arr,theta_arr]],axis=0)

    

# np.save('results', result)