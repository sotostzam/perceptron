import matplotlib.pyplot as plt
import numpy as np

def euclidean_distance(item_1, item_2):
    distance = np.sqrt(np.sum((np.array(item_1) - np.array(item_2))**2))
    return distance

class Mean_Shift:
    def __init__(self, cohesion=0.001, max_iter=100, bandwidth=4):
        self.bandwidth = bandwidth
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

        while True:
            next_centroids = []
            for i in range(len(self.centroids)):
                in_range = []
                for j in range(len(dataset)):
                    feature_distance = euclidean_distance(self.centroids[i], dataset[j])
                    if feature_distance < self.bandwidth:
                        in_range.append(dataset[j])

                new_centroid = np.average(in_range, axis = 0)
                next_centroids.append(new_centroid)

            # We use this to break the loop for the time being
            break
