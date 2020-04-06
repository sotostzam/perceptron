# N-Queens Problem using Backtracking and MRV

This python implementation creates N x N checkerboard and N queens. The constraint satisfaction problem is described as the following. Place all N queens on the board, so that no queen can attack any other.

![maze_map](/images/n-queens.png)

We can assume that a single queen can be placed on a single column of the board. Now the constraints we need to check for are the following:

1. No other queen is placed on the same row
2. No other queen is placed on the diagonals

## Backtracking

Backtracking is an algorithm utilizing Depth-first search. It recursively calls itself until a solution is found or a terminal state. A terminal state can either be a state where some queens can not be placed, so it backtracks to a previous state, or a terminal state, a state where no solution can exist, for example trying to solve this problem with 3 queens.

## Minimim Remaining Values (MRV)

The MRV algorithm is used at the same time as the backtracking algorithm. Instead of picking possibles moves for a queen, thus checking every possible move meaning all possible rows, it looks ahead and edits the movement domain of each queen, removing any values that are not possible.
