import numpy as np
import svm

def main():
    # Read x-values, y-values and the bias from the dataset
    dataset = np.genfromtxt('dataset.csv', delimiter=',')[:, [0,1]]
    # Read the target values (desired output) from the dataset
    targets = np.genfromtxt('dataset.csv', delimiter=',')[:, 2]

    # Create and train the support vector machine
    model = svm.Support_Vector_Machine()
    model.train(dataset, targets)

    # Create a list of points and ask for a prediction on them
    test_data = [[0.5, 2.2], [1.7, 3.1], [1.8, 2.9], [-1.2, -0.2], [3, 4.7]]
    for point in test_data:
        model.predict(point)

    # Show visualization plot of the model + predictions
    model.visualize()

if __name__ == "__main__":
    main()