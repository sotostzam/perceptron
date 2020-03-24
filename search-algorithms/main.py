import graph, bfs, dfs , ucs
import hill_climbing as hc

def print_results(name, result):
    print("----- " + name + " -----")
    if result:
        print("Path: " + ' -> '.join(result[0]))
        print("Cost: " + str(result[1]))
    else:
        print("Target not found!")

if __name__ == "__main__":
    graph = graph.Graph()
    graph.load_data('tour_romania.json')

    # Algorithms return either a tuple of (found_path, total_cost) or False
    print_results("Breadth-first search", bfs.search(graph, "Oradea", "Bucharest"))
    print_results("Depth-first search"  , dfs.search(graph, "Oradea", "Bucharest"))
    print_results("Uniform cost search" , ucs.search(graph, "Oradea", "Bucharest"))
    print_results("Hill Climbing"       ,  hc.search(graph, "Oradea", "Bucharest"))
