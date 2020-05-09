import matplotlib.pyplot as plt
import numpy as np

def euclidean_distance(item_1, item_2):
    distance = np.sqrt(np.sum((np.array(item_1) - np.array(item_2))**2))
    return distance

class K_Means:
    def __init__(self, k=2, cohesion=0.001, max_iter=100):
        self.k = k
        self.cohesion = cohesion
        self.max_iter = max_iter
        self.fig = plt.figure('K-Means Algorithm')
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
        for i in range(self.k):
            self.centroids.append(dataset[i])

        for i in range(self.max_iter):
            self.clusters = {}
            for j in range(len(self.centroids)):
                self.clusters[j] = []

            for j in range(len(dataset)):
                closest_centroid = (None, np.inf)
                for n in range(len(self.centroids)):
                    feature_distance = euclidean_distance(self.centroids[n], dataset[j])
                    if feature_distance < closest_centroid[1]:
                        closest_centroid = (n, feature_distance)
                self.clusters[closest_centroid[0]].append(dataset[j])

            self.ax.clear()
            self.ax.set_xlabel('Sepal length')
            self.ax.set_ylabel('Petal length')
            self.ax.set_zlabel('Petal width')
            for cluster in self.clusters:
                self.ax.scatter(self.centroids[cluster][1], self.centroids[cluster][2], self.centroids[cluster][3], marker=self.markers[cluster], c='k', s=30)
                for feature in self.clusters[cluster]:
                    self.ax.scatter(feature[1], feature[2], feature[3], c=self.colors[cluster], marker=self.markers[cluster], s=30)
            plt.pause(0.01)

            # Calculate new centroids
            cohesion_bypassed = False
            old_centroids = self.centroids.copy()
            for cluster in self.clusters:
                self.centroids[cluster] = np.mean(self.clusters[cluster], axis = 0)

                # Quality of cluster is determined by the sum of squared error (also known as residual sum of squares)
                rss = np.sum((old_centroids[cluster]-self.centroids[cluster])**2)
                if rss > self.cohesion:
                    cohesion_bypassed = True

            if not cohesion_bypassed:
                print("Clusters found! Run for " + str(i) + " iterations.")
                break
        plt.draw()

    def predict(self, features):
        for feature in features:
            closest_centroid = (None, np.inf)
            for i in range(len(self.centroids)):
                feature_distance = euclidean_distance(self.centroids[i], feature)
                if feature_distance < closest_centroid[1]:
                    closest_centroid = (i, feature_distance)
            self.ax.scatter(feature[1], feature[2], feature[3], c=self.colors[closest_centroid[0]], marker='*', s=100, linewidth='1', edgecolor='k')
            plt.pause(0.01)
        plt.show()
    