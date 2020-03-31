import heapq, math
import maze

# h is the heuristic function. h(n) estimates the cost to reach goal from node n
def euclidean_distance(node_1, node_2):
    distance = math.sqrt((node_2.x - node_1.x)**2 + (node_2.y - node_1.y)**2)
    return distance

# Path reconstruction
def reconstruct_path(current):
    total_path  = []
    temp = current
    total_path.append(temp.x)
    total_path.append(temp.y)
    while temp.cameFrom != None:
        total_path.append(temp.cameFrom.x)
        total_path.append(temp.cameFrom.y)
        temp = temp.cameFrom
    return total_path

# A* finds a path from start to goal
def a_star(maze, start, goal, heuristic):
    start = maze.set_start(start)
    goal  = maze.set_goal(goal)

    start.gScore = 0
    start.fScore = heuristic(start, goal)

    # The set of discovered nodes that may need to be (re-)expanded
    openSet = []
    heapq.heappush(openSet, start)

    # List of nodes already discovered and explored
    closedSet = []

    while openSet:
        current = heapq.heappop(openSet)
        if current is goal:
            maze.update_path_line(reconstruct_path(current))
            return True
        closedSet.append(current)           # Add node to closed set
        maze.set_status_closed(current)     # Update canvas node's color
        for neighbor in current.neighbors:
            if not neighbor in closedSet and not neighbor.obstacle:
                tentative_gScore = current.gScore + heuristic(current, neighbor)
                # Check if neighbor is found with better gScore
                if neighbor in openSet:
                    if tentative_gScore < neighbor.gScore:
                        neighbor.gScore = tentative_gScore
                        neighbor.fScore = neighbor.gScore + heuristic(neighbor, goal)
                        neighbor.cameFrom = current
                else:
                    neighbor.gScore = tentative_gScore
                    neighbor.fScore = neighbor.gScore + heuristic(neighbor, goal)
                    neighbor.cameFrom = current
                    heapq.heappush(openSet, neighbor)       # Add node to open set
                    maze.set_status_open(neighbor)          # Update canvas node's color
        maze.update_path_line(reconstruct_path(current))
    return False

if __name__ == "__main__":
    maze = maze.Maze(800, 500, 80, 50)
    start = (0, 0)
    goal  = (79, 49)
    result = a_star(maze, start, goal, heuristic = euclidean_distance)
    maze.window.mainloop()
