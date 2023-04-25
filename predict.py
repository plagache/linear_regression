#! /usr/bin/python3
import pandas  as pd
from tools import import_thetas, estimate_price

km = float(input("Enter your mileage: "))

theta_0, theta_1 = import_thetas()

price = estimate_price(km, theta_0, theta_1)

print(f"estimated price is: {price}")
