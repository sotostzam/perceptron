# Gradient Descent

This is a Python implementation of the gradient descent algorithm. Gradient descent is an optimization algorithm for minimizing a given cost function, most commonly used in machine learning.

![gradient_descent](images/gradient_descent.png)

## Initialization of the algorithm

* Define the cost function to be minimized
* Define the derivative of the cost function
* Set the learning rate which controls the rate of change of the value
* Set the starting location at a specific point

## Explanation of the update on each iteration

On every iteration we calculate the location of the next point using the following formulae:

```Python
nextPoint = point - learning_rate * derivative(point)
```

Calculating the derivative of a specific point on the cost function, we can find the slope (or gradient) of the function at this specific location. This gradient transaltes to the direction of the steepest ascent. Having this in mind, we substact this value from the last location, to find the steepest descent that we need for the gradient descent algorithm.

## Prerequistes

1) [Python 3](https://www.python.org/downloads/)
2) [NumPy](http://www.numpy.org/)
3) [Matplotlib](http://matplotlib.org/)

For your convenience there is a file named requirements, which holds the information about all the required libraries. After making sure you have python up and running in your machine, you can install all the requirements by using the following command:

```Python
pip install -r requirements.txt
```
