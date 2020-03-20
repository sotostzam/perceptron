# Perceptron Network

## What is a Perceptron

In the context of machine learning and neural networks, a perceptron is an artificial neuron utilizing an algorithm for supervised learning. It is the  simplest form of a neural network as it only contains a single layer, or neuron. For this reason it is often referred to as a single-layer perceptron, to distinguish it from a multi-layer perceptron, which is a more advanced and complex neural network.

Perceptron is a type of linear classifier, an algorithm that can predict and output a decision boundary on any given dataset, providing that the classes within this dataset are linearly separable. It also utilizes a feed-forward algorithm, as well as a linear predictor function to make predictions.

## How it works

![perceptron](/images/perceptron.png)

### Activation Function

Perceptron being a binary classifier makes use of an activation function, otherwise called a threshold function. This function maps any input to an output of 1 or -1.

```Math
f(x) = 1 if x >= 0,
      -1 otherwise
```

### Learning algorithm

The inputs to the perceptron are the dataset to be trained uppon, the desired outcome of each value of the dataset and a bias (usually being weight(0) or just 1).

The steps the algorithm is following are:

1. Firstly all weights are initialized to zero or a small random number.
2. For each value in the dataset calculate the actual output.
3. Update the weights.
4. Algorithm ends on these two scenarios:
   * If data are classified.
   * Or a specific number of iterations (epochs) has been reached.

During training of the algorithm, there is a plot showcasing the two classes. A line indicating the decision boundary is also depicted on the plot, which throughout the epochs, is updating until one of the two terminating scenarios is met. If the perceptron proves successful in finding a decision boundary, a line that linearly separates the two classes can be seen. An example is shown below:

![perceptron_plot](/images/perceptron_training.png)

## Python Implementation

With this implementation you can interact with the perceptron in the following ways:

* See current weights of the perceptron
* Train the Perceptron with a given dataset
* Give a test value to the perceptron and get a guess

Currently there are two datasets inside the "dataset" folder. The user has the option to choose between a custom random dataset and the popular "iris" dataset.

Your can read more about the "Iris" dataset by [clicking at this link](https://archive.ics.uci.edu/ml/datasets/Iris).
