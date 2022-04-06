import matplotlib.pyplot as plt
import seaborn as sns; sns.set()  # for plot styling
import numpy as np
import random

def euclidean_distance(item_1, item_2):
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

class K_Means_Classifier:
    def train(self, dataset, clusters):
        # Choose K (amount of clusters) random centroids from X (dataset)
        centroids = choose_random_sample(dataset, clusters)
        while True:
            # Cluster assignment
            clusters = {}
            for i in range(len(centroids)):
                clusters[i] = []

            for j in range(len(dataset)):
                distances = [euclidean_distance(centroids[n], dataset[j]) for n in range(len(centroids))]
                closest_centroid = distances.index(min(distances))
                clusters[closest_centroid].append(dataset[j])

            # Centroid Update
            old_centroids = centroids.copy()
            for cluster in clusters:
                centroids[cluster] = np.mean(clusters[cluster], axis = 0)

            if np.array_equal(old_centroids,centroids):
                break
        
        return clusters, centroids

    def fit(self, dataset, clusters):
        def calc_average_distance(comparator, cluster):
            average_score = 0
            for feature in cluster:
                average_score += euclidean_distance(comparator, feature)
            return average_score/len(cluster)

        # Compute data for elbow and silhouette plots by various k in {2 until 10% of dataset}
        elbow_rss = []
        silhouette_scores = []
        for iteration in range(2, int(10/100*len(dataset)+1)):
            clusters, centroids = self.train(dataset, iteration)
            current_rss=0
            silhouette_coefficients = []
            for cluster in clusters:
                for feature in clusters[cluster]:
                    # Compute residual sum of squares
                    current_rss += np.sum((feature-centroids[cluster])**2)/iteration

                    # Compute silhouette
                    avg_cluster = calc_average_distance(feature, clusters[cluster])

                    distances = {}
                    for nominee_cluster in clusters:
                        if nominee_cluster != cluster:
                            distance = calc_average_distance(feature, clusters[nominee_cluster])
                            distances[nominee_cluster] = distance

                    if len(distances) != 0:
                        closer_cluster = distances[min(distances, key=distances.get)]
                    else:
                        closer_cluster = avg_cluster

                    silhouette_coefficients.append((closer_cluster-avg_cluster)/max(closer_cluster, avg_cluster))
                
            silhouette_scores.append(sum(silhouette_coefficients) / len(silhouette_coefficients))
            elbow_rss.append(current_rss)

        # Run with best k found from Silhouette
        clusters, centroids = self.train(dataset, silhouette_scores.index(max(silhouette_scores))+2)
        
        markers = ['+', 'o', 'x', 'd', 's', 'p', 'v', '^']
        colors = ['r', 'g', 'b', 'y', 'm', 'c', 'peru', 'lightgreen']

        fig, axes = plt.subplots(1, 3, sharex=False, figsize=(15,5))
        #plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
        fig.tight_layout(rect=[0, 0.03, 1, 0.90])
        fig.suptitle('K-means Algorithm Analysis')
        msg_info = 'K-means with k ='+ str(silhouette_scores.index(max(silhouette_scores))+2)

        axes[0].set_title(msg_info)
        for cluster in clusters:
            for feature in clusters[cluster]:
                axes[0].scatter(feature[0], feature[1], c=colors[cluster], s=30)
            axes[0].scatter(centroids[cluster][0], centroids[cluster][1], c='black', s=150, alpha=0.6);
        
        axes[1].set_title('Elbow')
        axes[1].plot(range(2, int(10/100*len(dataset)+1)), elbow_rss)

        axes[2].set_title('Silhouette')
        axes[2].plot(range(2, int(10/100*len(dataset)+1)), silhouette_scores)

        plt.show()
