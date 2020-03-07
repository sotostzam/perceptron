import os
import numpy as np
import perceptron

# Create a single perceptron
neuron = perceptron.Perceptron(maxEpochs = 10, learning_rate = 0.1)

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
            dataset = np.genfromtxt('dataset.csv', delimiter=',')
            neuron.train(dataset)
        elif selection == 3:
            point_x = int(input("Enter point's x: "))
            point_y = int(input("Enter point's y: "))
            guess_point = np.array([1, point_x, point_y])
            neuron.guess(guess_point)
        else: 
            raise ValueError
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Wrong input specified.\n")
        pass