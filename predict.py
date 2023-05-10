#! /usr/bin/python3

import pandas
from linear_function import linear_function


thetas = pandas.read_csv('thetas.csv')
thetas_frame = pandas.DataFrame(thetas)
theta_0 = thetas_frame["theta0"].values[-1]
theta_1 = thetas_frame["theta1"].values[-1]


print("Theta 0 = ", theta_0, "\nTheta 1 = ", theta_1, sep='', end='\n')


kilometer = input("\nEnter your mileage: ")


try:
    estimate_price = linear_function(theta_1, theta_0, float(kilometer))
    print(estimate_price)
except:
    print("\nError in detecting your mileage.")
    exit()
