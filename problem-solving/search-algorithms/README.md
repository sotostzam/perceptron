# Blind and Informed Search Algorithms

This python implementation uses the popular simplified map of the Romania road system as its data set. However, anyone can create and load a custom graph just by defining a json fine in the appropriate format. Please take a look at the tour_romania.json file. The following picture depicts the graph that is created. Each circle is a node, and each of these nodes is connected via an edge to one or more neighbor nodes.

![romania-graph](/images/search_application.png)

It is possible to select and run various algorithms on this graph, allowing the user to select the starting node and the goal node. As far as depth limited search and its variants (DFS, IDS) are concerned, the appication gives you the ability to show the depth value and even edit it for the DLS search.

The informed search algorithms, need a special evaluation function, which will evaluate the step. In this implementation, this evvaluation function if using the euclidean distance between two node's pixel positions.

## Wikipedia Articles

* Uninformed Search Algorithms (or blind search)
  * [Breadth-first search](https://en.wikipedia.org/wiki/Breadth-first_search)
  * [Depth-first search](https://en.wikipedia.org/wiki/Depth-first_search)
  * [Depth limited search](#depth-limited-search)
  * [Iterative deepening search](https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search)
  * [Uniform cost search (Dijikstra)](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
* Informed Search Algorithms
  * [Hill Climbing](https://en.wikipedia.org/wiki/Hill_climbing)
  * [Best First Search](https://en.wikipedia.org/wiki/Best-first_search)
  * [A* (A-star)](https://en.wikipedia.org/wiki/A*_search_algorithm)

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

## Additional Example

If you wish to see another example of the BFS or the DFS algorithms in action, i have also implemented them while traversing a binary search tree. The BFS is used to print the structure of the tree and the DFS to print the nodes in the following orders: pre-order, in-order and post-order.

If you wish to know more you can take a look at this repository:
[Binary search tree](https://github.com/sotostzam/data-structures-and-algorithms)
