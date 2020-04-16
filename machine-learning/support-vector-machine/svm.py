import numpy as np
import heapq

class Support_Vector_Machine():
    def __init__(self):
        pass

    # Prediction method that returns a value of either -1 or 1
    def predict(self, features):
        # The equation of the prediction is: 'Xi dot W + b'
        prediction = np.sign(np.dot(features, self.weights) + self.b)
        return prediction

    ''' The goal of this optimization problem is:
            1. Minimize ||w|| (the magnitude of vector w)
            2. Maximize the value of b (bias)
        The basic equation is:
            Yi * (Xi * w + bias) >= 1
        where:
            Yi represents either class (- or +)
            Xi represents the training data
    '''
    def train(self, data, targets):
        self.data = data
        self.targets = targets

        magnitudes = []             # This is a min heap which hold the magnitutes of vector w

        transforms = [[1, 1], [-1, 1], [-1, -1], [1, -1]]

        max_value = np.amax(np.amax(self.data, axis=0))
        min_value = np.amin(np.amin(self.data, axis=0))

        # Initialize weight vector of the support vector machine
        self.weights = np.array([max_value * 10, max_value * 10])
        
        for b in range(int(-1 * max_value * 10), int(max_value * 10), 5):
            for transformation in transforms:
                transformed_w = self.weights * transformation
                classified = True
                for i in range(0, len(self.data)):
                    yi = self.targets[i]
                    if not yi * (np.dot(transformed_w, self.data[i]) + b) >= 1:
                        classified = False
                if classified:
                    heapq.heappush(magnitudes, (50, 50))

        print(self.weights)
