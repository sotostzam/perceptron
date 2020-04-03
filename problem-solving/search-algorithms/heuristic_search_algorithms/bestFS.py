import heapq, math

def search(graph, app, origin, target, beam = math.inf):
    # Make sure nodes are undiscovered initially
    graph.reset_nodes()
    origin_node = graph.get_node_obj(origin)
    target_node = graph.get_node_obj(target)
    # Best first search evaluates beft node like using a priority queue (Min Heap)
    frontier = []
    # Frontier is a tuple of (priority, (node, path_to_node, total_cost))
    heapq.heappush(frontier, (graph.evaluate(origin_node, target_node), (origin_node, [origin_node], 0)))
    while frontier:
        # Pick the best node according to the heuristic value
        _ , state = heapq.heappop(frontier)
        current_node, current_path, total_cost = state
        current_node.discovered = True
        if current_node is target_node:
            return current_path, total_cost
        neighbors = graph.get_neighbors(current_node)
        if neighbors:
            for neighbor_node, cost in neighbors:
                if neighbor_node.discovered is False:
                    app.update_canvas(current_path, neighbor_node)
                    new_cost = total_cost + cost
                    new_path = current_path.copy()
                    new_path.append(neighbor_node)
                    heapq.heappush(frontier, (graph.evaluate(neighbor_node, target_node), (neighbor_node, new_path, new_cost)))
                    # A beam value of inf is Best First Search, otherwise Beam Search
                    if len(frontier) > beam:
                        frontier = frontier[0: beam]
                        heapq.heapify(frontier)
        else:
            return False
    return False
