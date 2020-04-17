import numpy as np
import svm

def main():
    # Read x-values, y-values and the bias from the dataset
    dataset = np.genfromtxt('dataset.csv', delimiter=',')[:, [0,1]]
    # Read the target values (desired output) from the dataset
    targets = np.genfromtxt('dataset.csv', delimiter=',')[:, 2]

    model = svm.Support_Vector_Machine()
    model.train(dataset, targets)
    model.visualize()

    print(model.predict([0.5, 2.2]))

if __name__ == "__main__":
    main()