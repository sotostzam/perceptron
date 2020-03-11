import numpy as np

class Agent():

    # Default constructor for a perceptron
    def __init__(self, start_x, start_y):
        self.location = [start_x, start_y]
        self.q_table = np.zeros((10, 10))