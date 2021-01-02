#! /usr/bin/python3

#import display_data
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('data.csv')
df = pd.DataFrame(data)

theta = pd.read_csv('theta.csv')
theta_f = pd.DataFrame(theta)
theta_0 = theta_f.loc[theta_f.index[-1], 'theta0']
theta_1 = theta_f.loc[theta_f.index[-1], "theta1"]

km = data.iloc[:, 0]
price = data.iloc[:, 1]

"""
Normalize km and price data see if LR can be raise
"""

"""
Return the guess using hypothesis
"""


def estimate(mileage, t0, t1):
    return t0 + mileage * t1


"""
Return error on guess and guess
"""


def error(mileage, t0, t1, price):
    guess = estimate(mileage, t0, t1)
    ret = guess - price
    return (ret, guess)


def one(mileage, price):
    t0 = 0
    t1 = 0
    LR = 0.0000000000005
    for i in range(1000):
        err, guess = error(mileage, t0, t1, price)

        dt0 = LR * (1 / mileage.size) * err.sum()
        dt1 = LR * (1 / mileage.size) * (err * km).sum()

        t0 = t0 - dt0
        t1 = t1 - dt1

        print('ERR=', err.sum())
    return(t0, t1)

t0, t1 = one(km, price)
print('t0', t0, 't1', t1)

fig, axs = plt.subplots(2)

#err, guess = error(km, 8500, -0.025, price)
err, guess = error(km, t0, t1, price)


axs[0].scatter(km, price)
axs[0].plot(km, guess, 'green')
axs[1].scatter(km, err**2)

plt.show()
exit(0)


"""
t0 = 0.0
t1 = 0.0

L = 0.0001
epochs = 1000
n = float(len(km))

for i in range(len(km)):
    price_estimate = t0 + t1 * km
    dt1 = (1/n) * sum(km * price_estimate - price)
    dt0 = (1/n) * sum(price_estimate - price)
    t1 = t1 + L * dt1
    t0 = t0 + L * dt0
    #print(price_estimate)
    #print(dt1, dt0)
    print(t1, t0)

plt.plot([min(km), max(km)], [min(price_estimate), max(price_estimate)], color='red')
plt.show()
exit(0)
def cost(km, t0, t1, price):
    print(type(km), type(price), type(t0), type(t1))
    size = float(df.size / 2.0)
    error = 0.0
    for i in range(size):
        error += km[i] * t1 + t0 - price[i]
    return error / size

cost(km,)

def gradientdecent(iteration, learningRate):
    T0 = 0.0
    T1 = 0.0
    size = float(df.size / 2.0)
    for cycle in range(1, iteration):
        for i in range(0, int(size)):
            kmi = float(df.loc[i, 'km'])
            pi = float(df.loc[i, 'price'])
            print("|||||" + str(i) + "|||||")
            guess = estimate(T0, kmi, T1)
            error = guess - pi
            print(guess, error)
            # print(type(kmi), type(pi))
            # print(type(guess), type(error), type(learningRate), type(df.size), df.size)
            dT0 = learningRate * error
            dT1 = learningRate * error * kmi
            print("dt", dT0, dT1, sep=' ')
            print("t", T0, T1, sep=' ')
            T0 = T0 - dT0
            T1 = T1 - dT1
            i += 1
        cycle += 1
        #print("T0 =",  theta_0, "T1=", theta_1)



gradientdecent(20, 0.00000001)
linear = np.linspace(23000, 240000, 2)
lin = np.linspace(0, 500, 100)
fig, yx = plt.subplots()
# Diplay
yx.plot(linear, linear * theta_1 + theta_0, label='linear')
plt.show()
exit(0)
def save_thetas(theta_0, theta_1):
        f = open("theta.csv", "a+")
        f.write("\n%f, %f" %(theta_0, theta_1))
        f.close()


for i in range(0, 1):
        learning_rate = 0.1
        estimate_price = (km * theta_1) + theta_0
        calc2 = estimate_price - price
        calc = (estimate_price - price) * km
        theta_0 = learning_rate * ((1 / (estimate_price.size)) * calc2.sum())
        theta_1 = learning_rate * ((1 / (estimate_price.size)) * calc.sum())
        print(f' estimate_price {estimate_price}')
        print(f' calc {calc}')
        print(f'nbr = {estimate_price.size}')
        print(f'new theta0 = {theta_0}')
        print(f'new theta1 = {theta_1}')
        print(f'nombre de fois : {i + 1}')
        save_thetas(theta_0, theta_1)


nbr_point_tracer = 2

linear = np.linspace(km.min, km.max, nbr_point_tracer)
fig, yx = plt.subplots()
yx.plot(linear, linear * theta_1 + theta_0, label='linear')
yx.scatter(km, price)

# Diplay
yx.set_xlabel(f'km')
yx.set_ylabel(f'price')
yx.set_title('Graph')
yx.legend()
plt.show()
"""
