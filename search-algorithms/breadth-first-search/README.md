# Breadth-first search

Breadth-first search (BFS) is a uninformed search algorithm. It examines all possible states on the same level first, and then moves to the next level.

## How it works

This algorithm uses a FIFO queue structure (First In First Out) for keeping track of its search frontier. On each iteration the algorithm searches all the states being on the lower depth, as these states were inserted first in the queue. If a node that is attached via an edge has already been discovered, the algorithm ignores it and moves on.

Given a set of vertices *"V"* and a set of edges *"E"*, we can assume the following pseudocode:

```Pseudocode
algorithm bfs_search(start, stop)
    frontier <-> Is a queue
    label start as discovered
    frontier.push(start)
    while Q is not empty do
        current := frontier.pop()
        if current is stop then
            return True
        for all adjacentEdges(edge) from current do
            if edge is not discovered then
                label edge as discovered
                edge.parent := current
                frontier.enqueue(edge)
    return False
```

The biggest advantage of the BFS algorithm is that it finds the smallest possible route, meaning the route with the least amount of edges. This solution can only be described as best if all edges have the same cost. Moreover, the bfs algorithm is considered as "complete", as i will always find a solution if there is one. One disadvantage is that the search frontier of the bfs algorithm is increasing a lot in size, which means that it needs a lot more memory space.

## Time and space complexity

* *"V"* represents the ammount of vertices
* *"E"* represents all the edges of the graph

|  Time Complexity  | Space Complexity |
| :---------------: | :--------------: |
|     O(V + E)      |       O(V)       |

## Implementation

![graph-example](/images/graph.png)

This python implementation uses the example above to find a route between node **"A"** and node **"J"**. Using the breadth-first search algorithm on this graph yields the following path:

A -> B -> D -> F -> H -> I -> J

Additional example: I have also implemented the BFS algorithm to print the structure of a binary tree. If you wish to know more you can take a look at this repository:

[Binary search tree](https://github.com/sotostzam/data-structures-and-algorithms)
