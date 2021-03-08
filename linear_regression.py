#! /usr/bin/python3

# import display_data
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Automatic data import wiht panda
data = pd.read_csv('data.csv')
df = pd.DataFrame(data)
km = df["km"]
price = df["price"]
print(km)

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
    estimate_price = (km * theta_1) + theta_0
    calc2 = estimate_price - price
    calc = (estimate_price - price) * km
    print(f' estimate_price {estimate_price}')
    print(f' calc {calc}')

    learning_rate = 0.3

    theta_0 = learning_rate * ((1 / (estimate_price.size)) * calc2.sum())
    theta_1 = learning_rate * ((1 / (estimate_price.size)) * calc.sum())
    print(f'nbr = {estimate_price.size}')
    print(f'new theta0 = {theta_0}')
    print(f'new theta1 = {theta_1}')
    print(f'nombre de fois : {i + 1}')
    save_thetas(theta_0, theta_1)


nbr_point_tracer = 2

# Prepare Data to be Display data on matplotlib
linear = np.linspace(min(km), max(km), nbr_point_tracer)
fig, yx = plt.subplots()
# Actually display the Data
yx.plot(linear, linear * theta_1 + theta_0, label='linear')
yx.scatter(km, price)

# add some Title to the display
yx.set_xlabel(f'km')
yx.set_ylabel(f'price')
yx.set_title('Graph')
yx.legend()
plt.show()
