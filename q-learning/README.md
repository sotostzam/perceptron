# Q-Learning

Q-learning is a model-free reinforcement learning algorithm. It uses software agents that learn to make action based on the state they are and the reward they take. Q-Learnig is model-free, meaning that it does not need a model for the environment, and makes use of the Markov decision processes (MDP).

## How it works

Reinforcement learning, and Q-Learning more specifically needs the following to operate:

* A virtual agent
* A set of states
* A set of actions per state
* A set of rewards

Moreover, a learning rate has to be set, which determing the rate the algorithm is learning throughout the episodes, as well as a discount factor, which determines the importance of future rewards. A lower value of discount means that the agent will only value current rewards. The exact formula of the algorithm is shown below:

![qlearning](/images/qlearning.png)

## Implementation

Upon running this project, you are welcomed by a graphical user interface, with a menu on the right that is showing the episode number, the current amount of tries done on each episode, the total reward the agent got and the best reward. Below these labels, are three buttons for starting the application, resetting and exiting.

![qlearning_gui](/images/qlearning_gui.png)

Starting the simulation, the software agent starts to take actions and receive rewards for these actions. The rewards are given by the following table:

* When the agent (*red*) moves one tile it gets a reward of **-1**
* When it tries to move on a wall (*black*) it gets a score of **-10**
* Upon reaching the goal position (*green*), it gets a score of **100**

There are by default 1000 episodes to run, and each episode the agent has 200 tries to move around. After reaching either the maximum amount of tries or the goal position, the environment gets reset and a new episode starts. Last but not least, the user can modify the environment by clicking on the grid (Left mouse button to place a wall, right button to remove it).
