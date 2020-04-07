import math, time
import graph, genetic_algorithm

def main():
    pop_size = 10
    nodes_num = 7

    tsp = graph.Graph(nodes_num)
    pop_list = graph.get_population(tsp.nodes, pop_size)

    best_distance = math.inf

    while True:
        genetic_algorithm.assign_fitness(pop_list)
        genetic_algorithm.normalize_fitness(pop_list)
        new_pop = genetic_algorithm.nextGen(pop_list)
        pop_list = new_pop

        # Get population with lowest distance
        pop_best_distance = math.inf
        for i in range(len(pop_list)):
            if pop_list[i].distance < pop_best_distance:
                pop_best_distance = pop_list[i].distance

                # Construct current best path
                current_path = []
                for node in pop_list[i].nodes:
                    current_path.append(node.x)
                    current_path.append(node.y)

        if pop_best_distance < best_distance:
            best_distance = pop_best_distance
            print(best_distance)
            tsp.canvas_right.delete(tsp.best_path_obj)
            tsp.best_path_obj = tsp.canvas_right.create_line(current_path, width = 2, fill = 'green')

        tsp.canvas_left.delete(tsp.current_path_obj)
        tsp.current_path_obj = tsp.canvas_left.create_line(current_path, width = 2, fill = 'red')
        tsp.canvas_left.tag_lower(tsp.current_path_obj)

        tsp.canvas_right.tag_lower(tsp.best_path_obj)
        tsp.canvas_left.update()
        tsp.canvas_right.update()

        #time.sleep(0.1)

    tsp.window.mainloop()

if __name__ == "__main__":
    main()
