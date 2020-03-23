def search(graph, origin, target):
    # Make sure nodes are undiscovered initially
    graph.reset_nodes()
    target_node = graph.get_node_obj(target)
    origin_node = graph.get_node_obj(origin)
    # BFS uses a FIFO queue structure as frontier (First in first out)
    frontier = []
    frontier.append((origin_node, [origin_node.value], 0))
    origin_node.discovered = True
    while frontier:
        current_node, current_path, current_cost = frontier.pop(0)
        if current_node == target_node:
            return current_path, current_cost
        neighbors = graph.get_neighbors(current_node)
        for edge_node, cost in neighbors:
            if edge_node.discovered != True:
                edge_node.discovered = True
                new_path = current_path.copy()
                new_path.append(edge_node.value)
                frontier.append((edge_node, new_path, cost + current_cost))
    # Return false if target is not found
    return False
