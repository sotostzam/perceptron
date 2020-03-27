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
    # Best first search evaluates beft node like useing a priority queue (Min Heap)
    frontier = PriorityQueue()
    # Frontier is a tuple of (priority, (node, path_to_node, total_cost))
    frontier.put((evaluate(origin_node, target_node), (origin_node, [origin_node], 0)))
    while frontier:
        # Pick the best node according to the heuristic value
        _ , state = frontier.get()
        current_node, path, total_cost = state
        current_node.discovered = True

        # Reset canvas
        for item in graph.nodes:
            canvas.itemconfig(item.obj, fill='grey')
        for item in graph.edges:
            canvas.itemconfig(item[3], width = 3, fill='black')

        for item in range(0, len(path)):
            canvas.itemconfig(path[item].obj, fill='red')
            canvas.tag_raise(path[item].obj)
            if item < len(path)-1:
                for edge in graph.edges:
                    if edge[0] == path[item] and edge[1] == path[item + 1] or edge[1] == path[item] and edge[0] == path[item + 1]:
                        canvas.itemconfig(edge[3], fill='red')
        canvas.update()
        time.sleep(0.5)

        if current_node is target_node:
            return path, total_cost
        neighbors = graph.get_neighbors(current_node)
        if neighbors:
            for neighbor_node, cost in neighbors:
                if neighbor_node.discovered is False:
                    new_cost = total_cost + cost
                    new_path = path.copy()
                    new_path.append(neighbor_node)
                    frontier.put((evaluate(neighbor_node, target_node), (neighbor_node, new_path, new_cost)))
        else:
            return False
    return False
