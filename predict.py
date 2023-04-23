#! /usr/bin/python3
import pandas  as pd
from linear_regression import estimate_price

theta = pd.read_csv('theta.csv')
theta_f = pd.DataFrame(theta)
theta_0 = theta_f["theta0"].values[-1]
theta_1 = theta_f["theta1"].values[-1]

km = float(input("Enter your mileage: "))

print(estimate_price(km, theta_0, theta_1))
