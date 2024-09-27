# Linear Regression

## Installation and dependencies
You need python, pip, make
```bash
git clone https://github.com/plagache/linear_regression
cd linear_regression
make
```

## Usage
```
make train
make predict
make graph
```

## Explanation

our goal is to find a and b for the function a * x + b;
that will match our data set;
![Alt text](/readme_ressource/base.png)

this is the data plot with the same range of price than kilometers
![Alt text](/readme_ressource/data_with_y_to_250000.png)
we can see that price and kilometers are on a very different scale

if we didn't normalize the probleme is that we would have to use different learning rate;

the methode we use to normalize is called a min max normalization.
put simply :
we compare the range between the smallest element and our current element
and the range between the smallest and biggest of our data set

this way we keep the proportion but we are now in a plan between 0 and 1
![Alt text](/readme_ressource/data_normalize.png)

on this plan we do our training, and we can use the same learning rate for both our a and b;

we obtain thetas that are correlated with the normalize data
![Alt text](/readme_ressource/trained_normalize.png)

then we are going to use the,

distance of our data set :

```
y_range = y_max - y_min
x_range = x_max - x_min
```

and the range ratio :

```
range_ratio = y_range / x_range
```

to denormalize our theta.

this values enable us to rescale the theta to the scale of our data set.

![Alt text](/readme_ressource/my_linear.png)
