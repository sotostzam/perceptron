import graph, bfs, dfs , ucs

if __name__ == "__main__":
    graph = graph.Graph()
    graph.load_data('tour_romania.json')

    # Algorithms return either a tuple of (found_path, total_cost) or False
    bfs_result = bfs.search(graph, "Arad", "Bucharest")
    dfs_result = dfs.search(graph, "Arad", "Bucharest")
    ucs_result = ucs.search(graph, "Arad", "Bucharest")

    print("Breadth-first search")
    if bfs_result:
        print("Path: " + ' -> '.join(bfs_result[0]))
        print("Cost: " + str(bfs_result[1]) + "\n")
    else:
        print("Target not found!")

    print("Depth-first search")
    if dfs_result:
        print("Path: " + ' -> '.join(dfs_result[0]))
        print("Cost: " + str(dfs_result[1]) + "\n")
    else:
        print("Target not found!")

    print("Uniform cost search")
    if ucs_result:
        print("Path: " + ' -> '.join(ucs_result[0]))
        print("Cost: " + str(ucs_result[1]))
    else:
        print("Target not found!")
    
