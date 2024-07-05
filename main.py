from setup import *
import numpy as np

##initiate fields
x_arr = np.linspace(0, length, N_x)
T_arr = np.ones(N_x) * T_initial
T_arr[0] = T_boundary

rho_arr = np.ones(N_x) * rho_s
lambda_arr = np.ones(N_x) * lambda_s
theta_arr = np.zeros(N_x)

CA_arr = np.zeros(N_x)
for i in range(N_x):
    CA_arr[i] = CA_func(T_arr[i], theta_arr[i])

result = np.array([[x_arr,T_arr,theta_arr]])

# for i in range(N_t-1):
#     result = np.append(result,[[x_arr,T_arr,theta_arr]],axis=0)

print(CA_arr[0])

T_next = np.zeros(N_x)
i= 0
##main loop
while theta_arr[-2] < 1:
    if i > 100:
        break
    
    theta_next = np.zeros(N_x)
    for j in range(1, N_x - 1):
        T_next[j] = T_arr[j] + delta_t/CA_arr[j] * ( (lambda_l - lambda_s) * derivative_theta_l_T(T_arr[j]) * ((T_arr[j+1]-T_arr[j-1])/(2*delta_x))**2 + lambda_arr[j] * (T_arr[j+1] + T_arr[j-1] - 2*T_arr[j])/delta_x**2)
    T_next[-1] = T_next[-2]

    #set for next iteration
    for j in range(0, N_x):
        theta_next[j] = theta_l_func(T_next[j])
    for j in range(0, N_x):
        CA_arr[j] = CA_func(T_next[j], theta_next[j])

    lambda_arr = lambda_func(theta_next)
    
    #append to result
    result = np.append(result, [[x_arr, T_next, theta_next]],axis=0)

    #set for next iteration
    T_arr,T_next = T_next,T_arr
    theta_arr,theta_next = theta_next,theta_arr
    i += 1
    print('next')

print(result.shape)

np.save('results', result)