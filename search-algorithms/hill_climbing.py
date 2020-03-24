def search(graph, origin, target):
    # Make sure nodes are undiscovered initially
    graph.reset_nodes()
    origin_node = graph.get_node_obj(origin)
    target_node = graph.get_node_obj(target)
    # Hill climbing uses the node with the lowest distance to goal
    frontier = (origin_node, graph.get_distance(origin_node), [origin_node.value], 0)
    while frontier[0] != target_node:
        current_node, current_distance, path, total_cost = frontier
        neighbors = graph.get_neighbors(current_node)
        flag = False
        new_node = None
        if neighbors:
            new_cost = 0
            for neighbor_node, cost in neighbors:
                neighbor_dist = graph.get_distance(neighbor_node)
                if neighbor_dist < current_distance:
                    new_node = neighbor_node
                    current_distance = neighbor_dist
                    new_cost = cost
                    flag = True
        else:
            return False
        if flag:
            total_cost += new_cost
            path.append(new_node.value)
            frontier = (new_node, current_distance, path, total_cost)
        else:
            return False
    return frontier[2], frontier[3]
