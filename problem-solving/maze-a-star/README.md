# Maze Solver using Minimax and Alpha-Beta prunning

This python implementation creates a random map and uses the A* (A-star)  algorithm to traverse it and find the faster possible path from the upper left point of the window to the lower right point.

![maze_map](/images/maze_a_star.png)

With each iteration, the most optimal path is shown on the window (purple line). The A* algorithm uses a min heap (or priority queue), which means it selects the path with the lowest value from the queue. In the implementation, nodes that are added to the frontier, the heap, are shown as green dots, while nodes in the open set are shown as red dots. Such items that exist in the open set are not further evaluated.
