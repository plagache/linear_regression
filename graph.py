#!/usr/bin/python3

import matplotlib.pyplot as graph
import pandas
import numpy as math

data = pandas.read_csv('data.csv')

data_frame = pandas.DataFrame(data)

x = data_frame["km"]
kilometers = x

y = data_frame["price"]
prices = y

km_size = kilometers.index.stop
km_min = kilometers.min()
km_max = kilometers.max()
print( "\nkm_min : ", km_min)
print( "\nkm_max : ", km_max)

price_max = 0
price_min = 0

theta = pandas.read_csv('base_theta.csv')
theta_frame = pandas.DataFrame(theta)
theta_frame_index = theta_frame.index
print("\n",theta_frame)
print("\n",theta_frame_index)

theta_0 = theta_frame.loc[theta_frame.index[-1], 'theta0']
print(f'\ntheta0 : {theta_0}')

theta_1 = theta_frame.loc[theta_frame.index[-1], "theta1"]
print(f'\ntheta1 : {theta_1}')

def plot(theta_0, theta_1, x, y, x_y_min, x_y_max):
    
    print("\n", theta_0, km_max, x)
    graph.style.use('dark_background')
    nombre_point_tracer = 2
    
    # Prepare Data to be Display data on matplotlib
    linear = math.linspace(x_y_min, x_y_max, nombre_point_tracer)
    # Actually display the Data
    graph.plot(linear, linear * theta_1 + theta_0, label='linear')
    graph.plot()
    graph.scatter(x, y)
    
    # add some Title to the display
    model = math.polyfit(x, y, 1)
    print(model)
    graph.plot(linear, linear * model[0] + model[1], label='model')
    graph.xlabel('km')
    graph.ylabel('price')
    graph.legend()
    graph.show()

plot(theta_0, theta_1, kilometers, prices, km_min, km_max)
