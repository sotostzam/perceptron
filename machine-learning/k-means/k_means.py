import matplotlib.pyplot as plt
import numpy as np

def euclidean_distance(item_1, item_2):
    distance = np.sqrt(np.sum((np.array(item_1) - np.array(item_2))**2))
    return distance

class K_Means:
    def __init__(self, k=2, tol=0.001, max_iter=300):
        self.k = k
        self.tolerance = tol
        self.max_iter = max_iter
        self.fig = plt.figure('K-Means Algorithm')
        self.colors = ['g', 'b']

    def fit(self, featureset):
        # Randomly shuffle all rows
        featureset = featureset.sample(frac=1).reset_index(drop=True)
        dataset = featureset.to_numpy()

        # Select first k centroids from shuffled dataset
        self.centroids = []
        for i in range(self.k):
            self.centroids.append(dataset[i])

        for i in range(self.max_iter):
            self.clusters = {}
            for j in range(len(self.centroids)):
                self.clusters[j] = []

            for j in range(len(dataset)):
                closest_centroid = (None, None)
                for n in range(len(self.centroids)):
                    distance = euclidean_distance(self.centroids[n], dataset[j])
                    if closest_centroid is (None, None) or distance < closest_centroid[1]:
                        closest_centroid = (n, distance)
                self.clusters[closest_centroid[0]].append(dataset[j])

            # Calculate new centroids
            for cluster in self.clusters:
                self.centroids[cluster] = np.mean(self.clusters[cluster], axis = 0)

            self.fig.clf()
            ax = self.fig.add_subplot(1,1,1, projection='3d')
            ax.set_xlabel('Sepal length')
            ax.set_ylabel('Petal length')
            ax.set_zlabel('Petal width')
            for cluster in self.clusters:
                ax.scatter(self.centroids[cluster][1], self.centroids[cluster][2], self.centroids[cluster][3], marker='x', color='r', s=50)
                for feature in self.clusters[cluster]:
                    ax.scatter(feature[1], feature[2], feature[3], c=self.colors[cluster])
            plt.pause(0.0001)

        plt.show()

    def predict(self):
        pass