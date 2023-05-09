#!/usr/bin/python3

import pandas
# import numpy as math
from linear_function import linear_function
from graph import ploting


data = pandas.read_csv('data.csv')

data_frame = pandas.DataFrame(data)

# print(data_frame)

x_values = data_frame["km"]
kilometers = x_values

y_values = data_frame["price"]
prices = y_values

data_set_size = x_values.index.stop
# print( "\nData set size : ", data_set_size)

x_min = x_values.min()
# print("\nX min:", x_min)
y_min = y_values.min()
# print("\nY min:", y_min)
x_max = x_values.max()
# print("\nX max:", x_max)
y_max = y_values.max()
# print("\nY max:", y_max)

def save_thetas(theta_0, theta_1):
    # print(f'\nSaved theta0 : {theta_0}')
    # print(f'\nSaved theta1 : {theta_1}')
    f = open("theta.csv", "a+")
    f.write("\n%f, %f" % (theta_0, theta_1))
    f.close()


def get_normalised_list(given_list, min, max):
    normalized_list = []
    for index, (element) in enumerate(given_list, start = 0):
        normalized_value = (element - min) / (max - min)
        normalized_list.append(normalized_value)
    return(normalized_list)


def normalisation(x_values, y_values):
    x_normalised = get_normalised_list(x_values, x_min, x_max)
    y_normalised = get_normalised_list(y_values, y_min, y_max)
    matrix = pandas.DataFrame({"xs":x_normalised, "ys":y_normalised})
    # print("\nX normalized ------\n---------------\n", x_normalised)
    # print("\nX normalized ------\n---------------\n", x_normalised)
    # print("\nMatrix : ----------\n", matrix)
    return(matrix)


normalize_matrix = normalisation(x_values, y_values)
xs = normalize_matrix["xs"]
ys = normalize_matrix["ys"]
# print("\nNormalized Matrix : ----------\n", normalize_matrix)

def denormalized_value(value, min_value, max_value):
    return((value * (max_value - min_value)) + min_value)

def denormalize_data(normalized_data, min_value, max_value):
    denormalized_data = []
    for value in normalized_data:
        # denormalized_value = (value * (max_value - min_value)) + min_value
        denormalized_data.append(denormalized_value(value, min_value, max_value))
    return(denormalized_data)


def denormalization(normalize_matrix):
    x_normalised = normalize_matrix["xs"]
    denormalize_x = denormalize_data(x_normalised, x_min, x_max)
    y_normalised = normalize_matrix["ys"]
    denormalize_y = denormalize_data(y_normalised, y_min, y_max)
    denormalized_matrix = pandas.DataFrame({"km":denormalize_x, "price":denormalize_y})
    return(denormalized_matrix)

denormalized_matrix = denormalization(normalize_matrix)
# print("\nDenormalized Matrix : ----------\n", denormalized_matrix)


for i in range(0, 800):


    learning_rate = 0.3

    sum_loss_y = 0
    sum_loss_x = 0

    theta = pandas.read_csv('theta.csv')
    theta_frame = pandas.DataFrame(theta)
    theta_frame_index = theta_frame.index
    theta_0 = theta_frame.loc[theta_frame.index[-1], 'theta0']
    theta_1 = theta_frame.loc[theta_frame.index[-1], 'theta1']

    tmp_theta_0 = theta_0
    tmp_theta_1 = theta_1

    for x, y in zip(xs, ys):

        estimate = linear_function(theta_1, theta_0, float(x))

        # loss function represent the error of our model
        # and is the difference between the estimation of our model and the actual data
        loss_y = estimate - y

        sum_loss_y = sum_loss_y + loss_y
        sum_loss_x = sum_loss_x + loss_y * x

    # cost function is the average loss for the entire training data_set
    weighed_loss_y = sum_loss_y * (1 / data_set_size)
    weighed_loss_x = sum_loss_x * (1 / data_set_size)
    print(f'\nweighed loss y: {weighed_loss_y}')
    print(f'\nweighed loss x: {weighed_loss_x}')

    # this update the theta
    tmp_theta_0 -= learning_rate * weighed_loss_y
    # denormalized_theta_0 = denormalized_value(tmp_theta_0, y_min, y_max)
    # print(f'\nSaved theta0 : {denormalized_theta_0}')
    tmp_theta_1 -= learning_rate * weighed_loss_x
    # denormalized_theta_1 = denormalized_value(tmp_theta_1, x_min, x_max)
    # print(f'\nSaved theta1 : {denormalized_theta_1}')
    # save_thetas(denormalized_theta_0, denormalized_theta_1)
    save_thetas(tmp_theta_0, tmp_theta_1)


theta = pandas.read_csv('theta.csv')
theta_frame = pandas.DataFrame(theta)
theta_0 = theta_frame.loc[theta_frame.index[-1], 'theta0']
theta_0 = denormalized_value(theta_0, y_min, y_max)
print(f'\nlast theta 0 : {theta_0}')
theta_1 = theta_frame.loc[theta_frame.index[-1], "theta1"]
theta_1 = denormalized_value(theta_1, x_min, x_max)
print(f'\nlast theta 1 : {theta_1}')
# print("\nNormalized Matrix : ----------\n", normalize_matrix)
# print("\nxs : ----------\n", xs)
# print("\nys : ----------\n", ys)
# ploting(theta_0, theta_1, xs, ys, x_min, x_max)
ploting(theta_0, theta_1, x_values, y_values, x_min, x_max)
