import matplotlib.pyplot as plt
import seaborn as sns; sns.set()  # for plot styling
import numpy as np
import random

# Euclidean Distance
def dist(item_1, item_2):
    distance = np.sqrt(np.sum((np.array(item_1) - np.array(item_2))**2))
    return distance

def choose_random_sample(dataset, clusters):
    sample = []
    sample_num = 0
    while sample_num < clusters:
        i = random.randrange(len(dataset))
        if i not in sample:
            sample.append(i)
            sample_num += 1
    return [dataset[i] for i in sample]

class C_Means_Classifier:
    def __init__(self, epsilon = 0.01, alpha = 2):
        self.epsilon = epsilon
        self.alpha = alpha
        self.markers = ['+', 'o', 'x', 'd', 's', 'p', 'v', '^']
        self.colors = ['r', 'g', 'b', 'y', 'm', 'c', 'peru', 'lightgreen']

    def is_centroid(self, sample):
        for centroid in self.centroids:
            if np.array_equal(centroid, sample):
                return True
        return False

    def fit(self, dataset, clusters):
        # Choose K (amount of centroids) random centroids from X (dataset)
        self.centroids = choose_random_sample(dataset, clusters)
        U = np.random.rand(len(dataset), clusters)
                
        while True:
            # Calculate fuzzy centroids
            for j in range(len(self.centroids)):
                nom = den = 0
                for i in range(len(dataset)):
                    nom += U[i,j]**self.alpha*dataset[i]
                    den += U[i,j]**self.alpha
                self.centroids[j] = nom/den

            # Calculate membership matrix values
            old_U = U.copy()
            for i in range(len(dataset)):
                for j in range(len(self.centroids)):
                    total_membership = 0
                    for k in range(len(self.centroids)):
                        total_membership += dist(dataset[i], self.centroids[j])/(dist(dataset[i], self.centroids[k]))
                    U[i,j] = 1/total_membership**(2/(self.alpha-1))

            # Clustering Loss
            c_loss = 0
            for i in range(len(dataset)):
                for j in range(len(self.centroids)):
                    c_loss += (U[i,j]**self.alpha)*dist(dataset[i], self.centroids[j])**2

            # Check for stability
            dist_U = np.linalg.norm(old_U-U)
            if dist_U < self.epsilon:
                print('Clustering loss is', c_loss)
                break

        for feature in range(len(dataset)):
            if not self.is_centroid(dataset[feature]):
                plt.scatter(dataset[feature][0], dataset[feature][1], c=self.colors[np.argmax(U[feature,:])], marker=self.markers[np.argmax(U[feature,:])], alpha=np.max(U[feature,:]))
        
        for c in range(len(self.centroids)):
            plt.scatter(self.centroids[c][0], self.centroids[c][1], c='black', s=150, alpha=0.6)

        plt.show()
