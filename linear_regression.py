#!/usr/bin/python3

from visual import display

# import display_data
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Automatic data import wiht panda
data = pd.read_csv('data.csv')
df = pd.DataFrame(data)
km = df["km"]
km_values = df["km"]
price = df["price"]
price_values = df["price"]
km_size = km.index.stop
km_min = km.min()
km_max = km.max()
price_max = 0
price_min = 0
print( "\n", "km_max : ", km_max,
    "\n","km_min : ", km_min,
        "\n",
        "\n",
        "\n")


theta = pd.read_csv('theta.csv')
theta_f = pd.DataFrame(theta)
print(theta_f)
theta_0 = theta_f.loc[theta_f.index[-1], 'theta0']
print(f'theta0 : {theta_0}')
theta_1 = theta_f.loc[theta_f.index[-1], "theta1"]
print(f'theta1 : {theta_1}')



def save_thetas(theta_0, theta_1):
    f = open("theta.csv", "a+")
    f.write("\n%f, %f" % (theta_0, theta_1))
    f.close()


# Perform linear reg a certain number (range)
for i in range(0, 1):
    print(km.index.stop)
    estimate_price = (km * theta_1) + theta_0
    calc2 = estimate_price - price
    calc = (estimate_price - price) * km
    print(f' estimate_price {estimate_price}')
    print(f' calc {calc}')
    learning_rate = 0.3
    dt0 = 0
    dt1 = 0
    for km, price in zip(km, price):
        dt0 += (theta_1 * km + theta_0) - price
        dt1 += ((theta_1 * km + theta_0) - price) * km
    theta_0 -= dt0 / km_size * learning_rate
    theta_1 -= dt1 / km_size * learning_rate
    #theta_0 = learning_rate * ((1 / (estimate_price.size)) * calc2.sum())
    #theta_1 = learning_rate * ((1 / (estimate_price.size)) * calc.sum())
    print(f'nbr = {estimate_price.size}')
    print(f'new theta0 = {theta_0}')
    print(f'new theta1 = {theta_1}')
    print(f'nombre de fois : {i + 1}')
    save_thetas(theta_0, theta_1)

display(theta_0, theta_1, km_values, price_values, km_min, km_max)
