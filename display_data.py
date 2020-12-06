#! /usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import csv

with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    km = []
    price = []
    for row in csv_reader:
        if line_count == 0:
            km.append(row[0])
            price.append(row[1])
            line_count += 1
        else:
            km.append(int(row[0]))
            price.append(int(row[1]))
            #print(f'Is the KM : {row[0]},Is the price : {row[1]}.')
    print(f'{km}')
    print(f'{price}')

# km[1:] from index 1

plt.plot(price[1:],km[1:])
plt.show()
