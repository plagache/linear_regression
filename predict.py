#! /usr/bin/python3

import pandas  as pd

theta = pd.read_csv('theta.csv')

theta_f = pd.DataFrame(theta)


theta_0 = theta_f.loc[theta_f.index[-1], 'theta0']
theta_1 = theta_f.loc[theta_f.index[-1], 'theta1']

print("Theta 0 = ", theta_0, "\nTheta 1 = ", theta_1, sep='', end='\n')

km = input("Enter your mileage: ")

estimate_Price = theta_0 + ( theta_1 * float(km))

print(estimate_Price)
