# Search Algorithms

Given a problem with a state space, a search algorithm's purpose is to find the solution. All algorithms that try to find a solution are called search algorithms. These algorithms fall into the following categories:

## Table of contents

* [Uninformed Search Algorithms](#uninformed-search-algorithms)
  * [Breadth-first search](#breadth-first-search)
  * [Depth-first search](#depth-first-search)
  * [Uniform cost search](#uniform-cost-search)
* [Informed Search Algorithms](#informed-search-algorithms)
  * [Hill Climbing](#hill-climbing)
  * [Best First Search](#best-first-search)
* [Time and space complexities](#time-and-space-complexities)
* [Implementation](#implementation)

## Uninformed Search Algorithms

These kinds of algorithms are also called blind search algorithms. These algorithms do not take into account the information about the evaluation of each state. So they act in the same way to solve any problem, and they only care about the timing that each state is created. Some of these algorithms are state below:

### Breadth-first search

Breadth-first search (BFS) is a uninformed search algorithm. It examines all possible states on the same level first, and then moves to the next level. BFS uses a FIFO queue structure (First In First Out) for keeping track of its search frontier. On each iteration the algorithm searches all the states being on the lower depth, as these states were inserted first in the queue. If a node that is attached via an edge has already been discovered, the algorithm ignores it and moves on.

We can assume the pseudocode for the breadth-first search algorithm as following:

```Pseudocode
algorithm bfs_search(graph, origin, target)
    frontier <- Is a queue
    label origin as discovered
    frontier.push(origin)
    while Q is not empty do
        current := frontier.pop()
        if current is target then
            return success
        for all adjacentEdges(edge) from current do
            if edge is not discovered then
                label edge as discovered
                edge.parent := current
                frontier.enqueue(edge)
    return failure
```

The biggest advantage of the BFS algorithm is that it finds the smallest possible route, meaning the route with the least amount of edges. This solution can only be described as best if all edges have the same cost. Moreover, the bfs algorithm is considered as "complete", as i will always find a solution if there is one. One disadvantage is that the search frontier of the bfs algorithm is increasing a lot in size, which means that it needs a lot more memory space.

### Depth-first search

Like the name of this algorithm suggests, depth-first search (DFS) is an uninformed search algorithm which examines all possible states that exist in the deeper layers of the tree. If there is more than one state at the same depth, it randomly chooses the next or picks the one on the left for ease.

The search frontier this algorithm uses, is a LIFO stack structure (Last In First Out). This means that on each iteration, every new state gets added to the top of the stack, and the search procedure continues with one of them. If a node that is attached via an edge has already been discovered, the algorithm ignores it and moves on.

We can assume the pseudocode for the depth-first search algorithm as following:

```Pseudocode
algorithm dfs_search(graph, origin, target)
    frontier <- Is a stack
    frontier.push(origin)
    while frontier is not empty do
        current = frontier.pop()
        if current is not discovered then
            label current as discovered
            if current is target:
                return success
            for all adjacentEdges(edge) from current do
                frontier.push(edge)
    return failure
```

The DFS algorithm has the advantage of not consuming too many resources when it comes to space. The search frontier does not increase by that much on each iteration, so its memory for upcoming search states is relatively small. However, this algorithm does not guarantee that the first solution found, is also the best. What is more, it can be stuck in a loop if there are branches of a tree with infinite length.

### Uniform Cost search

Unlike the BFS, uniform-cost search doesn’t care about the number of steps that each of the paths it searches has, but the total path cost. Therefor, it uses a priority queue. This means that the path that is selected from the frontier is the one with the lowest cost value so far.

We can assume the pseudocode for the uniform cost search algorithm as following:

```Pseudocode
algorithm ucs_search(graph, origin, target)
    frontier <- Is a priority queue
    frontier.push(origin, 0)
    while frontier is not empty do
        current = frontier.pop()
        if current is not discovered then
            label current as discovered
            if current is target:
                return success
            for all adjacentEdges(edge) from current do
                if edge is not discovered then
                    new_cost = old_cost + current_cost
                    frontier.push(edge, new_cost)
    return failure
```

There is a diffrerence between UCS and BFS. In breadth-first search, the discovery is done when the node is added to the frontier. However in uniform-cost search, the cost and discovery is done when evaluating this path form the frontier.

## Informed Search Algorithms

Given a problem which has a huge amount of states, blind search algorithms consume so much time, that most of the time a solution is never found. Taking this fact into account, the searching time needs to be reduced which means that the different number of states should also be reduced. To achieve that, an indication is needed so that it can describe and evaluate each state that the algorithm is on. Algorithms that utilize this information about states are called heuristic search algorithms.

### Hill Climbing

The hill climbing algorithm shares a lot of similarities with the depth-first search algorithm (DFS). However, there are two key differences:

1. With the Hill Climbing algorithm the next node to go into the frontier is based on the distance value from the target, while DFS chooses one of the neighbor nodes, often being the most left option.

2. With the Hill Climbing algorithm, there is only one node in the frontier. Every time it chooses a new node to search, the other nodes get eliminated, while with DFS they are added to the frontier, to be discovered later.

We can assume the pseudocode for the hill climbing algorithm as following:

```Pseudocode
algorithm hill_climbing(graph, origin, target)
    frontier = origin
    while frontier is not target do
        children = expand(neighbors)
        if children is empty then
            return failure
        bestNeighbor = best(children)
        if hValue(bestNeighbor) < hValue(frontier) then
            frontier = bestNeighbor
    return success
```

Generally, the hill climbing algorithm is used when a solution needs to be found extremely fast, even if this solution is not the best available. This means that HC could choose a node that, at the time, is the best, only to prove later that this whole path is a mediocre or bad choice to take. HC is very efficient both in time and memory, but it is not complete. He can also be stuck in deadlocks, making a solution impossible to find.

### Best First Search

Information to be added.

## Time and space complexities

* *"V"* represents the ammount of vertices
* *"E"* represents all the edges of the graph
* *"H"* represents the maximum height of the tree
* *"b"* represents the branching factor
* *"C"* represents the cost of the optimal solution
* *"e"* represents minimum cost of a step

|        Algorithm        |  Time Complexity  | Space Complexity |
|   :-----------------:   | :---------------: | :--------------: |
|  Breadth-first search   |     O(V + E)      |       O(V)       |
|   Depth-first search    |     O(V + E)      |       O(H)       |
|   Uniform cost search   |    O(b^(C/e))     |    O(b^(C/e))    |
|      Hill Climbing      |       O(∞)        |       O(b)       |

## Implementation

This python implementation uses the popular simplified map of the Romania road system as its data set. However, anyone can create and load a custom graph just by defining a json fine in the appropriate format. Please take a look at the tour_romania.json file. The following picture depicts the graph that is created. Each square is a node, and each of these nodes is connected via an edge to one or more neighbor nodes.

![graph-example](/images/romanianmap.jpg)

If you wish to see another example of the BFS or the DFS algorithms in action, i have also implemented them while traversing a binary search tree. The BFS is used to print the structure of the tree and the DFS to print the nodes in the following orders:

* pre-order
* in-order
* post-order

If you wish to know more you can take a look at this repository:
[Binary search tree](https://github.com/sotostzam/data-structures-and-algorithms)
