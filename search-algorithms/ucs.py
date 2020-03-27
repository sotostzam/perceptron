from queue import PriorityQueue
import time

def search(graph, canvas, origin, target):
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
        time.sleep(0.2)

        if current_node.discovered != True:
            current_node.discovered = True

            if current_node == target_node:
                current_path.append(current_node)

                # Reset canvas
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
