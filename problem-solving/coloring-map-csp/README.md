# Coloring Australia Map using Backtracking

This python implementation uses the Australia map and creates nodes for each of its states. The problem backtracking solves in this example is the following: We need to color each state, so that no adjacent (neighbor) state has the same color.

![australia-graph](/images/csp.png)

To better understand the constraint satisfaction problem, we should initialize the following:

All Australia states as a set of variables:

* {WA, NT, SA, Q, NSW, V, T }

The state space of each variable (or the possible values for each variable):

* {red, green, blue}

Then we create the constraint graph which contains all the variables (shown as nodes) and all adjacent states (connected and shown as edges). Using the backtracking algorithm we need to find a coloring sheme of all states, with the constrant that no adjacent states have the same color.

If you wish to know more about how the backtracking algorithm works, you can refer to the following wikipedia link: [Backtracking](https://en.wikipedia.org/wiki/Backtracking)
