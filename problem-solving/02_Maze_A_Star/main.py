import heapq
import maze

def a_star(maze):
    start = maze.grid[0][0]
    goal = maze.grid[len(maze.grid)-1][len(maze.grid[0])-1]
    start.obstacle = False
    goal.obstacle = False

    start.gScore = 0
    start.fScore = maze.evaluate(start, goal)

    # The set of discovered nodes that may need to be (re-)expanded
    openSet = []
    heapq.heappush(openSet, start)

    # List of nodes already discovered and explored
    closedSet = []

    pathLine = maze.canvas.create_line(0, 0, 0, 0)
    while openSet:
        current = heapq.heappop(openSet)

################################ CANVAS UPDATE ###################################
        path = []
        temp = current
        path.append(temp.x)
        path.append(temp.y)
        while temp.cameFrom != None:
            path.append(temp.cameFrom.x)
            path.append(temp.cameFrom.y)
            temp = temp.cameFrom
        maze.canvas.delete(pathLine)
        if len(path) > 2:
            pathLine = maze.canvas.create_line(path, width = 6, fill = 'purple')
##################################################################################

        if current is goal:
            return True
        closedSet.append(current)
        maze.canvas.itemconfig(current.obj, fill='red')
        for neighbor in current.neighbors:
            if not neighbor in closedSet and not neighbor.obstacle:
                tentative_gScore = current.gScore + maze.evaluate(current, neighbor)
                # Check if neighbor is found with better gScore
                if neighbor in openSet:
                    if tentative_gScore < neighbor.gScore:
                        neighbor.gScore = tentative_gScore
                        neighbor.fScore = neighbor.gScore + maze.evaluate(neighbor, goal)
                        neighbor.cameFrom = current
                else:
                    neighbor.gScore = tentative_gScore
                    neighbor.fScore = neighbor.gScore + maze.evaluate(neighbor, goal)
                    neighbor.cameFrom = current
                    heapq.heappush(openSet, neighbor)
                    maze.canvas.itemconfig(neighbor.obj, fill='green')
        maze.canvas.update()
    return False

if __name__ == "__main__":
    maze = maze.Maze(800, 500, 80, 50)
    result = a_star(maze)
    maze.window.mainloop()
