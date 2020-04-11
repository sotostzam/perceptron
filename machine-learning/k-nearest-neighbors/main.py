import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math, random

def euclidean_distance(item_1, item_2):
    distance = math.sqrt((item_2[0] - item_1[0])**2 + (item_2[1] - item_1[1])**2)
    return distance

# Main k-neughbors classification algorithm
def k_neighbors_guess(k, item, dataset):
    neighbor_distances = pd.DataFrame(columns = dataset.columns)
    for i in range(dataset.shape[0]):
        if (dataset.iloc[i].equals(item)):
            continue
        if neighbor_distances.shape[0] < k:
            neighbor_distances = neighbor_distances.append(dataset.iloc[i], ignore_index = True)
        else:
            for j in range(neighbor_distances.shape[0]):
                if euclidean_distance(item, neighbor_distances.iloc[j]) > euclidean_distance(item, dataset.iloc[i]):
                    neighbor_distances.drop([j], inplace=True)
                    neighbor_distances = neighbor_distances.append(dataset.iloc[i], ignore_index = True)
    return neighbor_distances.groupby('species').size().idxmax()

def main():
    # Read the iris dataset
    dataset = pd.read_csv("iris.csv")
    training_dataset = dataset.copy()

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

    class_1 = training_dataset[training_dataset['species'] == 'setosa']
    class_2 = training_dataset[training_dataset['species'] == 'versicolor']
    class_3 = training_dataset[training_dataset['species'] == 'virginica']

    correct = 0
    for i in range(test_dataset.shape[0]):
        result = k_neighbors_guess(3, test_dataset.iloc[i], dataset)
        for j in range(dataset.shape[0]):
            if test_dataset.iloc[i].equals(dataset.iloc[j]) and test_dataset.iloc[i].species == result:
                correct += 1
                break

        fig = plt.figure('k-nearest neighbors')
        plt.clf()
        ax = fig.add_subplot(1, 1, 1)
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.scatter(class_1['sepal_length'], class_1['sepal_width'], marker='x', color='r', label='Setosa')
        ax.scatter(class_2['sepal_length'], class_2['sepal_width'], marker='o', color='g', label='Versicolor')
        ax.scatter(class_3['sepal_length'], class_3['sepal_width'], marker='s', color='b', label='Virginica')
        ax.scatter(test_dataset.iloc[i][0], test_dataset.iloc[i][1], marker='s', color='y')
        ax.legend(loc='upper right')
        plt.pause(0.1)

    print("Training results: " + str(correct) + "/" + str(test_dataset.shape[0]) + " (" + str(round((correct/test_dataset.shape[0])*100, 2)) + "%)")
    plt.show()

if __name__ == "__main__":
    main()