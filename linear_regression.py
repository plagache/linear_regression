#!/usr/bin/python3

from visual import display, save_fig
from tools import import_data, import_thetas, estimate_price, get_normalized_list, get_denormalized_value, save_thetas
import imageio

# Data import
df, kms, prices = import_data()

km_min = kms.min()
km_max = kms.max()

price_max = prices.max()
price_min = prices.min()

df["normalized_price"] = get_normalized_list(prices.tolist(), price_min, price_max)
n_prices = df["normalized_price"]

df["normalized_km"] = get_normalized_list(kms.tolist(), km_min, km_max)
n_kms = df["normalized_km"]

n_km_min = n_kms.min()
n_km_max = n_kms.max()

sample_size = len(kms.values.tolist())

theta_0, theta_1 = import_thetas()

# Denormalize thetas
def denormalize_thetas(t0, t1):

    # Some value for kms
    x0, x1 = kms.values[0], kms.values[1]

    # Price at x0
    y0 = prices.values[0]

    # Corresponding normalized value for kms
    x0n, x1n = n_kms.values[0], n_kms.values[1]

    # Corresponding normalized value for price using the normalized parameters
    y0n, y1n = estimate_price(x0n, t0, t1), estimate_price(x1n, t0, t1)

    # Denormalized value of estimation
    y0r, y1r = get_denormalized_value(y0n, price_min, price_max), get_denormalized_value(y1n, price_min, price_max)

    # Simplified equation from jon nimrod
    dtheta_0 =  (y0r * x1 - x0 * y1r) / (x1 - x0)
    dtheta_1 = (y0 - dtheta_0) / x0

    return dtheta_0, dtheta_1

frames = []

# Perform linear reg a certain number (range)
for i in range(0, 100):

    learning_rate = 0.7
    dt0 = 0
    dt1 = 0

    for km, price in zip(n_kms, n_prices):
        price_diff = estimate_price(km, theta_0, theta_1) - price
        dt0 += price_diff
        dt1 += price_diff * km

    theta_0 -= learning_rate * dt0 / sample_size
    theta_1 -= learning_rate * dt1 / sample_size

    dtheta0, dtheta1 = denormalize_thetas(theta_0, theta_1)
    save_thetas(dtheta0, dtheta1)
    save_fig(dtheta0, dtheta1, df, i)

    image = imageio.v2.imread(f'./img/img_{i}.png')
    frames.append(image)



# display(theta_0, theta_1, n_kms, n_prices, n_km_min, n_km_max)

nt0, nt1 = denormalize_thetas(theta_0, theta_1)

display(nt0, nt1, kms, prices, km_min, km_max)

image = imageio.v2.imread(f'./img/img_final.png')
frames.append(image)
imageio.mimsave('./example.gif', frames, duration = 50)
