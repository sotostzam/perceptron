import math, time
import graph, genetic_algorithm

def main():
    pop_size  = 250        # Population size
    nodes_num = 12         # Number of nodes in graph
    max_iter  = 1000       # Maximum number of iterations

    tsp = graph.Graph(nodes_num)
    population = graph.get_population(tsp.nodes, pop_size)
    best_distance = math.inf
    iteration = 0
    first_guess = None

    while True:
        genetic_algorithm.assign_fitness(population)
        genetic_algorithm.normalize_fitness(population)

        # Get population with lowest distance
        pop_best_distance = math.inf
        current_path = []
        for i in range(len(population)):
            if population[i].distance < pop_best_distance:
                pop_best_distance = population[i].distance

                # Construct current best path
                current_path.clear()
                for node in population[i].nodes:
                    current_path.append(node.x)
                    current_path.append(node.y)

        # Update left canvas (population's best distance)
        tsp.update_current_path(current_path)

        # Update right canvas (global best distance)
        if pop_best_distance < best_distance:
            iteration = 0
            best_distance = pop_best_distance
            if first_guess is None:
                first_guess = best_distance
            # Find percentage increase from first guess
            perc = abs(((best_distance - first_guess) / first_guess) * 100)
            print("Best distance: " + str(round(best_distance, 2)) + "\tImprovement: " + str(round(perc, 1)) + "%")
            # Update right canvas (global best distance)
            tsp.update_best_path(current_path)
        
        tsp.window.update()

        # Advance to next generation
        population = genetic_algorithm.advance_generation(population)
        
        if iteration == max_iter:
            print("Reached maximum number of iterations with no further improvements.")
            break
        else:
            iteration += 1

    tsp.window.mainloop()

if __name__ == "__main__":
    main()
