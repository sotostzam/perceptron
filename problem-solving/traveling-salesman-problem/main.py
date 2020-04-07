import math, time
import graph, genetic_algorithm

def main():
    pop_size  = 250      # Population size
    nodes_num = 12       # Number of nodes in graph

    tsp = graph.Graph(nodes_num)
    population = graph.get_population(tsp.nodes, pop_size)
    best_distance = math.inf

    while True:
        genetic_algorithm.assign_fitness(population)
        genetic_algorithm.normalize_fitness(population)

        # Get population with lowest distance
        pop_best_distance = math.inf
        for i in range(len(population)):
            if population[i].distance < pop_best_distance:
                pop_best_distance = population[i].distance

                # Construct current best path
                current_path = []
                for node in population[i].nodes:
                    current_path.append(node.x)
                    current_path.append(node.y)

        # Update left canvas (population's best distance)
        tsp.canvas_left.delete(tsp.current_path_obj)
        tsp.current_path_obj = tsp.canvas_left.create_line(current_path, width = 2, fill = 'red')
        tsp.canvas_left.tag_lower(tsp.current_path_obj)

        # Update right canvas (global best distance)
        if pop_best_distance < best_distance:
            best_distance = pop_best_distance
            print(best_distance)
            tsp.canvas_right.delete(tsp.best_path_obj)
            tsp.best_path_obj = tsp.canvas_right.create_line(current_path, width = 2, fill = 'green')
            tsp.canvas_right.tag_lower(tsp.best_path_obj)
        
        tsp.window.update()

        # Advance to next generation
        population = genetic_algorithm.advance_generation(population)

    tsp.window.mainloop()

if __name__ == "__main__":
    main()
