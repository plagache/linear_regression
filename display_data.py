#! /usr/bin/python3

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv

# old methode to import data

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
   # print(f'{x}')
   # print(f'{y}')

## Automatic data import wiht panda

data = pd.read_csv('data.csv')

# Create frame
df = pd.DataFrame(data)
print(df[['km', 'price']])

# Create columns
km = df["km"]
price = df["price"]
print(f'km :  {km}')

# old min-max function
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

min_p, max_p = min_max(price)
min_k, max_k = min_max(km)
#print(f'minimum price is : {min_p}, maximum is : {max_p}')
#print(f'minimum km is : {min_k}, maximum is : {max_k}')


## min max function from python3
min_p = min(price) 
max_p = max(price) 
print(f'minimum price : {min_p}, maximum price : {max_p}')

min_k = min(km)
max_k = max(km)
print(f'minimum km : {min_k}, maximum km : {max_k}')

# Old methode to calculte a and b

nbr_point_tracer = 2

coef_directeur = 1 / ((min_k - max_k) / (max_p - min_p))
print(coef_directeur)

Ordonne_Origin = min_p - coef_directeur * max_k
print(Ordonne_Origin)
print(f'min p {min_p}')
print(f'max k {max_k}')

linear = np.linspace(min_k, max_k, nbr_point_tracer)
print(linear)

## Calculate a and b of ax+b

def element_droite(ax, ay, bx, by):

    coef_directeur = (ay - by) / (ax - bx)
    print(f'coef_ directeur : {coef_directeur}')

    Ordonne_Origin = ay - coef_directeur * ax
    print(Ordonne_Origin)
    print(f'Ordonne_Origin : {Ordonne_Origin}')

    return (coef_directeur, Ordonne_Origin)


coef_directeur, Ordonne_Origin = element_droite(km[km.idxmin()], price[km.idxmin()], km[km.idxmax()], price[km.idxmax()])


fig, yx = plt.subplots()
yx.plot(linear, linear * coef_directeur + Ordonne_Origin, label='linear')
yx.scatter(x[1:], y[1:])

# Diplay
yx.set_xlabel(f'{x[0]}')
yx.set_ylabel(f'{y[0]}')
yx.set_title('Graph')
yx.legend()
plt.show()
