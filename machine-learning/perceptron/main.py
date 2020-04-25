import os
import numpy as np
import perceptron

def load_dataset(option):
    if option == 2:
        dataset = np.genfromtxt('datasets/classification_pixel_data.csv', delimiter=',')
        augmented_matrix = np.ones((dataset.shape[0], 1), dtype = float)
        augmented_matrix = np.column_stack((augmented_matrix, dataset))
        return augmented_matrix.T
    elif option == 1:
        # Read and generate the third and forth feature of the dataset
        dataset_values = np.genfromtxt('datasets/iris.data', delimiter=',')[0:100, [2,3]]
        
        # Read and generate the names of the two classes
        dataset_target_names = np.genfromtxt('datasets/iris.data', delimiter=',', dtype = np.str_)[0:100, [4]]
        dataset_targets = np.zeros((dataset_target_names.shape[0], 1), dtype = float)

        # Iterate through the names and tranform them to two classes of -1 and 1
        for i in range (0, len(dataset_target_names)):
            if dataset_target_names[i] == "Iris-setosa":
                dataset_targets[i] = float(-1)
            else:
                dataset_targets[i] = float(1)

        # Initialize the augmented matrix that contains the bias as the first column and the targets as the last column
        augmented_matrix = np.ones((dataset_values.shape[0], 1), dtype = float)
        augmented_matrix = np.column_stack((augmented_matrix, dataset_values)) 
        augmented_matrix = np.column_stack((augmented_matrix, dataset_targets))
        return augmented_matrix.T
    else:
        return np.genfromtxt('datasets/custom_dataset.csv', delimiter=',')

def showMenu():
    while True:
        try:
            print("Please enter your choice:\n" +
                "1. Show weights\n" +
                "2. Train Perceptron\n" +
                "3. Guess value\n" +
                "0. Quit application\n")
            selection = int(input("Your selection: "))
            os.system('cls' if os.name == 'nt' else 'clear')
            if selection == 0:
                quit()
            if selection == 1:
                neuron.show_weights()
            elif selection == 2:
                print("Please enter your choice:\n" +
                    "1. Iris dataset\n" +
                    "2. Pixel classification dataset\n" +
                    "3. Custom test dataset\n")
                selection = int(input("Your selection: "))
                if selection > 0 and selection < 4: 
                    dataset = load_dataset(selection)
                    neuron.train(dataset)
            elif selection == 3:
                point_x = int(input("Enter point's x: "))
                point_y = int(input("Enter point's y: "))
                prediction = neuron.guess(np.array([1, point_x, point_y]))
                print("Perceptron's class prediction: " + prediction + ".\n")
            else: 
                raise ValueError
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Wrong input specified.\n")
            pass

if __name__ == "__main__":
    # Create a single perceptron with 2 features
    neuron = perceptron.Perceptron(maxEpochs = 3000, learning_rate = 0.1, features = 2)
    showMenu()
