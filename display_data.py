#! /usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import csv

with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    x = []
    y = []
    for row in csv_reader:
        if line_count == 0:
            x.append(row[0])
            y.append(row[1])
            line_count += 1
        else:
            x.append(int(row[0]))
            y.append(int(row[1]))
            #print(f'Is the KM : {row[0]},Is the price : {row[1]}.')
    print(f'{km}')
    print(f'{price}')

def min_max(lst):
    maxi = lst[0]
    mini = maxi
    for element in lst:
        if maxi < element:
            maxi = element
        if mini > element:
            mini = element
    return (mini, maxi)

# km[1:] from index 1

# goes from 240 000km for 3650 dollars
# to 22 899 for 7990 dollars

nbr_point_tracer = 2

min_p, max_p = min_max(y[1:])
min_k, max_k = min_max(x[1:])
print(f'minimum is : {min_p}, maximum is : {max_p}')
print(f'minimum is : {min_k}, maximum is : {max_k}')

coef_directeur = 1 / ((min_k - max_k) / (max_p - min_p))
print(coef_directeur)

Ordonne_Origin = min_p - coef_directeur * max_k
print(Ordonne_Origin)

linear = np.linspace(min_k, max_k, nbr_point_tracer)
print(linear)


fig, yx = plt.subplots()
yx.plot(linear, linear * coef_directeur + Ordonne_Origin, label='linear')
yx.scatter(x[1:], y[1:])

# Diplay
yx.set_xlabel(f'{x[0]}')
yx.set_ylabel(f'{y[0]}')
yx.set_title('Graph')
yx.legend()
plt.show()
