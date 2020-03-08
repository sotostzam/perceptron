import numpy as np

class NeuralNetwork:

    # Define the sigmoid function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Default Constructor
    def __init__(self, input_nodes, hidden_nodes, output_nodes):
        self.input_nodes  = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes

        # Randomize weights from input -> hidden and hidden -> output layers
        self.weights_IH = -1 + np.random.rand(self.hidden_nodes, self.input_nodes) * 2
        self.weights_HO = -1 + np.random.rand(self.output_nodes, self.hidden_nodes) * 2

        # Randomize biases from input -> hidden and hidden -> output layers
        self.bias_H = -1 + np.random.rand(self.hidden_nodes, 1) * 2
        self.bias_O = -1 + np.random.rand(self.output_nodes, 1) * 2
        
    # Define Feed forward algorithm
    def feedForward(self, input):
        # Generating the hidden layer
        hidden = np.array(self.weights_IH.dot(input))               # Matrix multiplication between weights of Input to Hidden by the dataset
        hidden = np.add(hidden, self.bias_H)                        # Add the bias to the matrix
        hidden = np.array(list(map(self.sigmoid, hidden)))          # Pass every value of the matrix through the activation function

        # Generating the output layer
        output = np.array(self.weights_HO.dot(hidden))              # Matrix multiplication between weights of Hidden to Output by the dataset
        output = np.add(output, self.bias_O)                        # Add the bias to the matrix
        output = np.array(list(map(self.sigmoid, output)))          # Pass every value of the matrix through the activation function

        return output

# Create a neural network of 2 inputs, 2 hidden, and 1 output nodes
mlp = NeuralNetwork(2, 2, 1)

test_input = np.array([[1], [0]])
output = mlp.feedForward(test_input)
print(output)