# Depth-first search

Like the name of this algorithm suggests, depth-first search (DFS) is an uninformed search algorithm which examines all possible states that exist in the deeper layers of the tree. If there is more than one state at the same depth, it randomly chooses the next or picks the one on the left for ease.

## How it works

The search frontier this algorithm uses, is a LIFO stack structure (Last In First Out). This means that on each iteration, every new state gets added to the top of the stack, and the search procedure continues with one of them. If a node that is attached via an edge has already been discovered, the algorithm ignores it and moves on.

Given a set of vertices *"V"* and a set of edges *"E"*, we can assume the following pseudocode:

```Code
algorithm dfs_search(start, stop)
    frontier <- Is a stack
    frontier.push(start)
    while frontier is not empty do
        current = frontier.pop()
        if current is not discovered then
            label current as discovered
            if current is stop:
                return True
            for all adjacentEdges(edge) from current do
                frontier.push(edge)
    return False
```

The DFS algorithm has the advantage of not consuming too many resources when it comes to space. The search frontier does not increase by that much on each iteration, so its memory for upcoming search states is relatively small. However, this algorithm does not guarantee that the first solution found, is also the best. What is more, it can be stuck in a loop if there are branches of a tree with infinite length.

## Time and space complexity

* *"V"* represents the ammount of vertices
* *"E"* represents all the edges of the graph
* *"H"* represents the maximum height of the tree

|  Time Complexity  | Space Complexity |
| :---------------: | :--------------: |
|     O(V + E)      |       O(H)       |

## Implementation

![graph-example](/images/graph.png)

This python implementation uses the example above to find a route between node **"A"** and node **"J"**. Using the depth-first search algorithm on this graph yields the following path:

A -> B -> D -> C -> E -> G -> F -> H -> I -> J

Additional example: I have also implemented the DFS algorithm to tranverse a binary search tree in the following orders: pre-orde, in-order and post-order. If you wish to know more you can take a look at this repository:

[Binary search tree](https://github.com/sotostzam/data-structures-and-algorithms)
