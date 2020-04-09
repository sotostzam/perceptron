# Traveling Salesman Problem

This python implementation is creating some random nodes on a canvas. On the right canvas area, it displays the current best distance between all of them, and on the right the best ever distance found.

![tsp](/images/tsp.png)

## Genetic Algorithms

A genetic algorithm is a metaheuristic algorithm which simulates the process of natural selection. It is part of a class called evolutionary algorithms which are used for optimization and search problems. Typically a genetic algorithm cointains the following traits:

* Initializes a population, commonly hundreds or even thousands of random solutions for a problem
* Contains a fitness function, to evaluate each population
* Selection function, able to select some of the best possible solutions
* Crossover function, to combine the solution from the selection function, and produce one or more offsprings
* Mutation function, able to alter values of the offprings to create more variation

Usually, to terminate a genetic algorithm, a number of total iteration is initialized, so that when this number is met while no further change on the last "best" solution, the algorithm is terminated. If a new "best" solution is found, then reset this number to zero.