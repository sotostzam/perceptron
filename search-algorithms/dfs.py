def search(graph, origin, target):
    # Make sure nodes are undiscovered initially
    graph.reset_nodes()
    target_node = graph.get_node_obj(target)
    # DFS uses a LIFO stack structure as frontier (Last in first out)
    frontier = []
    frontier.append((graph.get_node_obj(origin), [graph.get_node_obj(origin).value], 0))
    while frontier:
        current_node, current_path, current_cost = frontier.pop()
        if current_node.discovered != True:
            current_node.discovered = True
            if current_node == target_node:
                return current_path, current_cost
            neighbors = graph.get_neighbors(current_node)
            neighbors.reverse()
            for edge_node, cost in neighbors:
                new_path = current_path.copy()
                new_path.append(edge_node.value)
                frontier.append((edge_node, new_path, cost + current_cost))
    # Return false if target is not found
    return False
