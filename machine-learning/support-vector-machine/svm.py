import numpy as np
import matplotlib.pyplot as plt

class Support_Vector_Machine():
    def __init__(self):
        self.fig = plt.figure('Support Vector Machine')
        self.ax = self.fig.add_subplot(1,1,1)

    def visualize(self):
        points1 = np.where(self.targets == 1)
        points2 = np.where(self.targets == -1)
        self.ax.scatter(self.data[points1, 0], self.data[points1, 1], marker='+', color='b', label='Class 1')
        self.ax.scatter(self.data[points2, 0], self.data[points2, 1], marker='_', color='r', label='Class 2')
        plt.show()

        def hyperplane(x, w, b, u):
            pass

    def train(self, data, targets):
        ''' The goal of this optimization problem is:
                1. Minimize ||w|| (the magnitude of vector w)
                2. Maximize the value of b (bias)
            The basic equation is:
                Yi * (Xi * w + bias) >= 1
            where:
                Yi represents either class (- or +)
                Xi represents the training data
        '''
        self.data = data
        self.targets = targets

        magnitudes = []             # This is a min heap which hold the magnitutes of vector w

        transforms = [[1, 1], [-1, 1], [-1, -1], [1, -1]]

        self.max_value = np.amax(np.amax(self.data, axis=0))
        self.min_value = np.amin(np.amin(self.data, axis=0))

        steps = [self.max_value * 0.1,
                 self.max_value * 0.01,
                 self.max_value * 0.001]

        b_multiplier = 10
        b_step_size = 5
        w_optimum = self.max_value * 10

        for step in steps:
            # Initialize weight vector of the support vector machine
            weights = np.array([w_optimum, w_optimum])
            optimized = False
            while not optimized:
                for b in np.arange(-1 * self.max_value * b_multiplier, self.max_value * b_multiplier, b_step_size):
                    for transformation in transforms:
                        transformed_w = weights * transformation
                        classified = True
                        for i in range(0, len(self.data)):
                            yi = self.targets[i]
                            if not yi*(np.dot(transformed_w, self.data[i]) + b) >= 1:
                                classified = False
                        if classified:
                            magnitudes.append((np.linalg.norm(transformed_w), transformed_w, b))

                if weights[0] < 0:
                    optimized = True
                else:
                    weights = weights - step

            magnitudes = sorted(magnitudes, key=lambda x: x[0])

            # Take the smallest value of the magnitudes (we want to minimize that)
            choice = magnitudes[0]
            self.weights = choice[1]
            self.b = choice[2]
            w_optimum = self.weights[0] + step * 2

        print(self.weights)

    # Prediction method that returns a value of either -1 or 1
    def predict(self, features):
        # The equation of the prediction is: 'Xi dot W + b'
        prediction = np.sign(np.dot(features, self.weights) + self.b)
        return prediction