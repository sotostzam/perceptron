def search(graph, origin, target):
    # Make sure nodes are undiscovered initially
    graph.reset_nodes()
    origin_node = graph.get_node_obj(origin)
    target_node = graph.get_node_obj(target)
    # Hill climbing uses the node with the lowest distance to goal
    frontier = [(origin_node, [origin_node.value], 0)]
    while frontier:
        # Pick the best node according to the heuristic value
        best_node = min(frontier, key = lambda t: graph.get_distance(t[0]))
        for i in range(0, len(frontier)):
            if frontier[i] is best_node:
                del frontier[i]
                break
        current_node, path, total_cost = best_node
        current_node.discovered = True
        if current_node is target_node:
            return path, total_cost
        neighbors = graph.get_neighbors(current_node)
        if neighbors:
            for neighbor_node, cost in neighbors:
                if neighbor_node.discovered is False:
                    new_cost = total_cost + cost
                    new_path = path.copy()
                    new_path.append(neighbor_node.value)
                    frontier.append((neighbor_node, new_path, new_cost))
        else:
            return False
    return False
