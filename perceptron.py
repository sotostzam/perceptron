import numpy as np
import matplotlib.pyplot as plt

class Perceptron():

    # Neuron Activation Function (Step function -1/1)
    def f(self, u):
        if u > 0:
            return 1
        else:
            return -1

    # Parameters
    w = b = maxEpochs = 0

    # Default constructor 
    def __init__(self):
        self.w = -1 + np.random.rand(3) * 2         # Initialize weights randomly on range [-1:1]  
        self.maxEpochs = 10                         # Max iterations
        self.b = 0.1                                # Learning rate

    def train(self, dataset):
        x = np.delete(dataset, dataset.shape[0]-1, 0)           # Array holding sample data
        d = dataset[-1]                                         # Array representing the desired output of the neuron    

        convergence = True                                      # Convergence value (True | False)

        # Start of Percepton training
        for epoch in range (0, self.maxEpochs + 1):             # Iterate through the epochs given
            convergence = True                                  # Convergence value (True | False)
            for p in range (0, x.T.shape[0]):                   # Iterate through each sample
                result = 0
                for i in range (0, len(self.w)):
                    result += self.w[i] * x[i, p]
                u = self.f(result)
                if u != d[p]:                                   # Check if sample is misclassified
                    for i in range(0, len(self.w)):
                        self.w[i] = self.w[i] + self.b * (d[p] - u) * x[i, p]      # Update weights
                    convergence = False
            if convergence:
                print("Training successfull after " + str(epoch) + " epochs.")
                print("Weights after training: " + str(self.w) + "\n")
                break
            if convergence == False and epoch == self.maxEpochs:
                print("Training unsuccessfull after " + str(epoch) + " epochs.\n"
                      "Maybe this dataset is not linearly classifiable.\n")

    def guess(self, point):
        guessedValue = 0
        for i in range (0, len(self.w)):
            guessedValue += self.w[i] * point[i]
        u = self.f(guessedValue)
        if u == -1:
            print("Perceptron's guess: Class 1.\n")
        else:
            print("Perceptron's guess: Class 2.\n")

    def show_weights(self):
        print("Perceptron's weights:\t" + str(self.w) + "\n")