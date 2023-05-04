#! /usr/bin/python3

import pandas  as pd
from linear_function import linear_function


theta = pd.read_csv('theta.csv')
theta_f = pd.DataFrame(theta)
theta_0 = theta_f.loc[theta_f.index[-1], 'theta0']
theta_1 = theta_f.loc[theta_f.index[-1], 'theta1']
print("Theta 0 = ", theta_0, "\nTheta 1 = ", theta_1, sep='', end='\n')


kilometer = input("\nEnter your mileage: ")


try:
    estimate_price = linear_function(theta_1, theta_0, float(kilometer))
    print(estimate_price)
except:
    print("\nError in detecting your mileage.")
    exit()
