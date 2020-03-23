# Search Algorithms

Given a problem with a state space, a search algorithm's purpose is to find the solution. All algorithms that try to find a solution are called search algorithms. These algorithms fall into the following categories:

---

## Uninformed Search Algorithms

These kinds of algorithms are also called blind search algorithms. These algorithms do not take into account the information about the evaluation of each state. So they act in the same way to solve any problem, and they only care about the timing that each state is created. Some of these algorithms are state below:

* [Breadth-first search](https://github.com/sotostzam/artificial-intelligence/tree/master/search-algorithms/breadth-first-search)
* [Depth-first search](https://github.com/sotostzam/data-structures-and-algorithms)

### Uniform Cost search

#### Time and space complexity

* *"b"* represents the branching factor
* *"C"* represents the cost of the optimal solution
* *"e"* represents minimum cost of a step

|  Time Complexity  | Space Complexity |
| :---------------: | :--------------: |
|    O(b^(C/e))     |    O(b^(C/e))    |

#### Implementation

![graph-example](/images/graph_weighted.png)

---

## Informed Search Algorithms

Given a probelm which has a huge amount of states, blind search algorithms consume so much time, that most of the time a solution is never found. Taking this fact into account, the searching time needs to be reduced which means that the different number of states should also be reduced. To achieve that, an indication is needed so that it can describe and evaluate each state that the algorithm is on. Algorithms that utilize this information about states are called heuristic search algorithms.
