import numpy as np
from matplotlib import pyplot as plt
import svm

def main():
    # Read x-values, y-values and the bias from the dataset
    dataset = np.genfromtxt('dataset.csv', delimiter=',')[:, [0,1,3]]
    # Read the target values (desired output) from the dataset
    targets = np.genfromtxt('dataset.csv', delimiter=',')[:, 2]

    support_vector_machine = svm.Support_Vector_Machine()

    learning_rate = 0.1
    iterations = 10000
  
    points1 = np.where(targets == 1)
    points2 = np.where(targets == -1)
    plt.clf()
    plt.title('Support Vector Machine')
    plt.scatter(dataset[points1, 0], dataset[points1, 1], marker='+', color='b', label='Class 1')
    plt.scatter(dataset[points2, 0], dataset[points2, 1], marker='_', color='r', label='Class 2')
    #plt.plot(weights[0], weights[1], -weights[1], weights[0])

    x2 = [weights[0], weights[1], -weights[1], weights[0]]
    x3 = [weights[0], weights[1], weights[1], -weights[0]]

    x2x3 = np.array([x2, x3])
    X, Y, U, V = zip(*x2x3)

    ax = plt.gca()
    ax.quiver(X,Y,U,V, scale = 1, color = 'blue')
    #plt.pause(0.0001)
    plt.show()

if __name__ == "__main__":
    main()