# Q-Learning

Q-learning is a model-free reinforcement learning algorithm. It uses software agents that learn to make action based on the state they are and the reward they take. Q-Learnig is model-free, meaning that it does not need a model for the environment, and makes use of the Markov decision processes (MDP).

## How it works

Q-Learning uses the following formula to transform the Q-Table's values:

![qlearning](/images/qlearning.png)

To be more specific, the q-learning algorithm utilizes the following:

* ***A virtual agent***, capable of moving around and exchanging information with the environment (maze).
* ***A set of states***, which represent all the possible states that the agent can be on each timestep.
* ***A set of actions*** per state. These must be known to the agent, in order for it to know what are all the available the possibilities.
* ***A set of rewards***. This means that the agent gets a reward upon moving to a new state.
* ***A learning rate***, which determines the rate the algorithm is learning throughout the episodes
* ***A discount factor***, which determines the importance of future rewards. A lower value of discount means that the agent will only value current rewards.

This project also includes a policy called ***epsilon greedy strategy***. This strategy makes use of a variable epsilon, ranging from 0 to 1, that indicates the percentage of exploration the agent wants to do. For instance, on the first episode we need the agent to do a lot of exploration so an epsilon value of 1 means 100% exploration. When episodes go on and the agent has explored the environment, this epsilon reduces itself, and this reduction means that the agent is getting more *greedy* for the best reward. This procedure is used in order to minimize the possibility of finding a path to the goal that is not optimal

## Implementation

This implementation supports a graphical user interface. On the top left there are options to change the position of the goal and the agent. Below these options there is the main menu, which contains a set of buttons which can do the following actions:

* Start the simulation process (Running 250 episodes)
* Reset the maze to its initial state
* Save or load the maze's layout to/from a csv file
* Exit the application

On the right hand side, there is a column of labels that are showing some parameters and statistics of the current state. These parameters include:

* Episode number
* Current amount of tries left for each episode
* Total reward for each episode
* Best accumulated score
* Success rate of all the episodes
* Exploration rate (1 - 100%)

Last but not least, in the middle of these two columns, there is the maze layout. The user can modify this environment by clicking on the grid (Left mouse button to place a wall, right button to remove it).

![qlearning_gui](/images/qlearning_gui.png)

Starting the simulation, the software agent starts to take actions and receive rewards for these actions. The rewards are given by the following table:

* **-1**, when the agent (*red circle*) moves one tile
* **-10**, when it tries to move on a wall (*black square*)
* **100**, upon reaching the goal position (*green square*)

There are by default 250 episodes to run, and each episode the agent has 200 tries to move around. After reaching either the maximum amount of tries or the goal position, the environment gets reset and a new episode starts.
