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

        # Visualization
        points1 = np.where(target == -1)
        points2 = np.where(target == 1)
        x_min = np.amin(x[1]) * 0.9
        x_max = np.amax(x[1]) * 1.1
        y_min = np.amin(x[2]) * 0.9
        y_max = np.amax(x[2]) * 1.1
        x_range = np.linspace(x_min, x_max, endpoint = True)

        fig = plt.figure('Perceptron Neuron')
        ax = fig.add_subplot(1,1,1)
        ax.set_xlabel('Feature 1')
        ax.set_ylabel('Feature 2')
        ax.legend(loc='upper right')
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
        ax.scatter(x[1, points1], x[2, points1], marker='x', color='b', label='Class -1')
        ax.scatter(x[1, points2], x[2, points2], marker='o', color='r', label='Class 1')
        line = None

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
            
            # Plotting the line separating the two classes
            y_intercept = - 1 * (self.w[0] / self.w[2]) - 1 * (self.w[1] / self.w[2]) * x_range
            if line:
                ax.lines.remove(line)
            line, = plt.plot(x_range, y_intercept, linewidth=1, color='g')
            plt.pause(0.001)

    def show_weights(self):
        print("Perceptron's weights:\t" + str(self.w) + "\n")