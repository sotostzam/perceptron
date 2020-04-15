import numpy as np
from matplotlib import pyplot as plt

# Function to train the support vector machine
def train_svm(points, targets, learning_rate, epochs):
    # Initialize weights of the support vector machine
    weights = np.zeros(len(points[0]))
    # Implement svm here
    return weights

def main():
    # Read x-values, y-values and the bias from the dataset
    dataset = np.genfromtxt('dataset.csv', delimiter=',')[:, [0,1,3]]
    # Read the target values (desired output) from the dataset
    targets = np.genfromtxt('dataset.csv', delimiter=',')[:, 2]

    learning_rate = 0.1
    iterations = 10000

    weights = train_svm(dataset, targets, learning_rate, iterations)
  
    points1 = np.where(targets == 1)
    points2 = np.where(targets == -1)
    plt.clf()
    plt.title('Support Vector Machine')
    plt.scatter(dataset[points1, 0], dataset[points1, 1], marker='+', color='b', label='Class 1')
    plt.scatter(dataset[points2, 0], dataset[points2, 1], marker='_', color='r', label='Class 2')
    plt.show()

if __name__ == "__main__":
    main()