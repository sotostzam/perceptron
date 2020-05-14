import matplotlib.pyplot as plt
import numpy as np

def euclidean_distance(item_1, item_2):
    distance = np.sqrt(np.sum((np.array(item_1) - np.array(item_2))**2))
    distance = np.linalg.norm(np.array(item_1) - np.array(item_2))
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
        shift_centroids = []
        for i in range(len(dataset)):
            shift_centroids.append(dataset[i])

        while True:
            next_centroids = []
            for centroid in shift_centroids:
                in_range = []
                for feature in dataset:
                    distance = euclidean_distance(centroid, feature)
                    if distance < self.bandwidth:
                        in_range.append(feature)

                new_centroid = np.average(in_range, axis = 0)
                next_centroids.append(new_centroid)

            # Keep only the unique centroids in the list
            unique_centroids = np.unique(next_centroids, axis=0)
            
            # Keep previous centroids for equality checks
            prev_centroids = np.copy(shift_centroids)
            # Assign the found centroids
            shift_centroids = np.copy(unique_centroids)

            if np.array_equal(shift_centroids, prev_centroids):
                break
        
        self.centroids = np.copy(shift_centroids)
