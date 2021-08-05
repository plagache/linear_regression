# import display_data
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def display(theta_0, theta_1, km, price, km_min, km_max):
    
    print(theta_0, km_max, km)
    plt.style.use('dark_background')
    nbr_point_tracer = 2
    
    # Prepare Data to be Display data on matplotlib
    linear = np.linspace(km_min, km_max, nbr_point_tracer)
    # Actually display the Data
    #plt.plot(linear, linear * theta_1 + theta_0, label='linear')
    plt.plot()
    plt.scatter(km, price)
    
    # add some Title to the display
    model = np.polyfit(km, price, 1)
    print(model)
    plt.plot(linear, linear * model[0] + model[1], label='model')
    plt.xlabel('km')
    plt.ylabel('price')
    plt.legend()
    plt.show()
