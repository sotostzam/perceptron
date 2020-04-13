import numpy as np
import matplotlib.pyplot as plt

# Find regression line using ordinary least squares method
def regression(x_values, y_values):
    x_mean = np.sum(x_values) / len(x_values)
    y_mean = np.sum(y_values) / len(y_values)
    
    nom = 0
    den = 0
    for i in range(len(x_values)):
        nom += (x_values[i] - x_mean) * (y_values[i] - y_mean)
        den += (x_values[i] - x_mean) ** 2
    m = nom / den
    b = y_mean - m * x_mean
    return m, b

def main():
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

    x_min = np.amin(x) - 1
    x_max = np.amax(x) + 1
    y_min = np.amin(y) - 1
    y_max = np.amax(y) + 1

    m, b = regression(x, y)

    x_range = np.linspace(x_min, x_max, endpoint = True)
    line = m * x_range + b

    plt.title('Linear Regression')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.scatter(x, y, color='b')
    plt.plot(x_range, line, linewidth=1, color='g')
    plt.show()

if __name__ == "__main__":
    main()