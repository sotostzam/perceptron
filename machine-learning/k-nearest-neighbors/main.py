import pandas as pd
import matplotlib.pyplot as plt
import math, random
from collections import Counter

def euclidean_distance(item_1, item_2):
    distance = math.sqrt((item_2[2] - item_1[2])**2 + (item_2[3] - item_1[3])**2)
    return distance

# Main k-neughbors classification algorithm
def k_neighbors_guess(k, item, dataset):
    neighbor_distances = []
    for i in range(dataset.shape[0]):
        # If it is the same item ignore it and move on
        if (dataset.iloc[i].equals(item)):
            continue
        else:
            current_distance = euclidean_distance(item, dataset.iloc[i])
            if len(neighbor_distances) < k:
                neighbor_distances.append((current_distance, dataset.iloc[i].species))
            else:
                for j in range(len(neighbor_distances)):
                    if neighbor_distances[j][0] > current_distance:
                        del neighbor_distances[j]
                        neighbor_distances.append((current_distance, dataset.iloc[i].species))
                        break
    # Use counter to count all unique species
    counts = Counter(x[1] for x in neighbor_distances)
    return counts.most_common(1)[0][0]

def main(neighbors):
    # Read the iris dataset
    dataset = pd.read_csv("iris.csv")
    training_dataset = dataset.copy()

    # Randomly pick 10 samples (20%) of each species and remove from dataset
    train_data_indexes = []
    while len(train_data_indexes) < 30:
        first = random.randint(0, 49)
        second = random.randint(50, 99)
        third = random.randint(100, 149)
        if first in train_data_indexes or second in train_data_indexes or third in train_data_indexes:
            pass
        else:
            train_data_indexes.append(first)
            train_data_indexes.append(second)
            train_data_indexes.append(third)

    test_dataset = training_dataset.iloc[train_data_indexes]
    training_dataset.drop(train_data_indexes, inplace=True)

    # Find the different species from the dataset
    class_1 = training_dataset[training_dataset['species'] == 'setosa']
    class_2 = training_dataset[training_dataset['species'] == 'versicolor']
    class_3 = training_dataset[training_dataset['species'] == 'virginica']

    fig = plt.figure(str(neighbors) + '-Nearest Neighbors')
    correct = 0
    for i in range(test_dataset.shape[0]):
        # Get a guess on the test sample
        result = k_neighbors_guess(neighbors, test_dataset.iloc[i], training_dataset)
        for j in range(dataset.shape[0]):
            if test_dataset.iloc[i].equals(dataset.iloc[j]) and test_dataset.iloc[i].species == result:
                correct += 1
                break

        plt.clf()
        ax = fig.add_subplot(1, 1, 1)
        ax.set_xlabel('Petal length')
        ax.set_ylabel('Petal width')
        ax.scatter(class_1['petal_length'], class_1['petal_width'], marker='x', color='r', label='Setosa')
        ax.scatter(class_2['petal_length'], class_2['petal_width'], marker='o', color='g', label='Versicolor')
        ax.scatter(class_3['petal_length'], class_3['petal_width'], marker='^', color='b', label='Virginica')
        ax.scatter(test_dataset.iloc[i][2], test_dataset.iloc[i][3], marker='s', color='y', label='Test sample')
        ax.legend(loc='upper left')
        plt.pause(0.001)

    print("Training results using " + str(neighbors) + " nearest neighbors: " + str(correct) + "/" +
          str(test_dataset.shape[0]) + " (" + str(round((correct/test_dataset.shape[0])*100, 2)) + "%)")
    plt.show()

if __name__ == "__main__":
    main(neighbors = 3)