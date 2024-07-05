import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

data_path = 'results.npy'

data = np.load(data_path)

fig, ax = plt.subplots()
line, = ax.plot([], [])

def animation_init_temperature():
    ax.set(title='Temperature distribution', xlabel='x [m]', ylabel='T [K]'
           , xlim=(0, 0.1), ylim=(273, 373))
    return line,

def animation_function_temperature(i):
    x = data[i,0,:]
    T = data[i,1,:]
    line.set_data(x, T)
    ax.set_title(f'Temperature distribution, Time step: {i}')
    return line,

def animation_init_theta():
    ax.set(title='Theta distribution', xlabel='x [m]', ylabel='Theta [-]'
           , xlim=(0, 0.1), ylim=(0, 1))
    return line,

def animation_function_theta(i):
    x = data[i,0,:]
    theta = data[i,2,:]
    line.set_data(x, theta)
    ax.set_title(f'Theta distribution, Time step: {i}')
    return line,

anim_temperature = FuncAnimation(fig, animation_function_temperature, init_func=animation_init_temperature, frames=data.shape[0], interval=50,blit=True)
anim_temperature.save('temperature_animation.gif', writer='pillow', fps=30)

anim_theta = FuncAnimation(fig, animation_function_theta, init_func=animation_init_theta, frames=data.shape[0], interval=50,blit=True)
anim_theta.save('theta_animation.gif', writer='pillow', fps=30)