from queue import PriorityQueue

def search(graph, origin, target):
    # Make sure nodes are undiscovered initially
    graph.reset_nodes()
    target_node = graph.get_node_obj(target)
    # UCS uses a priority queue. Here priority is the lowest cost
    frontier = PriorityQueue()        
    # Frontier is a tuple of (priority, (node, path_to_node))                    
    frontier.put((0, (graph.get_node_obj(origin), [])))
    while frontier.qsize() > 0:
        current_cost, state = frontier.get()
        current = state[0]
        current_path = state[1]
        if current.discovered != True:
            current.discovered = True
            if current == target_node:
                current_path.append(current.value)
                print("Path: " + str(' -> '.join(current_path)))
                print("Accumulated cost: " + str(current_cost))
                return True

            # Get neighbors of node and add them to frontier
            neighbors = graph.get_neighbors(current)
            for edge_node, cost in neighbors:
                if edge_node.discovered != True:
                    new_cost = current_cost + cost
                    new_path = current_path.copy()
                    new_path.append(current.value)
                    frontier.put((new_cost, (edge_node, new_path)))
    return print("Not found.")
