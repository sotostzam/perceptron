import numpy as np
from matplotlib import pyplot as plt
import svm

def main():
    # Read x-values, y-values and the bias from the dataset
    dataset = np.genfromtxt('dataset.csv', delimiter=',')[:, [0,1]]
    # Read the target values (desired output) from the dataset
    targets = np.genfromtxt('dataset.csv', delimiter=',')[:, 2]

    model = svm.Support_Vector_Machine()
    model.train(dataset, targets)

    learning_rate = 0.1
    iterations = 10000
  
    points1 = np.where(targets == 1)
    points2 = np.where(targets == -1)
    plt.clf()
    plt.title('Support Vector Machine')
    plt.scatter(dataset[points1, 0], dataset[points1, 1], marker='+', color='b', label='Class 1')
    plt.scatter(dataset[points2, 0], dataset[points2, 1], marker='_', color='r', label='Class 2')
    plt.show()

if __name__ == "__main__":
    main()