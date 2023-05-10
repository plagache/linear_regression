#!/usr/bin/python3

import matplotlib.pyplot as graph
import pandas
import numpy as math
# from training import denormalized_value
from linear_function import linear_function
import matplotx
import os
import imageio


data = pandas.read_csv('data.csv')
data_frame = pandas.DataFrame(data)
x_values = data_frame["km"]
y_values = data_frame["price"]
x_min = x_values.min()
x_max = x_values.max()


thetas = pandas.read_csv('thetas.csv')
thetas_frame = pandas.DataFrame(thetas)
theta_0 = thetas_frame["theta0"].values[-1]
theta_1 = thetas_frame["theta1"].values[-1]
thetas_size = thetas_frame["theta0"].count()


def ploting(theta_0, theta_1, xs, ys, x_min, x_max, name):
    
    graph.style.use(matplotx.styles.dracula)
    # graph.style.use(matplotx.styles.onedark)
    # graph.style.use(matplotx.styles.gruvbox["dark"])
    nombre_point_tracer = 10
    
    # Prepare Data to be Display data on matplotlib
    x = math.linspace(x_min, x_max, nombre_point_tracer)
    y = x * theta_1 + theta_0
    # Actually display the Data
    graph.plot(x, y, "g", label=name)
    # graph.plot()
    graph.scatter(xs, ys)
    
    linear = math.linspace(x_min, x_max, nombre_point_tracer)
    model = math.polyfit(x_values, y_values, 1)
    graph.plot(linear, linear * model[0] + model[1], "r:.", label='Polyfit')

    graph.xlabel('km')
    graph.ylabel('price')
    graph.legend()
    # graph.show()


# def ploting_example():
#     model = math.polyfit(x_values, y_values, 1)
#     ploting(model[1], model[0], x_values, y_values, x_min, x_max, "polyfit example")
#
#
# ploting_example()

filenames = []
for index in range(0,thetas_size):

    theta_0 = thetas_frame["theta0"].values[index]
    theta_1 = thetas_frame["theta1"].values[index]
    ploting(theta_0, theta_1, x_values, y_values, x_min, x_max, "Last trained Thetas")
    
    # create file name and append it to a list
    filename = f'png/{index}.png'
    filenames.append(filename)
    
    # save frame
    graph.savefig(filename)
    graph.close()

    # build gif
with imageio.get_writer('Training.gif', mode='I') as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)
    writer.close
        
# Remove files
for filename in set(filenames):
    os.remove(filename)

ploting(theta_0, theta_1, x_values, y_values, x_min, x_max, "Last trained Thetas")
