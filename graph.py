#!/usr/bin/python3

import matplotlib.pyplot as graph
import pandas
import numpy as math
# from training import denormalized_value
from linear_function import linear_function


data = pandas.read_csv('data.csv')
data_frame = pandas.DataFrame(data)
x_values = data_frame["km"]
y_values = data_frame["price"]
x_min = x_values.min()
x_max = x_values.max()


thetas = pandas.read_csv('thetas.csv')
thetas_frame = pandas.DataFrame(thetas)
theta_frame_index = thetas_frame.index
theta_0 = thetas_frame.loc[thetas_frame.index[-1], 'theta0']
theta_1 = thetas_frame.loc[thetas_frame.index[-1], "theta1"]


def ploting(theta_0, theta_1, xs, ys, x_min, x_max, name):
    
    graph.style.use('dark_background')
    nombre_point_tracer = 10
    
    # Prepare Data to be Display data on matplotlib
    x = math.linspace(x_min, x_max, nombre_point_tracer)
    y = x * theta_1 + theta_0
    # Actually display the Data
    graph.plot(x, y, label=name)
    graph.plot()
    graph.scatter(xs, ys)
    
    linear = math.linspace(x_min, x_max, nombre_point_tracer)
    model = math.polyfit(x_values, y_values, 1)
    graph.plot(linear, linear * model[0] + model[1], label='Polyfit')

    graph.xlabel('km')
    graph.ylabel('price')
    graph.legend()
    graph.show()


# def ploting_example():
#     model = math.polyfit(x_values, y_values, 1)
#     ploting(model[1], model[0], x_values, y_values, x_min, x_max, "polyfit example")
#
#
# ploting_example()


ploting(theta_0, theta_1, x_values, y_values, x_min, x_max, "My linear")
