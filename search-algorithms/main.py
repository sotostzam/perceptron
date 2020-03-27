import graph, bfs, dls , ucs
import hill_climbing as hc
import bestFS, a_star

def print_results(name, result):
    print("----- " + name + " -----")
    if result:
        print("Path: " + ' -> '.join(result[0]))
        print("Cost: " + str(result[1]))
        if len(result) is 3:
            print("Depth: " + str(result[2]))
    else:
        print("Path not found!")

if __name__ == "__main__":
    graph = graph.Graph()
    graph.load_data('tour_romania.json')

    # Algorithms return either a tuple of (found_path, total_cost) or False
    print_results("Breadth-first search", bfs.search(graph, "Oradea", "Bucharest"))
    print_results("Depth-first search", dls.search(graph, "Oradea", "Bucharest"))
    print_results("Depth limited search", dls.search(graph, "Oradea", "Bucharest", depth = 5))
    print_results("Iterative deepening search", dls.id(graph, "Oradea", "Bucharest"))
    print_results("Uniform cost search", ucs.search(graph, "Oradea", "Bucharest"))
    print_results("Hill Climbing",  hc.search(graph, "Oradea", "Bucharest"))
    print_results("Best First Search", bestFS.search(graph, "Oradea", "Bucharest"))
    print_results("A* (A-star)", a_star.search(graph, "Oradea", "Bucharest"))

    ########### Graphical User Interface ###########
    import tkinter as tk
    import time

    def drawOnCanvas(event):
        print(event.x)
        print(event.y)

    window = tk.Tk()
    window.title("Search Algorithms")
    window.rowconfigure(0, minsize=500, weight=1)
    window.columnconfigure(0, minsize=150, weight=1)

    # Canvas Panel Parameters
    canvas = tk.Canvas(master = window, width = 800, height = 500, bg="white")
    canvas.grid(row=0, column=0, sticky="nsew")

    # Bind Events
    canvas.bind("<Button 1>", lambda event : drawOnCanvas(event))
    canvas.bind("<Button 2>", lambda event : drawOnCanvas(event))
    canvas.bind("<Button 3>", lambda event : drawOnCanvas(event))

    edge_obj = []
    node_obj = []
    for edge in graph.edges:
        edge_obj.append(canvas.create_line(edge[0].x, edge[0].y, edge[1].x, edge[1].y, width = 3, fill='black'))
    for node in graph.nodes:
        node_obj.append(canvas.create_oval(node.x - 10, node.y - 10, node.x + 10, node.y + 10, fill="grey"))
        # canvas.create_text(node.x + 40, node.y, font="Purisa", text=node.value)               # Names of cities      

    window.mainloop()
