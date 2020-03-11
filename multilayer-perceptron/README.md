# Multilayer Perceptron (MLP)

## What is a multi-layer perceptron

A multi-layer perceptron is a class of feedforward neural network, used on the field of supervised learning. It consists of multiple layers of perceptrons, with the minmum amount being three: one input, one or more hidden layers and one output layer. It is different than a single-layer perceptron, because it can distinguish non linearly separable data.

## How it works

![perceptron](/images/mlp.png)

### Activation Function

Multi-layer perceptrons can utilize an activation function, called a sigmoid, which can map the input to an output of 0 or 1.

```Math
f(x) = 1 / (1 + e^(-x))
```

### Layers

A multilayer perceptron has three types of layers. An input layer, which is where different datasets are passed into the algorithm, one or more hidden layers, which are all connected with each other, and an output layer which depicts the decision boundaries for the problem each mlp solves.

### Learning algorithm

The inputs to the perceptron are the dataset to be trained uppon, the desired outcome of each value of the dataset and a bias (usually being weight(0) or just 1).

This type of neural network also utilize backpropagation, an algorithm used in training feedforward neural networks for supervised learning. It is a technique which updates the weights by computing the gradient of the loss function with respect to each one of them. The computation is happening on each layer, iterating backwards and starting from the last layer.

During the training of the neural network, there is a plot showcasing the decision boundaries. throughout the epochs, these lines are being updated for a specific time of epochs that the MLP is trained for. An example of such a plot is shown below:

![perceptron_plot](/images/mlp_training.png)

## Python Implementation

This implementation shows how a multi-layer perceptron can solve the problem of the XOR gate, and give decision boundaries based on the training data of the gate. This is a problem which can not be solved with the use of a single layer perceptron.
