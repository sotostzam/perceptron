import heapq, time

def search(graph, app, origin, target):
    # Make sure nodes are undiscovered initially
    graph.reset_nodes()
    target_node = graph.get_node_obj(target)
    # UCS uses a priority queue as frontier. Here priority is determined by the cost
    frontier = []      
    # Frontier is a tuple of (priority, (node, path_to_node))
    heapq.heappush(frontier, (0, (graph.get_node_obj(origin), [])))
    while frontier:
        current_cost, state = heapq.heappop(frontier)
        current_node = state[0]
        current_path = state[1]
        if current_node.discovered != True:
            current_node.discovered = True
            app.update_canvas(current_path, current_node)
            if current_node == target_node:
                current_path.append(current_node)
                return current_path, current_cost
            # Get neighbors of node and add them to frontier
            neighbors = graph.get_neighbors(current_node)
            for edge_node, cost in neighbors:
                if edge_node.discovered != True:
                    new_cost = current_cost + cost
                    new_path = current_path.copy()
                    new_path.append(current_node)
                    heapq.heappush(frontier, (new_cost, (edge_node, new_path)))
    # Return false if target is not found
    return False
