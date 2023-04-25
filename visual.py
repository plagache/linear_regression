# import display_data
import matplotlib.pyplot as plt
import numpy as np

def display(theta_0, theta_1, km, price, km_min, km_max):
    
    # print(theta_0, km_max, km)
    plt.style.use('dark_background')
    nbr_point_tracer = 2
    
    # Prepare Data to be Display data on matplotlib
    linear = np.linspace(km_min, km_max, nbr_point_tracer)
    # Actually display the Data
    plt.plot(linear, linear * theta_1 + theta_0, label='ft_linear', c='r')
    plt.scatter(km, price)
    
    # add some Title to the display
    model = np.polyfit(km, price, 1)
    print(f'ours t0:{theta_0} t1:{theta_1}\nmodel t0:{model[1]} t1:{model[0]}')
    plt.plot(linear, linear * model[0] + model[1], label='polyfit', ls='--', c='g')
    plt.xlabel('km')
    plt.ylabel('price')
    plt.legend()
    plt.show()
