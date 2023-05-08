#!/usr/bin/python3

import pandas
# import numpy as math
from linear_function import linear_function


data = pandas.read_csv('data.csv')

data_frame = pandas.DataFrame(data)

x = data_frame["km"]
kilometers = x

y = data_frame["price"]
prices = y

km_size = kilometers.index.stop
data_size = km_size
km_min = kilometers.min()
km_max = kilometers.max()
print( "\nkm size : ", km_size)
print( "\nkm_min : ", km_min)
print( "\nkm_max : ", km_max)

price_max = 0
price_min = 0


def save_thetas(theta_0, theta_1):
    print(f'\nSaved theta0 : {theta_0}')
    print(f'\nSaved theta1 : {theta_1}')
    f = open("theta.csv", "a+")
    f.write("\n%f, %f" % (theta_0, theta_1))
    f.close()


for i in range(0, 100):

    learning_rate = 0.000000001

    # u = 1;

    sum_loss_price = 0;
    sum_loss_mileage = 0;

    theta = pandas.read_csv('theta.csv')
    theta_frame = pandas.DataFrame(theta)
    theta_frame_index = theta_frame.index
    theta_0 = theta_frame.loc[theta_frame.index[-1], 'theta0']
    theta_1 = theta_frame.loc[theta_frame.index[-1], "theta1"]

    print(f'\ntheta0 : {theta_0}')
    print(f'\ntheta1 : {theta_1}')

    tmp_theta_0 = theta_0
    tmp_theta_1 = theta_1

    for kilometer, price in zip(kilometers, prices):

        estimate_price = linear_function(theta_1, theta_0, float(kilometer))

        # loss function represent the error of our model
        # and is the difference between the estimation of our model and the actual data
        loss_price = estimate_price - price

        sum_loss_price = sum_loss_price + loss_price;
        sum_loss_mileage = sum_loss_mileage + loss_price * kilometer
        # print(f'\n price difference : {diff_price}')
        # print(f'\n estimate_price {estimate_price}')
        # estimate_price_sum =
        # print("\n u :", u)
        # u = u + 1;

    print(f'\n somme Price difference : {sum_loss_price}')
    print(f'\n somme Mileage difference : {sum_loss_mileage}')

    # cost function is the average loss for the entire training data_set
    cost_price = sum_loss_price * (1 / data_size)
    cost_mileage = sum_loss_mileage * (1 / data_size)
    print(f'\n cost Price difference : {cost_price}')
    print(f'\n cost Mileage difference : {cost_mileage}')

    tmp_theta_0 -= learning_rate * (1 / data_size) * sum_loss_price
    tmp_theta_1 -= learning_rate * ( 1 / data_size) * sum_loss_mileage
    print(f'\nnombre de fois : {i + 1}')
    save_thetas(tmp_theta_0, tmp_theta_1)
