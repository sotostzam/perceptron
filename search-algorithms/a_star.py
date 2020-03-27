from queue import PriorityQueue
import math, time

def evaluate(node1, node2):
    item = math.sqrt((node2.x - node1.x)**2 + (node2.y - node1.y)**2)
    #item = abs((node1.x - node2.x)) + abs((node1.y - node2.y))
    return item

def search(graph, canvas, origin, target):
    # Make sure nodes are undiscovered initially
    graph.reset_nodes()
    origin_node = graph.get_node_obj(origin)
    target_node = graph.get_node_obj(target)
    # A* uses a priority queue as frontier. Priority is determined by the cost
    frontier = PriorityQueue()
    # Frontier is a tuple of (priority, (node, path_to_node, total_cost))                    
    frontier.put((0 + graph.get_distance(origin_node), (origin_node, [], 0)))
    while frontier.qsize() > 0:
        _ , state = frontier.get()
        current_node = state[0]
        current_path = state[1]
        current_cost = state[2]

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
                    new_priority = new_cost + graph.get_distance(current_node)
                    frontier.put((new_priority, (edge_node, new_path, new_cost)))
    # Return false if target is not found
    return False
