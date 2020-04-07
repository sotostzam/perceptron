import math, time, random
import graph, genetic_algorithm

def main():
    pop_size = 10
    nodes_num = 7

    tsp = graph.Graph(nodes_num)
    pop_list = graph.get_population(tsp.nodes, pop_size)
    genetic_algorithm.normalize_fitness(pop_list)
    
    best_path_obj = None
    current_path_obj = None
    best_distance = math.inf

    while True:
        pop_best_distance = math.inf

        # Get population's best fitness (lowest distance)
        for i in range(len(pop_list)):
            if pop_list[i].fitness < math.inf:
                pop_best_distance = pop_list[i].fitness
                current_path = []
                for node in pop_list[i].nodes:
                    current_path.append(node.x)
                    current_path.append(node.y)

        if pop_best_distance < best_distance:
            best_distance = pop_best_distance
            tsp.canvas_right.delete(best_path_obj)
            best_path_obj = tsp.canvas_right.create_line(current_path, width = 2, fill = 'green')

        tsp.canvas_left.delete(current_path_obj)
        current_path_obj = tsp.canvas_left.create_line(current_path, width = 2, fill = 'red')
        tsp.canvas_left.tag_lower(current_path_obj)
        tsp.canvas_right.tag_lower(best_path_obj)
        tsp.canvas_left.update()
        tsp.canvas_right.update()

    tsp.window.mainloop()

if __name__ == "__main__":
    main()
