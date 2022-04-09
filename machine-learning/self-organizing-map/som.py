import matplotlib.pyplot as plt
import seaborn as sns; sns.set()  # for plot styling
import numpy as np

# Euclidean Distance
def dist(item_1, item_2):
    distance = np.sqrt(np.sum((np.array(item_1) - np.array(item_2))**2))
    return distance

class Centroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return [self.x, self.y]
    
    def update(self, dx, dy):
        self.x += dx
        self.y += dy

class Grid:
    def __init__(self, size, g_range):
        self.size = size
        self.g_range = g_range
        self.values = [[None for _ in range(self.size)] for _ in range(self.size)]
        set_points = np.linspace(self.g_range[0], self.g_range[1], self.size)
        for i in range(len(set_points)):
            for j in range(len(set_points)):
                self.values[i][j] = Centroid(set_points[j], np.flip(set_points)[i])

    def get_winner(self, x):
        winner = None
        min_distance = 0
        for row in range(len(self.values)):
            for centroid in self.values[row]:
                centroid_dist = dist(x, centroid.get())
                if winner is None:
                    winner = centroid
                    min_distance = centroid_dist
                if centroid_dist < min_distance:
                    winner = centroid
                    min_distance = centroid_dist
        return winner

class SOM_Classifier:
    def __init__(self):
        self.max_iter   = 250
        self.alpha      = 0.02
        self.grid_size  = 5
        self.r          = 0.6
        self.sigma      = 0.5
        self.markers    = ['+', 'o', 'x', 'd', 's', 'p', 'v', '^']
        self.colors     = ['r', 'g', 'b', 'y', 'm', 'c', 'peru', 'lightgreen']

    def sigm(self, n):
        return self.sigma * np.exp(-n/200)

    # Neighbourhood function
    def h(self, x, n):
        return np.exp((-x**2)/(2*self.sigm(n)**2))

    def fit(self, dataset):
        grid = Grid(self.grid_size, [-1,1])

        for feature in range(len(dataset)):
            plt.scatter(dataset[feature][0], dataset[feature][1], c="b")
        temp_lines = []
        temp_points = []

        # SOM Algorithm
        for i in range(self.max_iter):
            convergence = True
            for x in range(len(dataset)):
                # Get most similar unit
                winner = grid.get_winner(dataset[x])

                # Find and update neighbour centroids
                for c_row in grid.values:
                    for centroid in c_row:
                        if dist(centroid.get(), winner.get()) < self.r:
                            centroid.update(self.alpha * self.h(dist(centroid.get(), winner.get()),i) * (dataset[x][0]-centroid.x),
                                            self.alpha * self.h(dist(centroid.get(), winner.get()),i) * (dataset[x][1]-centroid.y))

            # Plotting
            if len(temp_lines) != 0:
                for obj in temp_lines:
                    hh = obj.pop(0)
                    hh.remove()
            temp_lines.clear()
            if len(temp_points) != 0:
                for obj in temp_points:
                    obj.remove()
            temp_points.clear()

            for i in range(len(grid.values)):
                for j in range(len(grid.values[i])):
                    if i < len(grid.values) and j < len(grid.values[i]):
                        if i < len(grid.values)-1 and j < len(grid.values[i])-1:
                            temp_lines.append(plt.plot([grid.values[i][j].x, grid.values[i][j+1].x], [grid.values[i][j].y, grid.values[i][j+1].y], '-', c='black', zorder=1))
                            temp_lines.append(plt.plot([grid.values[i][j].x, grid.values[i+1][j].x], [grid.values[i][j].y, grid.values[i+1][j].y], '-', c='black', zorder=1))
                        elif i == len(grid.values)-1 and j < len(grid.values[i])-1:
                            temp_lines.append(plt.plot([grid.values[i][j].x, grid.values[i][j+1].x], [grid.values[i][j].y, grid.values[i][j+1].y], '-', c='black', zorder=1))
                        elif i < len(grid.values)-1 and j == len(grid.values[i])-1:
                            temp_lines.append(plt.plot([grid.values[i][j].x, grid.values[i+1][j].x], [grid.values[i][j].y, grid.values[i+1][j].y], '-', c='black', zorder=1))
                    temp_points.append(plt.scatter(grid.values[i][j].x, grid.values[i][j].y, c='black', s=120, alpha=0.8, zorder=2))
            plt.pause(0.01)
        plt.show()
