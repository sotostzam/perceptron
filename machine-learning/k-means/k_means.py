import matplotlib.pyplot as plt
import numpy as np

class K_Means:
    def __init__(self, k=2, tol=0.001, max_iter=300):
        self.k = k
        self.tolerance = tol
        self.max_iter = max_iter
        self.fig = plt.figure('K-Means Algorithm')

    def fit(self, dataset):
        # Randomly shuffle all rows
        dataset = dataset.sample(frac=1).reset_index(drop=True)
        
        # Select first k centroids from shuffled dataset
        self.centroids = []
        for i in range(self.k):
            self.centroids.append(dataset.iloc[i])

        for i in range(self.max_iter):
            pass

        ax = self.fig.add_subplot(1,1,1, projection='3d')
        ax.set_xlabel('Sepal length')
        ax.set_ylabel('Petal length')
        ax.set_zlabel('Petal width')
        ax.scatter(dataset['sepal_width'], dataset['petal_length'], dataset['petal_width'])
        for centroid in self.centroids:
            ax.scatter(centroid['sepal_width'], centroid['petal_length'], centroid['petal_width'], marker='x', color='r', s=50)
        plt.show()

    def predict(self):
        pass