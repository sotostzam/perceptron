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

    def fit(self, dataset):
        # Randomly shuffle all rows
        dataset = dataset.sample(frac=1).reset_index(drop=True)
        
        # Select first k centroids from shuffled dataset
        self.centroids = []
        for i in range(self.k):
            self.centroids.append(dataset.iloc[i])

        for i in range(self.max_iter):
            self.clusters = {}
            for j in range(len(self.centroids)):
                self.clusters[j] = []

            for j in range(dataset.shape[0]):
                closest_centroid = None
                for n in range(len(self.centroids)):
                    if closest_centroid is None or euclidean_distance(self.centroids[n], dataset.iloc[j]) < closest_centroid:
                        closest_centroid = n
                self.clusters[closest_centroid].append(dataset.iloc[j])

            # Calculate new centroids

            self.fig.clf()
            ax = self.fig.add_subplot(1,1,1, projection='3d')
            ax.set_xlabel('Sepal length')
            ax.set_ylabel('Petal length')
            ax.set_zlabel('Petal width')
            # ax.scatter(dataset['sepal_width'], dataset['petal_length'], dataset['petal_width'])
            for i in range(len(self.clusters)):
                for n in range(len(self.clusters[i])):
                    ax.scatter(self.clusters[i][n]['sepal_width'], self.clusters[i][n]['petal_length'], self.clusters[i][n]['petal_width'], c=self.colors[i])
            for centroid in self.centroids:
                ax.scatter(centroid['sepal_width'], centroid['petal_length'], centroid['petal_width'], marker='x', color='r', s=50)
            plt.pause(0.0001)

        plt.show()

    def predict(self):
        pass