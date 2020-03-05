import numpy as np

# Perceptron Function
def f(x):
    if x > 0:
        return 1
    else:
        return -1

# Test data
x = np.array([[ 1.0, 1.0,  1.0,  1.0, 1.0,  1.0, 1.0, 1.0,  1.0, 1.0 ],
              [ 0.5, 1.0, -1.0, -2.0, 1.5, -1.5, 2.0, 0.0, 2.75, 1.0 ],
              [ 0.5, 2.0,  1.0,  1.0, 3.0,  3.5, 1.0, 3.0, 1.80, 3.0 ]
             ])
      
d = np.array([1.0, 1.0, -1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0])

# Randomize initial weights
w = -1 + np.random.rand(1,3) * 2  # Initialization of weights on [-1:1]
print("Initial weights:")
print(w)

flag = 1         
epochs = 0       # Starting iteration
maxEpochs = 10   # Max iterations
b = 0.2          # Learning rate

# Start of Percepton training
while flag < d.shape[0] and epochs < maxEpochs:
    for i in range (0, x.T.shape[1]):
        if flag < 10:
            eg=0
            for j in range(0, 3):
                c = w[0, j] * x[j, i]
                eg = eg + c
            u = f(eg)

            if u != d[i]:
                for j in range(0, 3):
                    w[0, j] = w[0, j] + b * (d[i] - u) * x[j, i]
                flag = 1
            else:
                flag = flag + 1

    epochs += 1
print("Trained weights:")
print(w)