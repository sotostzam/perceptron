# Search Algorithms

Given a problem with a state space, a search algorithm's purpose is to find the solution. All algorithms that try to find a solution are called search algorithms. These algorithms fall into the following categories:

## Table of contents

* [Uninformed Search Algorithms](#uninformed-search-algorithms)
  * [Breadth-first search](#breadth-first-search)
  * [Depth-first search](#depth-first-search)
  * [Uniform cost search](#uniform-cost-search)
* [Informed Search Algorithms](#informed-search-algorithms)
* [Time and space complexities](#time-and-space-complexities)
* [Implementation](#implementation)

## Uninformed Search Algorithms

These kinds of algorithms are also called blind search algorithms. These algorithms do not take into account the information about the evaluation of each state. So they act in the same way to solve any problem, and they only care about the timing that each state is created. Some of these algorithms are state below:

### Breadth-first search

Breadth-first search (BFS) is a uninformed search algorithm. It examines all possible states on the same level first, and then moves to the next level. BFS uses a FIFO queue structure (First In First Out) for keeping track of its search frontier. On each iteration the algorithm searches all the states being on the lower depth, as these states were inserted first in the queue. If a node that is attached via an edge has already been discovered, the algorithm ignores it and moves on.

Given a set of vertices *"V"* and a set of edges *"E"*, we can assume the following pseudocode:

```Pseudocode
algorithm bfs_search(graph, origin, target)
    frontier <-> Is a queue
    label origin as discovered
    frontier.push(origin)
    while Q is not empty do
        current := frontier.pop()
        if current is target then
            return True
        for all adjacentEdges(edge) from current do
            if edge is not discovered then
                label edge as discovered
                edge.parent := current
                frontier.enqueue(edge)
    return False
```

The biggest advantage of the BFS algorithm is that it finds the smallest possible route, meaning the route with the least amount of edges. This solution can only be described as best if all edges have the same cost. Moreover, the bfs algorithm is considered as "complete", as i will always find a solution if there is one. One disadvantage is that the search frontier of the bfs algorithm is increasing a lot in size, which means that it needs a lot more memory space.

### Depth-first search

Like the name of this algorithm suggests, depth-first search (DFS) is an uninformed search algorithm which examines all possible states that exist in the deeper layers of the tree. If there is more than one state at the same depth, it randomly chooses the next or picks the one on the left for ease.

The search frontier this algorithm uses, is a LIFO stack structure (Last In First Out). This means that on each iteration, every new state gets added to the top of the stack, and the search procedure continues with one of them. If a node that is attached via an edge has already been discovered, the algorithm ignores it and moves on.

Given a set of vertices *"V"* and a set of edges *"E"*, we can assume the following pseudocode:

```Code
algorithm dfs_search(graph, origin, target)
    frontier <- Is a stack
    frontier.push(origin)
    while frontier is not empty do
        current = frontier.pop()
        if current is not discovered then
            label current as discovered
            if current is target:
                return True
            for all adjacentEdges(edge) from current do
                frontier.push(edge)
    return False
```

The DFS algorithm has the advantage of not consuming too many resources when it comes to space. The search frontier does not increase by that much on each iteration, so its memory for upcoming search states is relatively small. However, this algorithm does not guarantee that the first solution found, is also the best. What is more, it can be stuck in a loop if there are branches of a tree with infinite length.

### Uniform Cost search

Unlike the BFS, uniform-cost search doesn’t care about the number of steps that each of the paths it searches has, but the total path cost. Therefor, it uses a priority queue. This means that the path that is selected from the frontier is the one with the lowest cost value so far.

Given a set of vertices *"V"* and a set of edges *"E"*, we can assume the following pseudocode:

```Code
algorithm ucs_search(graph, origin, target)
    frontier <- Is a priority queue
    frontier.push(origin, 0)
    while frontier is not empty do
        current = frontier.pop()
        if current is not discovered then
            label current as discovered
            if current is target:
                return True
            for all adjacentEdges(edge) from current do
                if edge is not discovered then
                    new_cost = old_cost + current_cost
                    frontier.push(edge, new_cost)
    return False
```

There is a diffrerence between UCS and BFS. In breadth-first search, the discovery is done when the node is added to the frontier. However in uniform-cost search, the cost and discovery is done when evaluating this path form the frontier.

## Informed Search Algorithms

Given a problem which has a huge amount of states, blind search algorithms consume so much time, that most of the time a solution is never found. Taking this fact into account, the searching time needs to be reduced which means that the different number of states should also be reduced. To achieve that, an indication is needed so that it can describe and evaluate each state that the algorithm is on. Algorithms that utilize this information about states are called heuristic search algorithms.

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

## Implementation

This python implementation uses the popular simplified map of the Romania road system as its data set. However, anyone can create and load a custom graph just by defining a json fine in the appropriate format. Please take a look at the tour_romania.json file. The following picture depicts the graph that is created. Each square is a node, and each of these nodes is connected via an edge to one or more neighbor nodes.

![graph-example](/images/romanianmap.jpg)

If you wish to see another example of the BFS or the DFS algorithms in action, i have also implemented them while traversing a binary search tree. The BFS is used to print the structure of the tree and the DFS to print the nodes in the following orders:

* pre-order
* in-order
* post-order

If you wish to know more you can take a look at this repository:
[Binary search tree](https://github.com/sotostzam/data-structures-and-algorithms)
