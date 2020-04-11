import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math, random

def euclidean_distance(item_1, item_2):
    distance = math.sqrt((item_2[0] - item_1[0])**2 + (item_2[1] - item_1[1])**2)
    return distance

# Main k-neughbors classification algorithm
def find_k_neighbors(k, item, dataset):
    neighbor_distances = []
    for i in range(dataset.shape[0]):
        if (dataset.iloc[i].equals(item)):
            continue
        distance = euclidean_distance(item, dataset.iloc[i])
        neighbor_distances.append((i, distance))
    neighbor_distances.sort(key = lambda x: x[1])
    return neighbor_distances[0: k]

def main():
    # Read the iris dataset
    dataset = pd.read_csv("iris.csv")

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

    test_dataset = dataset.iloc[train_data_indexes]
    dataset.drop(train_data_indexes, inplace=True)

    correct = 0
    for i in range(test_dataset.shape[0]):
        result = find_k_neighbors(3, test_dataset.iloc[i], dataset)
        print(result)

    class_1 = dataset[dataset['species'] == 'setosa']
    class_2 = dataset[dataset['species'] == 'versicolor']
    class_3 = dataset[dataset['species'] == 'virginica']

    fig = plt.figure('k-nearest neighbors')
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.scatter(class_1['sepal_length'], class_1['sepal_width'], marker='x', color='r', label='Setosa')
    ax.scatter(class_2['sepal_length'], class_2['sepal_width'], marker='o', color='g', label='Versicolor')
    ax.scatter(class_3['sepal_length'], class_3['sepal_width'], marker='s', color='b', label='Virginica')
    ax.legend(loc='upper right')
    plt.show()

if __name__ == "__main__":
    main()