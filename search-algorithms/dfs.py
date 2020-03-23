def search(graph, origin, target):
    # Make sure nodes are undiscovered initially
    graph.reset_nodes()
    target_node = graph.get_node_obj(target)
    # DFS uses a LIFO stack structure (Last in first out)
    frontier = []
    frontier.append(graph.get_node_obj(origin))
    found = False
    path = ""
    while frontier:
        current = frontier.pop()
        if current.discovered != True:
            current.discovered = True
            path += current.value + " -> "
            if current == target_node:
                found = True
                break
            neighbors = graph.get_neighbors(current)
            # Iterate all the children backwards to fill stack correctly
            for i in range(len(neighbors)-1, -1, -1):
                frontier.append(neighbors[i][0])
    print("Path: " + path[0: -4])
    if found:
        print("Target found!")
    else:
        print("Target not found!")
