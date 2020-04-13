import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Find the regression line using gradient descent
def regression(x_values, y_values, slope, y_inter):
    for i in range(len(x_values)):
        guess = slope * x_values[i] + y_inter
        error = y_values[i] - guess
        slope += error * x_values[i] * 0.01
        y_inter += error * 0.01
    return slope, y_inter

def main():
    dataset = pd.read_csv("anscombes.csv", index_col=0)
    data = dataset[dataset['dataset'] == 'I']
    x = data.x.tolist()
    y = data.y.tolist()
    x_range = np.linspace(np.min(x) - 2, np.max(x) + 2, endpoint = True)

    # Initialize slope and y-intercept
    m = 0
    b = 0

    fig = plt.figure('Linear Regression using Gradient Descent')

    for _ in range(50):
        m, b = regression(x, y, m, b)
        line = m * x_range + b

        plt.clf()
        ax = fig.add_subplot(1, 1, 1)
        ax.set_title("Anscombe's Quartet Set I")
        ax.set_xlim(np.min(x) - 2, np.max(x) + 2)
        ax.set_ylim(np.min(y) - 2, np.max(y) + 2)
        ax.scatter(x, y)
        ax.plot(x_range, line, linewidth=1, color='r')
        plt.pause(0.1)
    plt.show()

if __name__ == "__main__":
    main()