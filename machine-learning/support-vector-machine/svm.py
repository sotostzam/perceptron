import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

class Support_Vector_Machine():
    def __init__(self):
        self.fig = plt.figure('Support Vector Machine')
        self.ax = self.fig.add_subplot(1,1,1)

    def visualize(self):
        points1 = np.where(self.targets == 1)
        points2 = np.where(self.targets == -1)
        self.ax.scatter(self.data[points1, 0], self.data[points1, 1], marker='+', color='r', label='Class 1')
        self.ax.scatter(self.data[points2, 0], self.data[points2, 1], marker='_', color='g', label='Class 2')

        def hyperplane(x, w, b, v):
            return (-w[0] * x - b + v) / w[1]

        h_min = self.min_value * 0.9
        h_max = self.max_value * 1.1

        pos_h_1 = hyperplane(h_min, self.weights, self.b, 1)
        pos_h_2 = hyperplane(h_max, self.weights, self.b, 1)
        self.ax.plot([h_min, h_max], [pos_h_1, pos_h_2])

        neg_h_1 = hyperplane(h_min, self.weights, self.b, -1)
        neg_h_2 = hyperplane(h_max, self.weights, self.b, -1)
        self.ax.plot([h_min, h_max], [neg_h_1, neg_h_2])

        db_h_1 = hyperplane(h_min, self.weights, self.b, 0)
        db_h_2 = hyperplane(h_max, self.weights, self.b, 0)
        self.ax.plot([h_min, h_max], [db_h_1, db_h_2])

        plt.legend(loc='upper right')
        plt.show()
        
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

        # This is a list of tuples containing: [magnitude of weight, transformed weight, b]
        magnitudes = [] 

        # Transformation matrix dotted with the weight vector
        transformation_matrix = [[1, 1],
                                 [-1, 1],
                                 [-1, -1],
                                 [1, -1]]

        # Find maximum and minimum values of dataset (also used for visualization)
        self.max_value = np.amax(np.amax(self.data, axis=0))
        self.min_value = np.amin(np.amin(self.data, axis=0))

        ''' This is a convex optimization problem, therefore by decreasing our steps every time
            we surpass the global best, so that we can approximate it more accurately. '''
        steps = [self.max_value * 0.1,
                 self.max_value * 0.01,
                 self.max_value * 0.001]

        b_multiplier = 5                        # Bias does not need to be as precise as w
        b_step_size = 5                         # Bias can take bigger steps than w
        weight_value = self.max_value * 10      # Initial value for the weight vector

        for step in steps:
            weights = np.array([weight_value, weight_value])    # Initialize current weight vector
            step_optimized = False                              # Indicates if we surpassed the global best of convex function

            while not step_optimized:
                for b in np.arange(-1 * self.max_value * b_multiplier, self.max_value * b_multiplier, step * b_step_size):
                    for transform in transformation_matrix:
                        transformed_w = weights * transform
                        data_misfits = False

                        # Check if everything in dataset fits this equation Yi*(Xi.w+b) >= 1
                        for i in range(0, len(self.data)):
                            yi = self.targets[i]
                            if not yi*(np.dot(transformed_w, self.data[i]) + b) >= 1:
                                data_misfits = True
                                break

                        # If there all data correctly fit
                        if not data_misfits:
                            ''' Tuple is of form: 
                                    1. Magnitude: math.sqrt(transformed_w[0] ** 2 + transformed_w[1] ** 2))
                                    2. Transformed vector
                                    3. Bias
                            '''
                            magnitudes.append((np.linalg.norm(transformed_w), transformed_w, b))

                # Check if we surpassed the global best (which is zero)
                if weights[0] < 0:
                    step_optimized = True
                    print('Step value ' + str(step/self.max_value) + ' found the closest value possible.')
                else:
                    weights = weights - step    # Apparently we are doing: weights - [step, step]

            # Sort the list using the first element(magnitudes), in ascenting order
            magnitudes = sorted(magnitudes, key = lambda x: x[0])
         
            best_value = magnitudes[0]                      # Take the smallest value of the magnitudes (we want to minimize that)
            self.weights = best_value[1]                    # Assign current best transformed weight vector to svm's weight vector
            self.b = best_value[2]                          # Assign current best bias to svm's bias
            weight_value = best_value[1][0] + step * 2      # Assign current best transformed weight vector as optimal for next iterration

    # Prediction method that returns a value of either -1 or 1
    def predict(self, features):
        # The equation of the prediction is: 'Xi dot W + b'
        prediction = np.sign(np.dot(features, self.weights) + self.b)
        return prediction