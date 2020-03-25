from queue import PriorityQueue

def search(graph, origin, target):
    # Make sure nodes are undiscovered initially
    graph.reset_nodes()
    origin_node = graph.get_node_obj(origin)
    target_node = graph.get_node_obj(target)
    # Best first search evaluates beft node like useing a priority queue (Min Heap)
    frontier = PriorityQueue()
    # Frontier is a tuple of (priority, (node, path_to_node, total_cost))
    frontier.put((graph.get_distance(origin_node), (origin_node, [origin_node.value], 0)))
    while frontier:
        # Pick the best node according to the heuristic value
        _ , state = frontier.get()
        current_node, path, total_cost = state
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
                    frontier.put((graph.get_distance(neighbor_node), (neighbor_node, new_path, new_cost)))
        else:
            return False
    return False
