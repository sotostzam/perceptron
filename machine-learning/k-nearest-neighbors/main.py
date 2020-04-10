import numpy as np
import matplotlib.pyplot as plt
import math, random

def euclidean_distance(item_1, item_2):
    distance = math.sqrt((item_2[0] - item_1[0])**2 + (item_2[1] - item_1[1])**2)
    return distance

# Main k-neughbors classification algorithm
def find_k_neighbors(k, item, dataset):
    neighbor_distances = []
    for i in range(len(dataset)):
        if (dataset[i] == item).all():
            continue
        distance = euclidean_distance(item, dataset[i])
        neighbor_distances.append((i, distance))
    neighbor_distances.sort(key = lambda x: x[1])
    return neighbor_distances[0: k]

def main():
    # Read and generate the first and second feature of the dataset
    dataset_values = np.genfromtxt('iris.data', delimiter=',', usecols=(0, 1))
    # Read and generate the names of the two classes
    dataset_target_names = np.genfromtxt('iris.data', delimiter=',', usecols=(4), dtype = np.str_)
    dataset_targets = np.zeros((dataset_target_names.shape[0], 1), dtype = float)
    # Iterate through the names and tranform them to two classes of 0, 1 and 2
    for i in range (0, len(dataset_target_names)):
        if dataset_target_names[i] == "Iris-setosa":
            dataset_targets[i] = float(0)
        elif dataset_target_names[i] == "Iris-versicolor":
            dataset_targets[i] = float(1)
        else:
            dataset_targets[i] = float(2)

    # Final dataset with the values as well as the classes as the last column
    dataset = np.column_stack((dataset_values, dataset_targets))

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

    train_data = np.zeros([0, dataset.shape[1]])
    for i in range(len(train_data_indexes)):
        train_data = np.append(train_data, ([dataset[train_data_indexes[i]]]), 0)
    #dataset = np.delete(dataset, train_data_indexes, 0)

    class_1 = np.where(dataset[:,2] == 0)
    class_2 = np.where(dataset[:,2] == 1)
    class_3 = np.where(dataset[:,2] == 2)

    fig = plt.figure('k-nearest neighbors')
    ax = fig.add_subplot(1, 1, 1)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')

    ax.scatter(dataset_values[class_1, 0], dataset_values[class_1, 1], marker='x', color='r', label='Setosa')
    ax.scatter(dataset_values[class_2, 0], dataset_values[class_2, 1], marker='o', color='g', label='Versicolor')
    ax.scatter(dataset_values[class_3, 0], dataset_values[class_3, 1], marker='s', color='b', label='Virginica')
    ax.legend(loc='upper right')
    plt.show()

if __name__ == "__main__":
    main()