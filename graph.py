#!/usr/bin/python3

import matplotlib.pyplot as graph
import pandas
import numpy as math
# from training import denormalized_value
from linear_function import linear_function

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

thetas = pandas.read_csv('thetas.csv')
thetas_frame = pandas.DataFrame(thetas)
theta_frame_index = thetas_frame.index
print("\n",thetas_frame)
print("\n",theta_frame_index)

theta_0 = thetas_frame.loc[thetas_frame.index[-1], 'theta0']
print(f'\ntheta0 : {theta_0}')

theta_1 = thetas_frame.loc[thetas_frame.index[-1], "theta1"]
print(f'\ntheta1 : {theta_1}')

def ploting(theta_0, theta_1, xs, ys, x_y_min, x_y_max):
    
    # print("\n", theta_0, km_max, x)
    graph.style.use('dark_background')
    nombre_point_tracer = 10
    
    # Prepare Data to be Display data on matplotlib
    linear = math.linspace(x_y_min, x_y_max, nombre_point_tracer)
    x = math.linspace(x_y_min, x_y_max, nombre_point_tracer)
    y = x * theta_1 + theta_0
    # Actually display the Data
    # graph.plot(linear, linear * theta_1 + theta_0, label='linear')
    graph.plot(x, y, label='linear')
    graph.plot()
    graph.scatter(xs, ys)
    
    model = math.polyfit(xs, ys, 1)
    graph.plot(linear, linear * model[0] + model[1], label='model')
    print("\nModel [0]", model[0])
    print("\nModel [1]", model[1])
    graph.xlabel('km')
    graph.ylabel('price')
    graph.legend()
    graph.show()

ploting(theta_0, theta_1, kilometers, prices, km_min, km_max)
