import numpy as np
import matplotlib.pyplot as plt

# Define the learning rate (Good values are usually 0.01, 0.03 or 0.05)
learning_rate = 0.05

# Define f(x), the cost function to run the gradient descent algorithm on
def f(x):
    return 2 * x ** 2 - 3 * x + 5

# Define the derivative of the cost function in order to find the slope
def df(x):
    return 4 * x - 3

# Create 100 points, evenly spaced, starting from -5 up to 5 on the y axis
x = np.linspace(-5,5,100)

# Setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_title('Gradient Descent')
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# List of x values over iterations
points = [-5.]

# Define how many epochs (iterations) for the algorithm to run
for i in range(50):
    plt.clf()
    points.append(points[i] - learning_rate * df(points[i]))
    plt.grid()
    plt.plot(x, f(x), 'r', label="2*x^2-3*x+5")                          # Plot the function
    plt.plot([points[i]], f(points[i]), marker='o', color="blue")        # Plot the point
    plt.legend(loc='upper center')
    plt.pause(0.01)

    # Declare convergence if the derivative of the cost function is less than 0.001
    if (abs(df(points[-1])) < 10**(-3)):
        print("Iteration: " + str(i))
        print("Minimum found at x = " + str(round(points[-1], 2)))
        print("Convergence with value = " + str(round(df(points[i]), 5)))
        break

plt.show()