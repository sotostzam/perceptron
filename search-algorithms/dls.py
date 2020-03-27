import math, time

def search(graph, canvas, origin, target, depth = math.inf):
    # Make sure nodes are undiscovered initially
    graph.reset_nodes()
    target_node = graph.get_node_obj(target)
    # DFS uses a LIFO stack structure as frontier (Last in first out)
    frontier = [(graph.get_node_obj(origin), [graph.get_node_obj(origin)], 0)]
    while frontier:
        current_node, current_path, current_cost = frontier.pop()

        ## Reset canvas
        for item in graph.nodes:
            canvas.itemconfig(item.obj, fill='grey')
        for item in graph.edges:
            canvas.itemconfig(item[3], width = 3, fill='black')

        for item in range(0, len(current_path)):
            canvas.itemconfig(current_path[item].obj, fill='red')
            canvas.tag_raise(current_path[item].obj)
            if item < len(current_path)-1:
                for edge in graph.edges:
                    if edge[0] == current_path[item] and edge[1] == current_path[item + 1] or edge[1] == current_path[item] and edge[0] == current_path[item + 1]:
                        canvas.itemconfig(edge[3], fill='red')
        canvas.update()
        time.sleep(0.5)

        if current_node.discovered != True:
            current_node.discovered = True
            if current_node == target_node:
                return current_path, current_cost
            elif depth > len(current_path):
                neighbors = graph.get_neighbors(current_node)
                neighbors.reverse()
                for edge_node, cost in neighbors:
                    new_path = current_path.copy()
                    new_path.append(edge_node)
                    frontier.append((edge_node, new_path, cost + current_cost))
    # Return false if target is not found
    return False

def id(graph, canvas, origin, target):
    depth = 0
    while True:
        discovered = True
        result = search(graph, canvas, origin, target, depth)
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
