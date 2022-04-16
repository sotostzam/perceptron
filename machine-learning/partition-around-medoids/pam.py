import matplotlib.pyplot as plt
import seaborn as sns; sns.set()  # for plot styling
import numpy as np

# Euclidean Distance
def dist(item_1, item_2):
    distance = np.sqrt(np.sum((np.array(item_1) - np.array(item_2))**2))
    return distance

def choose_best_sample(dataset):
    best_sample = 0
    best_distance = np.inf
    for i in range(len(dataset)):
        distance = 0
        for j in range(len(dataset)):
            if i != j:
                distance += dist(dataset[i], dataset[j])
        if distance < best_distance:
            best_distance = distance
            best_sample = i
    return best_sample

class PAM_Classifier:
    def __init__(self):
        self.medoids = []

    def closest_medoid(self, sample):
        distances = [dist(self.medoids[i], sample) for i in range(len(self.medoids))]
        return min(distances)

    def sec_closest_medoid(self, sample):
        distances = [dist(self.medoids[i], sample) for i in range(len(self.medoids))]
        return sorted(distances)[1]
    
    def is_medoid(self, sample):
        for medoid in self.medoids:
            if np.array_equal(medoid, sample):
                return True
        return False

    def cluster_pop(self, label):
        count = 0
        for i in self.labels:
            if i == label:
                count+=1
        return count

    def fit(self, dataset, clusters):
        # Initialization
        self.medoids = [dataset[choose_best_sample(dataset)]]
        self.labels = [0] * len(dataset)
        self.markers = ['D', 'o', 'X', 'd', 's', 'p', 'v', '^']
        self.colors = ['r', 'g', 'b', 'y', 'm', 'c', 'peru', 'lightgreen']

        # BUILD algorithm
        curr_medoid = 1
        while curr_medoid < clusters:
            total_contribution = {}
            for candidate in range(len(dataset)):
                contributions = {}
                for voter in range(len(dataset)):
                    if not np.array_equal(dataset[voter], dataset[candidate]) and not self.is_medoid(dataset[voter]):
                        C_ij = max(self.closest_medoid(dataset[voter])-dist(dataset[candidate], dataset[voter]), 0)
                        contributions[voter] = C_ij
                total_contribution[candidate] = sum(contributions.values())
            self.medoids.append(dataset[max(total_contribution, key=total_contribution.get)])
            curr_medoid += 1
                
        use_swap = False
        if not use_swap: print('SWAP step did not run!')
        # SWAP algorithm
        while True and use_swap:
            best_contribution = []                     # List of [(i,h), C(i,h)]
            for i in range(len(self.medoids)):         # i medoid
                for h in range(len(dataset)):          # h non medoid candidate
                    if not self.is_medoid(dataset[h]):
                        contribution = 0
                        for j in range(len(dataset)):  # j is a voter, not medoid or candidate
                            if j != h and not np.array_equal(dataset[j], self.medoids[i]) and not self.is_medoid(dataset[j]):

                                # Compute contribution of each voter j to the swap of medoid i by the candidate h
                                if self.closest_medoid(dataset[j]) < min(dist(dataset[j], self.medoids[i]), dist(dataset[j], dataset[h])):
                                    # voter is neutral
                                    contribution += 0
                                elif dist(dataset[j], dataset[h]) < min(dist(dataset[j], self.medoids[i]), self.closest_medoid(dataset[j])):
                                    # voter agrees
                                    contribution += dist(dataset[j], dataset[h]) - min(dist(dataset[j], self.medoids[i]), self.closest_medoid(dataset[j]))
                                elif dist(dataset[j], self.medoids[i]) < min(dist(dataset[j], dataset[h]), self.closest_medoid(dataset[j])):
                                    # voter disagrees
                                    if dist(dataset[j], dataset[h]) < self.closest_medoid(dataset[j]):
                                        contribution += dist(dataset[j], dataset[h]) - dist(dataset[j], self.medoids[i])
                                    else:
                                        contribution += self.closest_medoid(dataset[j]) - dist(dataset[j], self.medoids[i])
                                   
                        if not best_contribution or contribution < best_contribution[1]:
                           best_contribution = [(i,h), contribution]

            if best_contribution[1] > 0:
                break
            else:
                print('[SWAP]', best_contribution[0], '\tTotal C:', best_contribution[1])
                self.medoids[best_contribution[0][0]] = dataset[best_contribution[0][1]]

        # Assign clusters to voters
        for voter in range(len(dataset)):
            if not self.is_medoid(dataset[voter]):
                distances = [dist(self.medoids[n], dataset[voter]) for n in range(len(self.medoids))]
                self.labels[voter] = distances.index(min(distances))

        # Calculate silhouette scores
        silhouette_scores = [0] * len(dataset)
        for i in range(len(dataset)):

            a = 0
            for j in range(len(dataset)):
                if i != j:
                    if self.labels[i] == self.labels[j]:
                        a += dist(dataset[i], dataset[j])
            a = a/self.cluster_pop(self.labels[i])             # How well i is assigned to its cluster

            b = 0
            cluster_means = []
            for c in range(len(self.medoids)):
                if c != self.labels[i]:
                    cluster_dist = 0
                    for j in range(len(dataset)):
                        if self.labels[j] == c:
                            cluster_dist += dist(dataset[i], dataset[j])
                    cluster_means.append(cluster_dist/self.cluster_pop(self.labels[c]))
            b = min(cluster_means)

            if self.cluster_pop(self.labels[i]) > 1:
                s = (b-a)/(max(a,b))
            else:
                s = 0

            silhouette_scores[i] = s

        # Plotting
        clusters = {}
        for cluster in range(len(self.medoids)):
            samples = []
            for sample in range(len(dataset)):
                if self.labels[sample] == cluster:
                    samples.append((sample, silhouette_scores[sample]))
            clusters[cluster] = sorted(samples,key=lambda x: x[1])

        fig, axes = plt.subplots(1, 2, sharex=False, figsize=(13,7))
        fig.tight_layout(rect=[0, 0.03, 1, 0.90])
        fig.suptitle('PAM (k-medoids) Algorithm Analysis')

        axes[0].set_title('PAM Clusters')
        for feature in range(len(dataset)):
            if not self.is_medoid(dataset[feature]):
                axes[0].scatter(dataset[feature][0], dataset[feature][1], c=self.colors[self.labels[feature]], s=30, marker=self.markers[self.labels[feature]])
        
        for medoid in range(len(self.medoids)):
            axes[0].scatter(self.medoids[medoid][0], self.medoids[medoid][1], c=self.colors[medoid], edgecolors='black', s=50, marker=self.markers[medoid])

        axes[1].set_title('Silhouette plot')
        axes[1].set_xlim([-1, 1])
        pos = 0
        for cluster in range(len(clusters)):
            for sample in clusters[cluster]:
                axes[1].barh(pos, sample[1], color=self.colors[self.labels[sample[0]]], edgecolor='none')
                pos+=1
        plt.show()
