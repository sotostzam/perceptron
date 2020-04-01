import math, time, random
import graph

def euclidean_distance(node_1, node_2):
    distance = math.sqrt((node_2.x - node_1.x)**2 + (node_2.y - node_1.y)**2)
    return distance

def get_total_distance(node_list):
    total_distance = 0
    for i in range(0, len(node_list)-2):
        total_distance += euclidean_distance(node_list[i], node_list[i+1])
    return total_distance

def solve(graph):
    best_distance = math.inf
    checked = []
    while True:
        checked.append(graph.nodes)
        path = []
        for node in graph.nodes:
            path.append(node.x)
            path.append(node.y)

        current_distance = get_total_distance(graph.nodes)
        if current_distance < best_distance:
            best_distance = current_distance
            graph.canvas_right.delete(graph.best_pathLine)
            graph.best_pathLine = graph.canvas_right.create_line(path, width = 2, fill = 'green')
            print(best_distance)

        graph.canvas_left.delete(graph.current_pathLine)
        graph.current_pathLine = graph.canvas_left.create_line(path, width = 2, fill = 'red')
        graph.canvas_left.tag_lower(graph.current_pathLine)
        graph.canvas_right.tag_lower(graph.best_pathLine)
        graph.canvas_left.update()
        graph.canvas_right.update()

        random.shuffle(graph.nodes)
        #time.sleep(.05)

if __name__ == "__main__":
    graph = graph.Graph(7)
    solve(graph)
    graph.window.mainloop()
