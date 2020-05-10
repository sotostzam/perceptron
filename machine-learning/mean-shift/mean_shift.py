import matplotlib.pyplot as plt
import numpy as np

def euclidean_distance(item_1, item_2):
    distance = np.sqrt(np.sum((np.array(item_1) - np.array(item_2))**2))
    return distance

class Mean_Shift:
    def __init__(self, cohesion=0.001, max_iter=100, radius=4):
        self.radius = radius
        self.cohesion = cohesion
        self.max_iter = max_iter
        self.fig = plt.figure('Mean-Shift Algorithm')
        self.ax = self.fig.add_subplot(1,1,1, projection='3d')
        self.fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
        self.markers = ['+', 'o', 'x', 's', 'd', 'p', 'v', '^']
        self.colors = ['r', 'g', 'b', 'y', 'm', 'c', 'peru', 'lightgreen']

    def fit(self, featureset):
        # Randomly shuffle all rows
        featureset = featureset.sample(frac=1).reset_index(drop=True)
        dataset = featureset.to_numpy()

        # Select first k centroids from shuffled dataset
        self.centroids = []
        for i in range(len(dataset)):
            self.centroids.append(dataset[i])

        for i in self.centroids:
            pass