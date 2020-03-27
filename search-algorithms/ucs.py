from queue import PriorityQueue
import time

def search(graph, app, origin, target):
    # Make sure nodes are undiscovered initially
    graph.reset_nodes()
    target_node = graph.get_node_obj(target)
    # UCS uses a priority queue as frontier. Here priority is determined by the cost
    frontier = PriorityQueue()        
    # Frontier is a tuple of (priority, (node, path_to_node))                    
    frontier.put((0, (graph.get_node_obj(origin), [])))
    while frontier.qsize() > 0:
        current_cost, state = frontier.get()
        current_node = state[0]
        current_path = state[1]
        app.update_canvas(current_path, .5)
        if current_node.discovered != True:
            current_node.discovered = True
            if current_node == target_node:
                current_path.append(current_node)
                app.update_canvas(current_path, .5)
                return current_path, current_cost

            # Get neighbors of node and add them to frontier
            neighbors = graph.get_neighbors(current_node)
            for edge_node, cost in neighbors:
                if edge_node.discovered != True:
                    new_cost = current_cost + cost
                    new_path = current_path.copy()
                    new_path.append(current_node)
                    frontier.put((new_cost, (edge_node, new_path)))
    # Return false if target is not found
    return False
