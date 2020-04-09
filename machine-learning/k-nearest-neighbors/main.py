import numpy as np
import matplotlib.pyplot as plt
import math

def euclidean_distance(item_1, item_2):
    distance = math.sqrt((item_2[0] - item_1[0])**2 + (item_2[1] - item_1[1])**2)
    return distance

def find_k_neighbors(k, item, dataset):
    neighbor_distances = []
    for i in range(len(dataset)):
        if (dataset[i] == item).all():
            continue
        distance = euclidean_distance(item, dataset[i])
        neighbor_distances.append((i, distance))
    neighbor_distances.sort(key = lambda x: x[1])
    return neighbor_distances[0: 5]

def main():
    # Read and generate the third and forth feature of the dataset
    dataset_values = np.genfromtxt('iris.data', delimiter=',', usecols=(0, 1))
    # Read and generate the names of the two classes
    dataset_target_names = np.genfromtxt('iris.data', delimiter=',', usecols=(4), dtype = np.str_)
    dataset_targets = np.zeros((dataset_target_names.shape[0], 1), dtype = float)
    # Iterate through the names and tranform them to two classes of -1 and 1
    for i in range (0, len(dataset_target_names)):
        if dataset_target_names[i] == "Iris-setosa":
            dataset_targets[i] = float(1)
        elif dataset_target_names[i] == "Iris-versicolor":
            dataset_targets[i] = float(2)
        else:
            dataset_targets[i] = float(3)
    dataset = np.column_stack((dataset_values, dataset_targets)) 

    # Test item
    test_item = find_k_neighbors(5, dataset[60], dataset)
    for item in test_item:
        print(dataset[item[0]])

    class_1 = np.where(dataset[:,2] == 1)
    class_2 = np.where(dataset[:,2] == 2)
    class_3 = np.where(dataset[:,2] == 3)

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