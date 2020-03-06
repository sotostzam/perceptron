import numpy as np

# Neuron Activation Function (Step function -1/1)
def f(u):
    if u > 0:
        return 1
    else:
        return -1

# Sample data
x = np.array([[ 1.0, 1.0,  1.0,  1.0, 1.0,  1.0, 1.0, 1.0,  1.0, 1.0 ],   # Augmented row
              [ 0.5, 1.0, -1.0, -2.0, 1.5, -1.5, 2.0, 0.0, 2.75, 1.0 ],   # X values
              [ 0.5, 2.0,  1.0,  1.0, 3.0,  3.5, 1.0, 3.0, 1.80, 3.0 ]    # Y values
             ])

# Array representing the desired output of the neuron        
d = np.array([1.0, 1.0, -1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0])

# Initialize parameters
w = -1 + np.random.rand(3) * 2      # Initialize random weights on range [-1:1]    
maxEpochs = 10                      # Max iterations
b = 0.1                             # Learning rate

print("Initial weights:\t" + str(w))

# Start of Percepton training
for epoch in range (0, maxEpochs):                          # Iterate through the epochs given
    convergence = True                                      # Convergence value (True | False)
    for p in range (0, x.T.shape[0]):                       # Iterate through each sample
        result = 0
        for i in range (0, len(w)):
            result += w[i] * x[i, p]
        u = f(result)
        if u != d[p]:                                       # Check if sample is misclassified
            for i in range(0, len(w)):
                w[i] = w[i] + b * (d[p] - u) * x[i, p]      # Update weights
            convergence = False
    if convergence == True:
        break

print("Trained weights:\t" + str(w))