import pandas as pd

def import_thetas():
    # Theta import
    theta = pd.read_csv('theta.csv')
    theta_f = pd.DataFrame(theta)
    theta_0 = theta_f["theta0"].values[-1]
    theta_1 = theta_f["theta1"].values[-1]
    return theta_0, theta_1

def estimate_price(km, t0, t1):
    return t1 * km + t0
