import matplotlib.pyplot as plt
import numpy as np

def euclidean_distance(item_1, item_2):
    distance = np.linalg.norm(np.array(item_1) - np.array(item_2))
    return distance

class Mean_Shift:
    def __init__(self, bandwidth=2):
        self.bandwidth = bandwidth
        self.fig = plt.figure('Mean-Shift Algorithm')
        self.ax = self.fig.add_subplot(1,1,1, projection='3d')
        self.fig.subplots_adjust(left=0, right=1, bottom=0, top=1)

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

            # Update plot with new centroid locations
            self.ax.clear()
            self.ax.set_xlabel('Sepal length')
            self.ax.set_ylabel('Petal length')
            self.ax.set_zlabel('Petal width')
            for i in range(len(dataset)):
                self.ax.scatter(dataset[i][1], dataset[i][2], dataset[i][3], c='b')
            for i in range(len(prev_centroids)):
                self.ax.scatter(prev_centroids[i][1], prev_centroids[i][2], prev_centroids[i][3], marker='*', c='r', s=50)
            plt.pause(0.01)

            # Check if we have convergence
            if np.array_equal(shift_centroids, prev_centroids):
                break
        
        self.centroids = np.copy(shift_centroids)
        print("Number of centroids: " + str(len(self.centroids)))

        plt.show()
