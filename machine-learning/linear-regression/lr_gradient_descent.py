import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Find the regression line using gradient descent
def gradient_descent(x_values, y_values, m, b, learning_rate):
    d_m = 0
    d_b = 0
    for i in range(len(x_values)):
        guess = m * x_values[i] + b
        error = y_values[i] - guess
        d_m += x_values[i] * error
        d_b += error
    m += d_m * learning_rate
    b += d_b * learning_rate
    return m, b

def main():
    # Load different sets (I, II, III, IV)
    dataset = pd.read_csv("anscombes.csv", index_col=0)
    data = dataset[dataset['dataset'] == 'I']
    x = data.x.tolist()
    y = data.y.tolist()

    # Initialize line (y = m*x + b) where m is slope and b is y-intercept
    m = 0   # Slope
    b = 0   # Y-intercept
    learning_rate = 0.0001
    iterations = 100

    x_range = np.array([np.min(x) - 2, np.max(x) + 2])
    fig = plt.figure('Linear Regression using Gradient Descent')
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title("Anscombe's Quartet Set I")
    #plt.clf()
    ax.set_xlim(np.min(x) - 2, np.max(x) + 2)
    ax.set_ylim(np.min(y) - 2, np.max(y) + 2)
    ax.scatter(x, y)

    for _ in range(iterations):
        m, b = gradient_descent(x, y, m, b, learning_rate)
        line = m * x_range + b
        ax.plot(x_range, line, linewidth=1, color='r')
        plt.pause(0.01)
    plt.show()

if __name__ == "__main__":
    main()