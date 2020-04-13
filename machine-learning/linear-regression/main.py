import pandas as pd
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
    dataset = pd.read_csv("anscombes.csv", index_col=0)

    set_1 = dataset[dataset['dataset'] == 'I']
    set_2 = dataset[dataset['dataset'] == 'II']
    set_3 = dataset[dataset['dataset'] == 'III']
    set_4 = dataset[dataset['dataset'] == 'IV']

    x1 = set_1.x.tolist()
    y1 = set_1.y.tolist()
    x2 = set_2.x.tolist()
    y2 = set_2.y.tolist()
    x3 = set_3.x.tolist()
    y3 = set_3.y.tolist()
    x4 = set_4.x.tolist()
    y4 = set_4.y.tolist()

    x_min = 2
    x_max = 20
    y_min = 2
    y_max = 14

    m1, b1 = regression(x1, y1)
    m2, b2 = regression(x2, y2)
    m3, b3 = regression(x3, y3)
    m4, b4 = regression(x4, y4)

    x_range = np.linspace(x_min, x_max, endpoint = True)

    line1 = m1 * x_range + b1
    line2 = m2 * x_range + b2
    line3 = m3 * x_range + b3
    line4 = m4 * x_range + b4

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    fig.canvas.set_window_title('Linear Regression')
    fig.suptitle("Anscombe's quartet")

    ax1.scatter(x1, y1)
    ax1.plot(x_range, line1, linewidth=1, color='r')
    ax1.set_xlim(x_min, x_max)
    ax1.set_ylim(y_min, y_max)
    ax1.set_title('Set I')

    ax2.scatter(x2, y2)
    ax2.plot(x_range, line2, linewidth=1, color='r')
    ax2.set_xlim(x_min, x_max)
    ax2.set_ylim(y_min, y_max)
    ax2.set_title('Set II')

    ax3.scatter(x3, y3)
    ax3.plot(x_range, line3, linewidth=1, color='r')
    ax3.set_xlim(x_min, x_max)
    ax3.set_ylim(y_min, y_max)
    ax3.set_title('Set III')

    ax4.scatter(x4, y4)
    ax4.plot(x_range, line4, linewidth=1, color='r')
    ax4.set_xlim(x_min, x_max)
    ax4.set_ylim(y_min, y_max)
    ax4.set_title('Set IV')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()