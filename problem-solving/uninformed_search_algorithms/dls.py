import math

def search(graph, app, origin, target, depth = math.inf):
    # Update current depth in gui
    app.update_depth(depth)
    # Make sure nodes are undiscovered initially
    graph.reset_nodes()
    target_node = graph.get_node_obj(target)
    # DFS uses a LIFO stack structure as frontier (Last in first out)
    frontier = [(graph.get_node_obj(origin), [graph.get_node_obj(origin)], 0)]
    while frontier:
        current_node, current_path, current_cost = frontier.pop()
        app.update_canvas(current_path, .5)
        if current_node.discovered != True:
            current_node.discovered = True
            if current_node == target_node:
                return current_path, current_cost
            elif depth >= len(current_path):
                neighbors = graph.get_neighbors(current_node)
                neighbors.reverse()
                for edge_node, cost in neighbors:
                    new_path = current_path.copy()
                    new_path.append(edge_node)
                    frontier.append((edge_node, new_path, cost + current_cost))
    # Return false if target is not found
    return False

def id(graph, app, origin, target):
    depth = 0
    while True:
        discovered = True
        result = search(graph, app, origin, target, depth)
        if result is False:
            # Check if all nodes have been discovered
            for node in graph.nodes:
                if node.discovered is False:
                    discovered = False
                    break
            if discovered:
                return False
            else:
                depth += 1
        else:
            return result + (depth,)
