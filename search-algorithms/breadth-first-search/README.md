# Breadth-first search

Breadth-first search (BFS) is a uninformed search algorithm. It examines all possible states on the same level first, and then moves to the next level.

![graph-example](/images/graph.png)

This python implementation uses the example above to find a route between node **"A"** and node **"J"**. Using the breadth-first search algorithm on this graph yields the following path:

A -> B -> D -> F -> H -> I -> J

## How it works

This algorithm uses a queue for keeping trach of its search frontier. On each iteration it checks if the target node is the one that is currently first on the queue, and if it is, the algorithms ends successfully finding the route. Otherwise, it gets all the edges attached to the current node that is searching, and inserts all the nodes attached to the queue, labeling them as discovered. If a node that is attached via an edge has already been discovered, the algorithm ignores it and moves on.

Particularly, the pseudocode according to Wikipedia is the following:

```Pseudocode
procedure BFS(G, start_v) is
    let Q be a queue
    label start_v as discovered
    Q.enqueue(start_v)
    while Q is not empty do
        v := Q.dequeue()
        if v is the goal then
            return v
        for all edges from v to w in G.adjacentEdges(v) do
            if w is not labeled as discovered then
                label w as discovered
                w.parent := v
                Q.enqueue(w)
```

Additional example: I have also implemented the BFS algorithm to print the structure of a binary tree. If you wish to know more you can take a look at this repository: [Binary search tree](https://github.com/sotostzam/data-structures-and-algorithms)
