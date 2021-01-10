#! /usr/bin/python3

# import display_data
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('data.csv')
df = pd.DataFrame(data)

theta = pd.read_csv('theta.csv')
theta_f = pd.DataFrame(theta)
theta_0 = theta_f.loc[theta_f.index[-1], 'theta0']
theta_1 = theta_f.loc[theta_f.index[-1], "theta1"]


"""
Return the guess using hypothesis
"""


def estimate(mileage, t0, t1):
    return t0 + mileage * t1


"""
Return error on guess and guess
"""


def error(guess, price):
    ret = guess - price
    return (ret)


def batch(lr, t0, t1):
    data_nbr = data['km'].size
    data['guess'] = estimate(data['km'], t0, t1)
    data['error'] = error(data['guess'], data['price'])
    data['sqerror'] = data['error']**2
    data['meansqerror'] = data['sqerror'].sum() / data_nbr
    dt0 = lr * (1.0 / data_nbr) * data['error'].sum()
    dt1 = lr * (1.0 / data_nbr) * (data['error'] * data['km']).sum()
    t0 = t0 - dt0
    t1 = t1 - dt1
    # print(data['guess'])
    # print(data['meansqerror'])
    print(data['sqerror'])
    print("|t0= {} ||dt0= {}|".format(t0, dt0))
    print("|t1= {} ||dt1= {}|".format(t1, dt1))
    return (t0, t1, data['sqerror'].sum())


t1 = 0
t0 = 0
lr = 1e-10
turn = 20

t0s, t1s, errors = [], [], []
turns = [x for x in range(20)]
for i in range(turn):
    t0, t1, err = batch(lr, t0, t1)
    t0s.append(t0)
    t1s.append(t1)
    errors.append(err)

print(t0s)
print(t1s)
print(errors)
# list of t0 and t1 and error for each batch
# print on separate graph t0,t1,error as function of batch

plt.figure()
plt.scatter(data['km'], data['price'])
plt.plot(data['km'], data['guess'], 'r-')

plt.figure()
plt.scatter(turns, t0s, c='r', label="Theta0")
plt.figure()
plt.scatter(turns, t1s, c='g', label="theta1")
plt.figure()
plt.scatter(turns, errors, c='b', label="error")

plt.show()
