import numpy as np
import matplotlib.pyplot as plt

class Perceptron():

    # Neuron Activation Function (Step function -1/1)
    def f(self, u):
        if u > 0:
            return 1
        else:
            return -1

    # Default constructor for a perceptron
    def __init__(self, maxEpochs = 10, learning_rate = 0.1, features = 2):
        self.w = -1 + np.random.rand(features + 1) * 2          # Initialize weights randomly on range [-1:1]  
        self.maxEpochs = maxEpochs                              # Max iterations
        self.learning_rate = learning_rate                      # Learning rate

    # Function to provide a guess for a specific input            
    def guess(self, input):
        sum = 0
        for i in range (0, len(self.w)):
            sum += self.w[i] * input[i]
        return self.f(sum)

    # Function to train the perceptron
    def train(self, dataset):
        x = np.delete(dataset, dataset.shape[0]-1, 0)           # Array holding sample data
        target = dataset[-1]                                    # Array representing the desired output of the neuron    
        x_min = np.amin(x[1]) - 0.5
        x_max = np.amax(x[1]) + 0.5
        y_min = np.amin(x[2]) - 0.5
        y_max = np.amax(x[2]) + 0.5

        # Iterate through each epoch
        for epoch in range (0, self.maxEpochs + 1):             # Iterate through the epochs given
            convergence = True                                  # Value indicating convergence status

            # Iterate through each sample
            for p in range (0, x.T.shape[0]):
                guessedValue = self.guess(x[:, p])              # Make a guess on the output of this sample
                error = (target[p] - guessedValue)              # Apply Gradient Descent to find the error

                # Weight tuning if sample is misclassified
                if guessedValue != target[p]:                                 
                    for i in range(0, len(self.w)):
                        self.w[i] += self.learning_rate * error * x[i, p]
                    convergence = False

            if convergence:
                print("Training successfull after " + str(epoch) + " epochs.")
                print("Weights after training: " + str(self.w) + "\n")
                break
            if convergence == False and epoch == self.maxEpochs:
                print("Training unsuccessfull after " + str(epoch) + " epochs.\n"
                      "Maybe this dataset is not linearly classifiable.\n")
            
            # Plotting of classes and the line separating the two
            x_range = np.linspace(x_min, x_max, endpoint = True)
            y_intercept = - 1 * (self.w[0] / self.w[2]) - 1 * (self.w[1] / self.w[2]) * x_range

            points1 = np.where(target == 1)
            points2 = np.where(target == -1)
            plt.clf()
            plt.title('Perceptron training...')
            plt.xlabel('Feature 1')
            plt.ylabel("Feature 2")
            plt.xlim(x_min, x_max)
            plt.ylim(y_min, y_max)
            plt.scatter(x[1, points1], x[2, points1], marker='x', color='b', label='Class 1')
            plt.scatter(x[1, points2], x[2, points2], marker='o', color='r', label='Class 2')
            plt.plot(x_range, y_intercept, linewidth=1, color='g')
            plt.legend(loc='upper right')
            plt.pause(0.1)

    def show_weights(self):
        print("Perceptron's weights:\t" + str(self.w) + "\n")