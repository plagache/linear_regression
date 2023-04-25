#!/usr/bin/python3

from visual import display
from tools import import_thetas, estimate_price
import pandas as pd

def get_normalized_list(values, min, max):
    return [get_normalized_value(x, min, max) for x in values]

def get_denormalized_list(values, min, max):
    return [get_denormalized_value(x, min, max) for x in values]

def get_normalized_value(value, min, max):
    return (value - min) / (max - min)

def get_denormalized_value(value, min, max):
    return value * (max - min) + min

def save_thetas(theta_0, theta_1):
    f = open("theta.csv", "a+")
    f.write("%f, %f\n" % (theta_0, theta_1))
    f.close()

# Data import
data = pd.read_csv('data.csv')
df = pd.DataFrame(data)

kms = df["km"]
km_min = kms.min()
km_max = kms.max()

prices = df["price"]
price_max = prices.max()
price_min = prices.min()

df["normalized_price"] = get_normalized_value(prices.tolist(), price_min, price_max)
df["normalized_km"] = get_normalized_value(kms.tolist(), km_min, km_max)
norme_price = df["normalized_price"]
# df["renormalized_price"] = get_denormalized_list(norme_price.tolist(), price_min, price_max)
norme_km = df["normalized_km"]
# df["renormalized_km"] = get_denormalized_list(norme_km.tolist(), km_min, km_max)
n_km_min = norme_km.min()
n_km_max = norme_km.max()

sample_size = len(kms.values.tolist())

theta_0, theta_1 = import_thetas()
# theta_0 = get_normalized_value(theta_0, price_min, price_max)

# Denormalize thetas
def denormalize_thetas(t0, t1):

    # Some value for kms
    x0, x1 = kms.values[0], kms.values[1]

    # Price at x0
    y0 = prices.values[0]

    # Corresponding normalized value for kms
    x0n, x1n = norme_km.values[0], norme_km.values[1]

    # Corresponding normalized value for price using the normalized parameters
    y0n, y1n = estimate_price(x0n, t0, t1), estimate_price(x1n, t0, t1)

    # Denormalized value of estimation
    y0r, y1r = get_denormalized_value(y0n, price_min, price_max), get_denormalized_value(y1n, price_min, price_max)

    # Simplified equation from jon nimrod
    dtheta_0 =  (y0r * x1 - x0 * y1r) / (x1 - x0)
    dtheta_1 = (y0 - dtheta_0) / x0

    return dtheta_0, dtheta_1

# Perform linear reg a certain number (range)
for i in range(0, 100):

    learning_rate = 0.7
    dt0 = 0
    dt1 = 0

    for km, price in zip(norme_km, norme_price):
        estimated_price = estimate_price(km, theta_0, theta_1)
        dt0 += estimated_price - price
        dt1 += (estimated_price - price) * km

    theta_0 -= learning_rate * dt0 / sample_size
    theta_1 -= learning_rate * dt1 / sample_size

    dtheta0, dtheta1 = denormalize_thetas(theta_0, theta_1)
    save_thetas(dtheta0, dtheta1)

display(theta_0, theta_1, norme_km, norme_price, n_km_min, n_km_max)

nt0, nt1 = denormalize_thetas(theta_0, theta_1)

display(nt0, nt1, kms, prices, km_min, km_max)
