def search(graph, origin, target):
    # Make sure nodes are undiscovered initially
    graph.reset_nodes()
    target_node = graph.get_node_obj(target)
    origin_node = graph.get_node_obj(origin)
    queue = []
    queue.append(origin_node)
    origin_node.discovered = True
    iter = 0
    while queue:
        path = ""
        current = queue.pop(0)
        if current == target_node:
            print(current.value)
            print("Path: " + path)
            return True
        neighbors = graph.get_neighbors(current)
        for edge in neighbors:
            if edge[0].discovered != True:
                edge[0].discovered = True
                path += edge[0].value + ", "
                queue.append(edge[0])
        print(str(iter) + ": " + path)
        iter += 1
    return print("Not found!")
