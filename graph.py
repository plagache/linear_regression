#!/usr/bin/python3

import matplotlib.pyplot as graph
import pandas
import numpy as math
import matplotx
import os
import imageio
import argparse


parser = argparse.ArgumentParser(
                    prog='Graph',
                    description='Plot different graph',
                    exit_on_error=False)

parser.add_argument('-p', '--polyfit',
                    help='Polyfit example',
                    action='store_true',
                    required=False)

parser.add_argument('-l', '--linear',
                    help='My linear function',
                    action='store_true',
                    required=False)

parser.add_argument('-g', '--gif',
                    help='Create Animated Gif',
                    action='store_true',
                    required=False)

args = parser.parse_args()


data = pandas.read_csv('data.csv')
data_frame = pandas.DataFrame(data)
x_values = data_frame["km"]
y_values = data_frame["price"]
x_min = x_values.min()
x_max = x_values.max()


thetas = pandas.read_csv('thetas.csv')
thetas_frame = pandas.DataFrame(thetas)
theta_0 = thetas_frame["theta0"].values[-1]
theta_1 = thetas_frame["theta1"].values[-1]
thetas_size = thetas_frame["theta0"].count()


def base_graph(xs, ys):

    # graph.style.use(matplotx.styles.dracula)
    # graph.style.use(matplotx.styles.onedark)
    graph.style.use(matplotx.styles.gruvbox["dark"])

    graph.xlabel('km')
    graph.ylabel('price')
    graph.scatter(xs, ys)
    # graph.legend()


nombre_point_tracer = 2


def ploting_linear_regression(theta_0, theta_1, x_min, x_max, name, format):

    # Prepare Data to be display on matplotlib
    x = math.linspace(x_min, x_max, nombre_point_tracer)
    y = x * theta_1 + theta_0

    # plot the linear regression
    graph.plot(x, y, format, label=name)


def polyfit_example():
    model = math.polyfit(x_values, y_values, 1)
    ploting_linear_regression(model[1], model[0], x_min, x_max, "Polyfit Example", "r:.")


def create_animated_gif(theta_0, theta_1):

    directory = "png"
    # print(directory)

    current_directory = os.getcwd()
    # print(current_directory)

    # Path
    path = os.path.join(current_directory, directory)
    # print(path)

    # Does Path already exist ?
    isExist = os.path.exists(path)
    # print(isExist)

    # Create directory
    if (isExist == False):
        os.mkdir(path)

    frames = []

    total_image = 120

    for index in range(1, total_image):

        # print(thetas_size)
        # print(index)
        index_pondere = int(thetas_size / total_image)
        # print(int(index_pondere))
        # print(index * index_pondere)
        theta_0 = thetas_frame["theta0"].values[index * index_pondere]
        theta_1 = thetas_frame["theta1"].values[index * index_pondere]
        base_graph(x_values, y_values)
        ploting_linear_regression(theta_0, theta_1, x_min, x_max, "My Linear Regression", "g")

        # create file name and append it to a list
        filename = f'png/{index}.png'
        frames.append(filename)

        # save frame
        graph.savefig(filename)
        graph.close()


    # Last frame
    base_graph(x_values, y_values)
    ploting_linear_regression(theta_0, theta_1, x_min, x_max, "My Linear Regression", "g")
    polyfit_example()
    # create file name and append it to a list
    filename = f'png/{total_image + 1}.png'
    frames.append(filename)

    # save frame
    graph.legend()
    graph.savefig(filename)
    graph.close()


        # build gif
    with imageio.get_writer('training.gif', mode='I') as writer:
        for filename in frames:
            image = imageio.v3.imread(filename)
            writer.append_data(image)
        writer.close

    # Remove files
    for filename in set(frames):
        os.remove(filename)
    os.rmdir(path)



base_graph(x_values, y_values)


if (args.linear == True):
    ploting_linear_regression(theta_0, theta_1, x_min, x_max, "My Linear Regression", "g")


if (args.polyfit == True):
    polyfit_example()


graph.legend()


if (args.gif == True):
    create_animated_gif(theta_0, theta_1)


graph.show()
