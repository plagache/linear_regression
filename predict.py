#! /usr/bin/python3

import pandas  as pd

theta = pd.read_csv('theta.csv')
theta_f = pd.DataFrame(theta)
theta_0 = theta_f.loc[theta_f.index[-1], 'theta0']
theta_1 = theta_f.loc[theta_f.index[-1], "theta1"]
print(theta_0)

km = input("Enter your mileage: ")

print(theta_0[0] + theta_1[0] * float(km))
