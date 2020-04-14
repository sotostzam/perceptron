# Linear Regression

Linear regression is an attempt to model the relationship between a dataset's values. This means that beforehand, it was made sure that there is a relationship between the variables of interest.

![linear-regression-gradient-descent](/images/linear_regression_gd.png)

## Optimization using ordinary least squares

The analytical solution and the most common method to linear regression analysis is that of the ordinary least squares (OLS). It does so by minimazing the sum of the squares of the distances between the observed data values in a daataset, and those predicted by the linear function. To run the example of linear regression using the ordinary least squares method type the following:

`python lr_ordinary_learst_squares.py`

## Optimization using gradient descent

Another approach to linear regression is using gradient descent to minimize the error (or cost function) of the line. The standard line equation is **y=m\*x+b**, where m is the slope of the line and b the y-intercept. Our goal is to alter these values so that we find a better line and at the same time minimize the error of it. To run the example of linear regression using gradient descent type the following:

`python lr_gradient_descent.py`

More on how gradient descent works and optimizes a cost function can be found in this [project](https://github.com/sotostzam/artificial-intelligence/tree/master/machine-learning/gradient-descent).
