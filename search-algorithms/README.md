# Search Algorithms

Given a problem and a description of its state space, we want to find a solution. To achieve that, we have to apply a sequence of strictly predetermined steps, also known as algorithms. All algorithms that fall into that category, meaning they try to find a solution to a problem, are called search algorithms.

## Table of contents

* [Uninformed Search Algorithms](#uninformed-search-algorithms)
  * [Breadth-first search](#breadth-first-search)
  * [Depth-first search](#depth-first-search)
  * [Depth limited search](#depth-limited-search)
  * [Iterative deepening search](#iterative-deepening-search)
  * [Uniform cost search](#uniform-cost-search)
* [Informed Search Algorithms](#informed-search-algorithms)
  * [Hill Climbing](#hill-climbing)
  * [Best First Search](#best-first-search)
  * [A* Algorithm](#A*-(A-Star))
* [Time and space complexities](#time-and-space-complexities)
* [Implementation](#implementation)

## Uninformed Search Algorithms

Algorithms that are labeled as **uninformed search algorithms** (also refered to as **blind search algorithms**), are used for problems that do not allow the evaluation the space state. So, these algorithms treat any problem in the same way, and they only care about the timing that each state is created. Some of these algorithms are stated below:

### Breadth-first search

**Breadth-first search** (BFS) firstly examines the root-node from there all the ascendants of this node, and so on so forth. In other words, the algorithm examines all possible states on the same level first, and then moves on to the next level. The BFS uses a FIFO queue structure (First In First Out) for keeping track of its search frontier. On each iteration the algorithm searches all the states being on a lower depth, as these states were inserted first in the queue. If a node that is attached via an edge has already been discovered, the algorithm ignores it and moves on.

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

The biggest advantage of the BFS algorithm is that it finds the smallest possible route, meaning the route with the least amount of steps. This solution can only be described as best if all edges have the same cost. Moreover, the bfs algorithm is considered as "complete", as i will always find a solution if there is one. One disadvantage is that the search frontier of the bfs algorithm is increasing a lot in size, which means that it needs a lot more memory space.

### Depth-first search

Like the name of this algorithm suggests, **depth-first search** (DFS) examines all possible states that exist at the deepest layer of the tree. If there is more than one state at the same depth, the choice is being done randomly or it is also common to choose the one being on the left.

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
            if current is target then
                return success
            for all adjacentEdges(edge) from current do
                frontier.push(edge)
    return failure
```

The DFS algorithm has the advantage of not consuming too many resources when it comes to space. The search frontier does not increase by that much on each iteration, so its memory for upcoming search states is relatively small. However, this algorithm does not guarantee that the first solution found, is also the best. What is more, it can be stuck in a loop if there are branches of a tree with infinite length.

### Depth limited search

Using a depth-first search can result in an extremely long or even infinite path, while taking another path could result in a solution pretty close to the origin node. This tactic can be eliminated by introducing a depth value to the algorithm, so when searching for a node's neighbors beyond a depth value, it does not add this path to the frontier. This approach is called **depth limited search**.

We can assume the pseudocode for the depth limited search algorithm as following:

```Pseudocode
algorithm dfs_search(graph, origin, target, depth)
    frontier <- Is a stack
    frontier.push(origin)
    while frontier is not empty do
        current = frontier.pop()
        if current is not discovered then
            label current as discovered
            if current is target then
                return success
            if depth > current_depth then
                for all adjacentEdges(edge) from current do
                    frontier.push(edge)
    return failure
```

### Iterative Deepening search

The algorithm utilizing an **iterative deepening search** (ID) combines the pros of both BFS and DFS. ID is on its core a depth limited search, but iterative and starting from zero. This means that whenever the result of an iteration is negative, it advances to a new depth until a solution is found or it checked all possible paths.

We can assume the pseudocode for the iterative deepening search algorithm as following:

```Pseudocode
algorithm ids(graph, origin, target)
    depth = 0
    while solution is not found do
        solution = depth_limited_search(graph, origin, target);
```

### Uniform Cost search

Unlike the BFS algorithm, **uniform-cost search** (UCS) doesn’t care about the total number of steps of a path, but the total path's steps cost. Therefore, it uses a priority queue which means that the path that is selected from the frontier is the one with the lowest cost value so far. In other words, the priority which determines the next node to be examined, is attached to the added cost of this step.

We can assume the pseudocode for the uniform cost search algorithm as following:

```Pseudocode
algorithm ucs_search(graph, origin, target)
    frontier <- Is a priority queue
    frontier.push(origin, 0)
    while frontier is not empty do
        current = frontier.pop()
        if current is not discovered then
            label current as discovered
            if current is target then
                return success
            for all adjacentEdges(edge) from current do
                if edge is not discovered then
                    new_cost = old_cost + current_cost
                    frontier.push(edge, new_cost)
    return failure
```

There is a difference between UCS and BFS. In *breadth-first search*, the discovery is done when the node is added to the frontier, while in *uniform cost search* the discovery is done uppon choosing the path from the frontier.

## Informed Search Algorithms

Given a problem that has a huge amount of states, blind search algorithms tend to be extremelly time-consuming, which almost always means that a solution can not be found. Taking this fact into account, the searching time needs to be reduced and as a result the different number of states should also be reduced. To achieve that, we indroduce an evaluation function which describes and evaluates each state. Algorithms that utilize this kind of information about states are called heuristic search algorithms.

### Hill Climbing

The **hill climbing** algorithm shares a lot of similarities with the depth-first search algorithm (DFS). However, there are two key differences:

* The next node to be inserted into the frontier is based on the distance value from the target, while in DFS one of the neighbor nodes is chosen, often being the left most option.
* There is only one node present in the frontier, so every time a new node is chosen to be searched, the other nodes get eliminated. On the contrary, using DFS all the nodes are added to the frontier, to be discovered later.

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

Unlike the hill climbing algorithm, **best first search** keeps all state-nodes in its frontier. Doing this means that the algorithm can return back to another state if it is following a worse path.

We can assume the pseudocode for the best first search algorithm as following:

```Pseudocode
algorithm bestFS(graph, origin, target)
    frontier <- Is a priority queue
    frontier.push(origin, hValue(origin))
    current = frontier.get()
    while current is not target do
        children = expand(neighbors)
        bestNeighbor = best(children)
        if hValue(bestNeighbor) < hValue(frontier) then
            frontier = bestNeighbor
        if frontier is empty then
            return failure
        current = frontier.get()
    return success
```

Best first search, stops if it finds a solution. This is a common practice for heuristic algorthms. However they can be modified to return multiple solutions. Using this modification though, eliminates the advantage bestFS has, which is a good solution in a relatively short ammount of time.

### A* (A-star)

BestFS algorithm makes use of an evaluation function that returns the distance from the original node to the foal node. With **A\* (A-star)** algorithm, this function's value is then added to the distance that there is already been explored up to the current state. In other words for some state S there are two evaluation functions:

* g(S) which returns the distance from the origin state up to the current state
* h(S) which returns the straight distance from the origin to the target

Of course, this evaluation function can be an underestimation or an overestimation of the real value. Moreover, if the value from h(S) is less or equal with the real value, then A* is guaranteed to find the best solution.

We can assume the pseudocode for the A-star algorithm as following:

```Pseudocode
algorithm a_star(graph, origin, target)
    frontier <- Is a priority queue
    frontier.push(origin, hValue(origin))
    while frontier is empty do
        current = frontier.get()
        neighbors = expand(current)
        if current is target then
            return success
        for each neighbor of current
            accumulated_cost = hValue(current) + cost(current)
            frontier.put(neighbor, accumulated_cost)
    return failure
```

## Time and space complexities

* *"b"* represents the branching factor
* *"d"* represents the depth of the goal node
* *"C"* represents the cost of the optimal solution
* *"e"* represents minimum cost of a step
* *"l"* represents the depth limit
* *[x]* represent notes explained below the following table

| Algorithm                  | Time Complexity | Space Complexity | Complete  | Optimal  |
| :------------------------- | :-------------- | :--------------  | :-------- | :------- |
| Breadth-first Search       | O(b^(d+1))      | O(b^(d+1))       | Yes [a]   | Yes [c]  |
| Depth-first Search         | O(b^d)          | O(b*d)           | No        | No       |
| Depth Limited Search       | O(b^l)          | O(b*l)           | No        | No       |
| Iterative Deepening Search | O(b^d)          | O(b*d)           | Yes [a]   | Yes [c]  |
| Uniform cost Search        | O(b^(C/e))      | O(b^(C/e))       | Yes [a,b] | Yes      |
| Hill Climbing              | O(d)            | O(b)             | No        | No       |
| Best First Search          | O(b^(d+1))      | O(b^d)           | No        | No       |
| A* (A-star)                | O(b^d)          | O(b^d)           | Yes       | Yes      |

* [a]: Complete if b is finite
* [b]: Complete if cost of steps > e, for e > 0
* [c]: Optimal if all steps have the same cost

## Implementation

This python implementation uses the popular simplified map of the Romania road system as its data set. However, anyone can create and load a custom graph just by defining a json fine in the appropriate format. Please take a look at the tour_romania.json file. The following picture depicts the graph that is created. Each square is a node, and each of these nodes is connected via an edge to one or more neighbor nodes.

![graph-example](/images/romanianmap.jpg)

Moreover, the dataset is orgnized in such a way that it included each city's distance from Bucharest in a straight line. This value is used by algorithms that are labeled as informed search algorithms.

If you wish to see another example of the BFS or the DFS algorithms in action, i have also implemented them while traversing a binary search tree. The BFS is used to print the structure of the tree and the DFS to print the nodes in the following orders: pre-order, in-order and post-order.

If you wish to know more you can take a look at this repository:
[Binary search tree](https://github.com/sotostzam/data-structures-and-algorithms)
