import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

selection = -1         # User selection options
functionName = ''      # Holds function name for plot label
points = []            # List of locations
learning_rate = 0.0    # Define the learning rate (Good values are usually 0.01, 0.03 or 0.05)
convergence = []       # List representing history of convergence

text = '''
Please select function to run gradient descent upon:
1. Paraboloid            -> x^2+y^2
2. Himmelblau's function -> (x^2+7-11)^2+(x+y^2-7)^2
0. Quit
'''
print(text)

while True:
    try:
        selection = int(input("Enter your selection: "))
        if selection <= 2 and selection >= 0:
            # Check if exit action is selected
            if selection == 0:
                quit()
            # Initialize values for each function
            elif selection == 1:
                points.append([3.5, 3.5])
                learning_rate = 0.06
                functionName = "x^2+y^2"
            else:
                points.append([-1.2, -1.0])
                learning_rate = 0.005
                functionName = "Himmelblau's function"
            break
        else:
            raise ValueError
    except ValueError:
        print("Wrong input specified.")
        print(text)
        pass

# Define a multivirable function f(x, y), the cost function to run the gradient descent algorithm on
def f(x, y):
    if   selection == 1: return x ** 2 + y ** 2
    else               : return ((x ** 2 + y - 11) ** 2) + ((x + y ** 2 - 7) ** 2)

# Define the derivative of the cost function in order to find the slope
def df(x, y):
    if selection == 1:
        dfdx = 2 * x                                                # Partial derivative with respect to x
        dfdy = 2 * y                                                # Partial derivative with respect to y
    else:
        dfdx = 4 * x * (x ** 2 + y - 11) + 2 * (x + y ** 2 - 7)     # Partial derivative with respect to x
        dfdy = 2 * (x ** 2 + y - 11) + 4 * y * (x + y ** 2 - 7)     # Partial derivative with respect to y
    return dfdx, dfdy

if   selection == 1:
    x = np.linspace(-5, 5, 20)
    y = np.linspace(-5, 5, 20)
else:
    x = np.linspace(-6, 6, 20)
    y = np.linspace(-6, 6, 20)

X, Y = np.meshgrid(x, y)

fig = plt.figure(figsize=(10,8))

for i in range(50):
    # Update the location of the next value and the current convergence value
    points.append([points[i][0] - df(points[i][0], points[i][1])[0] * learning_rate, points[i][1] - df(points[i][0], points[i][1])[1] * learning_rate])
    convergence.append(df(points[i][0], points[i][1])[0] ** 2 + df(points[i][0], points[i][1])[1] ** 2)

    # Update plots
    plt.clf()
    ax = fig.add_subplot(2, 2, 1, projection='3d')
    ax.title.set_text(functionName)
    ax.contour3D(X, Y, f(X, Y), 50, cmap='coolwarm')                                                  # Plot the function in 3D
    ax.view_init(elev=40., azim=240)
    ax.scatter(points[i][0], points[i][1], f(points[i][0], points[i][1]), marker='o', color="red")    # Plot the point
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    ax2 = fig.add_subplot(2, 2, 2)
    ax2.set_title('Contour Map')
    cp = plt.contour(X, Y, f(X, Y), colors='black', linestyles='dashed', linewidths=1)                # Plot the line map
    plt.clabel(cp, inline=1, fontsize=10)
    cp = plt.contourf(X, Y, f(X, Y), 50, cmap='viridis')                                              # Plot the contour map
    ax2.plot(points[i][0], points[i][1], marker='o', color="red")                                     # Plot the point
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    
    ax3 = fig.add_subplot(2, 2, 3)
    ax3.set_title('Convergence')
    ax3.grid()
    ax3.plot(list(range(0, i+1)), convergence)

    ax4 = fig.add_subplot(2, 2, 4, frameon =False)
    ax4.table(colLabels = ['Iteration','Current Min','Convergence'],
              cellText=[[i, round(f(points[-1][0], points[-1][1]), 4), round(convergence[-1], 5)]],
              loc = 'center',
              cellLoc = 'center')
    ax4.axes.get_xaxis().set_visible(False)
    ax4.axes.get_yaxis().set_visible(False)

    plt.subplots_adjust(wspace=0.5)
    plt.pause(0.01)

    # Declare convergence if J(θ) decreases less than 10^(-3) (==0.001) in one iteration
    if (abs(convergence[-1]) < 10**(-3)):
        break

plt.show()