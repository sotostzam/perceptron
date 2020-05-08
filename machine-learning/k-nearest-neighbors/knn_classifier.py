import math, random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter
style.use('seaborn')

# Eucledean Distance using all dimentions
def euclidean_distance(item_1, item_2):
    distance = np.sqrt(np.sum((np.array(item_1) - np.array(item_2))**2))
    return distance

class KNN_Classifier:
    def __init__(self, k):
        self.fig = plt.figure(str(k) + '-Nearest Neighbors')
        self.ax = self.fig.add_subplot(1,1,1, projection='3d')
        self.colors = {'setosa': 'm', 'versicolor': 'g', 'virginica': 'b'}
        self.k = k

    def visualize(self):
        # Find the different species from the dataset
        class_1 = self.dataset[self.dataset['species'] == 'setosa']
        class_2 = self.dataset[self.dataset['species'] == 'versicolor']
        class_3 = self.dataset[self.dataset['species'] == 'virginica']
        self.ax.set_xlabel('Sepal length')
        self.ax.set_ylabel('Petal length')
        self.ax.set_zlabel('Petal width')
        self.ax.scatter(class_1['sepal_width'], class_1['petal_length'], class_1['petal_width'], marker='p', color=self.colors['setosa'], label='Setosa')
        self.ax.scatter(class_2['sepal_width'], class_2['petal_length'], class_2['petal_width'], marker='o', color=self.colors['versicolor'], label='Versicolor')
        self.ax.scatter(class_3['sepal_width'], class_3['petal_length'], class_3['petal_width'], marker='d', color=self.colors['virginica'], label='Virginica')

        # Get unique labels only
        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = dict(zip(labels, handles))

        self.ax.legend(by_label.values(), by_label.keys(), loc='upper left')
        plt.show()

    # Fit k-neughbors model to database
    def fit(self, dataset, train_percent = 0.2):
        # Randomly shuffle all rows
        dataset = dataset.sample(frac=1).reset_index(drop=True)
        percentage = train_percent * dataset.shape[0]

        self.dataset = dataset.drop(dataset.index[-int(percentage): dataset.shape[0]], axis=0)
        self.test_dataset = dataset.drop(dataset.index[0: -int(percentage)], 0).reset_index(drop=True)

    # Get a prediction on a simple value
    def predict(self, item, withConfidence = True):
        neighbor_distances = []
        for i in range(self.dataset.shape[0]):
            # If it is the same item ignore it and move on
            if (self.dataset.iloc[i].equals(item)):
                continue
            else:
                current_distance = euclidean_distance(item, self.dataset.iloc[i].drop(['species'], axis = 0))
                neighbor_distances.append((current_distance, self.dataset.iloc[i].species))

        # Use counter to count all unique species
        counts = Counter(x[1] for x in sorted(neighbor_distances, key=lambda x: x[0])[0:self.k])
        if withConfidence:
            print("Prediction: " + str(counts.most_common(1)[0][0]) + 
                  ", Confidence: " + str((counts.most_common(1)[0][1]/self.k)*100) + "%")
        else:
            return counts.most_common(1)[0][0]

    # Helper function to get the accuracy by using the test_dataset on the model
    def accuracy(self):
        correct = 0
        for i in range(self.test_dataset.shape[0]):
            item = self.test_dataset.iloc[i]
            # Get prediction on the test sample
            result = self.predict(item.drop(['species'], axis = 0), False)
            if result == item.species:
                correct += 1
                self.ax.scatter(item['sepal_width'], item['petal_length'], item['petal_width'], marker='*', color=self.colors[result])
            else:
                self.ax.scatter(item['sepal_width'], item['petal_length'], item['petal_width'], marker='x', color='r', label='Misclassified')
        return round((correct/self.test_dataset.shape[0])*100, 2)
