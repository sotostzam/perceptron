import numpy as np
import matplotlib.pyplot as plt

selection = -1         # User selection options
functionName = ''      # Holds function name for plot label
points = []            # List of locations
learning_rate = 0.03   # Define the learning rate (Good values are usually 0.01, 0.03 or 0.05)

text = '''
Please select function to run gradient descent upon:
1. 2*x*x*cos(x)-5*x
2. arctan(x^2)
3. x^2
4. x^3
5. 2*x^2-3*x+5
0. Quit
'''
print(text)

while True:
    try:
        selection = int(input("Enter your selection: "))
        if selection <= 5 and selection >= 0:
            # Check if selection made is exit
            if selection == 0:
                quit()
            # Initialize values for each function
            elif selection == 1:
                points.append(-1.4)
                functionName = "2*x*x*cos(x)-5*x"
            elif selection == 2: 
                points.append(-2.6)
                learning_rate = 0.2
                functionName = "arctan(x^2)"
            elif selection == 3: 
                points.append(4.5)
                learning_rate = 0.09
                functionName = "x^2"
            elif selection == 4: 
                points.append(4.9)
                learning_rate = 0.01
                functionName = "x^3"
            else               : 
                points.append(-4.5)
                learning_rate = 0.05
                functionName = "2*x^2-3*x+5"
            break
        else: 
            raise ValueError
    except ValueError:
        print("Wrong input specified.")
        print(text)
        pass

# Define f(x), the cost function to run the gradient descent algorithm on
def f(x):
    if   selection == 1: return 2 * x * x * np.cos(x) - 5 * x
    elif selection == 2: return np.arctan(x**2)
    elif selection == 3: return x ** 2
    elif selection == 4: return x ** 3
    else               : return 2 * x ** 2 - 3 * x + 5

# Define the derivative of the cost function in order to find the slope
def df(x):
    if   selection == 1: return 4 * x * np.cos(x) - 2 * x * x * np.sin(x) - 5
    elif selection == 2: return (2 * x) / (1 + x ** 4)
    elif selection == 3: return 2 * x
    elif selection == 4: return 3 * x ** 2
    else               : return 4 * x - 3

# Create 100 points, evenly spaced, starting from -5 up to 5 on the y axis
x = np.linspace(-5,5,100)

# Setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_title('Gradient Descent')
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# Define how many epochs (iterations) for the algorithm to run
for i in range(50):
    plt.clf()
    points.append(points[i] - learning_rate * df(points[i]))
    plt.grid()
    plt.plot(x, f(x), 'r', label=functionName)                           # Plot the function
    plt.plot([points[i]], f(points[i]), marker='o', color="blue")        # Plot the point
    plt.legend(loc='upper center')
    plt.pause(0.01)

    # Declare convergence if the derivative of the cost function is less than 0.001
    if (abs(df(points[-1])) < 10**(-3)):
        print("Iteration: " + str(i))
        print("Minimum found at x = " + str(round(points[-1], 2)))
        print("Convergence with value = " + str(round(df(points[i]), 5)))
        break

plt.show()