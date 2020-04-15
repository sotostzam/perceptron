import numpy as np

class Support_Vector_Machine():
    def __init__(self):
        pass

    def predict(self, features):
        return np.sign(np.dot(features, self.weights) + self.b)

    def train(self, data):
        self.data = data
        
        # Initialize weights of the support vector machine
        weights = np.zeros(len(data[0]))
        