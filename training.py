#!/usr/bin/python3

import pandas
import numpy as math
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

theta = pandas.read_csv('base_theta.csv')
theta_frame = pandas.DataFrame(theta)
theta_frame_index = theta_frame.index
print("\n",theta_frame)
print("\n",theta_frame_index)

theta_0 = theta_frame.loc[theta_frame.index[-1], 'theta0']
print(f'\ntheta0 : {theta_0}')

theta_1 = theta_frame.loc[theta_frame.index[-1], "theta1"]
print(f'\ntheta1 : {theta_1}')


def save_thetas(theta_0, theta_1):
    print(f'\ntheta0 : {theta_0}')
    print(f'\ntheta1 : {theta_1}')
    f = open("theta.csv", "a+")
    f.write("\n%f, %f" % (theta_0, theta_1))
    f.close()


for i in range(0, 10):
    print(km_size)
    estimate_price = (kilometers * theta_1) + theta_0
    calc2 = estimate_price - prices
    calc = (estimate_price - prices) * kilometers
    # print(f'\n estimate_price {estimate_price}')
    # print(f'\n calc {calc}')
    learning_rate = 0.3
    dt0 = 0
    dt1 = 0
    for kilometer, price in zip(kilometers, prices):
        estimate_price = linear_function(theta_1, theta_0, float(kilometer))
        # print(f'\n estimate_price {estimate_price}')
        dt0 += (theta_1 * kilometer + theta_0) - price
        dt1 += ((theta_1 * kilometer + theta_0) - price) * kilometer
    theta_0 -= dt0 / km_size * learning_rate
    theta_1 -= dt1 / km_size * learning_rate
    #theta_0 = learning_rate * ((1 / (estimate_price.size)) * calc2.sum())
    #theta_1 = learning_rate * ((1 / (estimate_price.size)) * calc.sum())
    print(f'\nnbr = {estimate_price.size}')
    print(f'\nnew theta0 = {theta_0}')
    print(f'\nnew theta1 = {theta_1}')
    print(f'\nnombre de fois : {i + 1}')
    save_thetas(theta_0, theta_1)
