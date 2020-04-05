# Tic-Tac-Toe using Minimax and Alpha-Beta prunning

This python implementation is based on the popular game Tic-Tac-Toe. It uses two search algorithms for two-player games, one is called Minimax and the second one Alpha-Beta prunning.

![tic-tac-toe](/images/tictactoe.png)

## Minimax

Given a state of the game, the minimax algorithm returns a decision about its next best move against another player. Internally, it uses two players for this decision, one play for maximazing rewards (max) and one to minimize rewards (min). It creates a tree, and each depth value of this tree is a different player, while the leaf-nodes of the tree are the terminal states. Usually the max players is defined as the root node.

## Alpha-Beta prunning

The Alpha-Beta algorithm is a layer on top of the Minimax algorithm. It utilizes the prunning of sub-trees of the main tree. Its name is given by the two boundaries it has, (alpha and beta) which control the maximum value (alpha) and the lowest value (beta) that can be achieved by the Max and Min players. Max is trying to increase the alpha variable, while Min tries to decrease beta. With larger trees this prunning gives an extreme boost in the completion of the searches of this combination with the Minimax algorithm.
