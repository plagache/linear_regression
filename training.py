#!/usr/bin/python3

import pandas
from linear_function import linear_function


data = pandas.read_csv('data.csv')

data_frame = pandas.DataFrame(data)

# print(data_frame)

x_values = data_frame["km"]

y_values = data_frame["price"]

data_set_size = x_values.count()
# print( "\nData set size : ", data_set_size)

x_min = x_values.min()
# print("\nX min:", x_min)
y_min = y_values.min()
# print("\nY min:", y_min)
x_max = x_values.max()
# print("\nX max:", x_max)
y_max = y_values.max()
# print("\nY max:", y_max)


def get_normalised_list(given_list, min, max):
    normalized_list = []
    for index, (element) in enumerate(given_list, start = 0):
        normalized_value = (element - min) / (max - min)
        normalized_list.append(normalized_value)
    return normalized_list


def normalisation(x_values, y_values):
    x_normalised = get_normalised_list(x_values, x_min, x_max)
    y_normalised = get_normalised_list(y_values, y_min, y_max)
    matrix = pandas.DataFrame({"xs":x_normalised, "ys":y_normalised})
    return matrix


normalize_matrix = normalisation(x_values, y_values)
xs = normalize_matrix["xs"]
ys = normalize_matrix["ys"]
# print("\nNormalized Matrix : ----------\n", normalize_matrix)


def denormalized_value(value, min_value, max_value):
    return (value * (max_value - min_value)) + min_value


def denormalize_data(normalized_data, min_value, max_value):
    denormalized_data = []
    for value in normalized_data:
        denormalized_data.append(denormalized_value(value, min_value, max_value))
    return denormalized_data


def denormalization(normalize_matrix):
    x_normalised = normalize_matrix["xs"]
    denormalize_x = denormalize_data(x_normalised, x_min, x_max)
    y_normalised = normalize_matrix["ys"]
    denormalize_y = denormalize_data(y_normalised, y_min, y_max)
    denormalized_matrix = pandas.DataFrame({"km":denormalize_x, "price":denormalize_y})
    return denormalized_matrix


denormalized_matrix = denormalization(normalize_matrix)
# print("\nDenormalized Matrix : ----------\n", denormalized_matrix)


def denormalization_thetas(normalized_theta_0, normalized_theta_1):

    y_mean = y_values.sum() / data_set_size
    # y_mean = (1 / data_set_size) * sum(y_values)
    # x_mean = (1 / data_set_size) * sum(x_values)
    x_mean = x_values.sum() / data_set_size

    y_range = y_max - y_min
    x_range = x_max - x_min

    range_ratio = y_range / x_range
    # print("\nrange ratio =", range_ratio)

    d_theta_1 = normalized_theta_1 * range_ratio
    # print("\ntheta_1 = ", theta_1)

    # graph 1 rapport de la normalized distance + la moyenne
    # part_theta_0 = (normalized_theta_0 * range_ratio + y_mean)
    # print ("\nPart theta_0 = ", part_theta_0)
    # graph 2 rapport de la normalized distance + la moyenne
    # part_theta_1 = d_theta_1 * x_mean
    # print ("\nPart theta_1 = ", part_theta_1)

    d_theta_0 = (normalized_theta_0 * range_ratio + y_mean) - (d_theta_1 * x_mean)
    # print("\ntheta_0 = ", d_theta_0)


    return d_theta_0, d_theta_1


def save_thetas(theta_0, theta_1):
    # print(f'\nSaved theta0 : {theta_0}')
    # print(f'\nSaved theta1 : {theta_1}')
    f = open("thetas.csv", "a+")
    f.write("%f, %f\n" % (theta_0, theta_1))
    f.close()


def get_thetas():
    thetas = pandas.read_csv('thetas.csv')
    thetas_frame = pandas.DataFrame(thetas)
    theta_0 = thetas_frame["theta0"].values[-1]
    theta_1 = thetas_frame["theta1"].values[-1]
    return theta_0, theta_1


def gradient_descent(theta_0, theta_1):

    # total = 2000;
    # learning_rate = 0.2
    total = 100;
    learning_rate = 1

    for i in range(0, total):

        sum_loss_y = 0
        sum_loss_x = 0

        for x, y in zip(xs, ys):

            estimate = linear_function(theta_1, theta_0, float(x))

            # loss function represent the error of our model
            # and is the difference between the estimation of our model and the actual data
            loss_y = estimate - y
            loss_x = (estimate - y) * x

            sum_loss_y = sum_loss_y + loss_y
            sum_loss_x = sum_loss_x + loss_x

        # cost function is the average loss for the entire training data_set
        gradient_theta_0 = sum_loss_y / data_set_size
        gradient_theta_1 = sum_loss_x / data_set_size

        # this update the theta
        theta_0 -= learning_rate * gradient_theta_0
        theta_1 -= learning_rate * gradient_theta_1

        dt0, dt1 = denormalization_thetas(theta_0, theta_1)
        save_thetas(dt0, dt1)

    return denormalization_thetas(theta_0, theta_1)


base_theta_0, base_theta_1 = get_thetas()

dt0, dt1 = gradient_descent(base_theta_0, base_theta_1)

print("\nlast denormalized theta 0 =", dt0)
print("\nlast denormalized theta 1 =", dt1)
