import time

def search(graph, canvas, origin, target):
    # Make sure nodes are undiscovered initially
    graph.reset_nodes()
    target_node = graph.get_node_obj(target)
    origin_node = graph.get_node_obj(origin)
    # BFS uses a FIFO queue structure as frontier (First in first out)
    frontier = [(origin_node, [origin_node], 0)]
    origin_node.discovered = True
    while frontier:
        current_node, current_path, current_cost = frontier.pop(0)

        ## Reset canvas
        for item in graph.nodes:
            canvas.itemconfig(item.obj, fill='grey')
        for item in graph.edges:
            canvas.itemconfig(item[3], width = 3, fill='black')

        for item in range(0, len(current_path)):
            canvas.itemconfig(current_path[item].obj, fill='red')
            if item < len(current_path)-1:
                for edge in graph.edges:
                    if edge[0] == current_path[item] and edge[1] == current_path[item + 1] or edge[1] == current_path[item] and edge[0] == current_path[item + 1]:
                        canvas.itemconfig(edge[3], fill='red')
        canvas.update()
        time.sleep(0.5)

        if current_node == target_node:
            return current_path, current_cost
        neighbors = graph.get_neighbors(current_node)
        for edge_node, cost in neighbors:
            if edge_node.discovered != True:
                edge_node.discovered = True
                new_path = current_path.copy()
                new_path.append(edge_node)
                frontier.append((edge_node, new_path, cost + current_cost))
    # Return false if target is not found
    return False
