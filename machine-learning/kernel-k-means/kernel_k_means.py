import matplotlib.pyplot as plt
import seaborn as sns; sns.set()  # for plot styling
import numpy as np
import random

def choose_random_sample(dataset, clusters):
    sample = []
    sample_num = 0
    while sample_num < clusters:
        i = random.randrange(len(dataset))
        if i not in sample:
            sample.append(i)
            sample_num += 1
    return [dataset[i] for i in sample], np.random.randint(clusters, size=len(dataset))

class K_Means_Classifier:
    def __init__(self):
        self.markers = ['+', 'o', 'x', 'd', 's', 'p', 'v', '^']
        self.colors = ['r', 'g', 'b', 'y', 'm', 'c', 'peru', 'lightgreen']

    def k(self, item1, item2):
        return (np.dot(item1,item2)+0)**2   #TODO This should be +1 normally but needs further testing
        #return np.exp(-(np.linalg.norm(item1-item2)**2)/2*0.08**2)

    def calc_terms(self, member, cluster_members):
        total_ft = 0
        total_st = 0    # Mean of the number of elements in the kernel center
        for i in range(len(cluster_members)):
            total_st += self.k(member, cluster_members[i]) 
            for j in range(len(cluster_members)):
                total_ft += self.k(cluster_members[i], cluster_members[j])
        return total_ft/len(cluster_members)**2-2*total_st/len(cluster_members)

    def fit(self, dataset, num_clusters):
        self.dataset = dataset
        # Choose K (amount of clusters) random centroids from X (dataset)
        self.centroids, self.labels = choose_random_sample(self.dataset, num_clusters)
        while True:
            # Cluster identification
            clusters = {}
            for i in range(len(self.centroids)):
                clusters[i] = []
                for j in range(len(self.dataset)):
                    if self.labels[j] == i:
                        clusters[i].append(self.dataset[j])

            # Cluster assignmnet by using kernel functions
            for i in range(len(self.dataset)):
                distances = []
                for j in range(len(self.centroids)):
                    terms = self.calc_terms(dataset[i], clusters[j])
                    distances.append(self.k(dataset[i],dataset[i]) + terms)
                self.labels[i] = distances.index(min(distances))

            plt.clf()
            for i in range(len(self.dataset)):
                plt.scatter(self.dataset[i][0], self.dataset[i][1], c=self.colors[self.labels[i]], s=30)
            plt.pause(0.01)


