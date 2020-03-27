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
    import tkinter as tk
    import time

    window = tk.Tk()
    window.title("Search Algorithms")
    window.rowconfigure(0, minsize=500, weight=1)
    window.columnconfigure(0, minsize=150, weight=1)

    # Canvas Panel Parameters
    canvas = tk.Canvas(master = window, width = 800, height = 500, bg="white")
    canvas.grid(row=0, column=0, sticky="nsew")

    graph = graph.Graph()
    graph.load_data('tour_romania.json', canvas)

    # Algorithms return either a tuple of (found_path, total_cost) or False
    # bfs.search(graph, canvas, "Oradea", "Bucharest")
    # dls.search(graph, canvas, "Oradea", "Bucharest")
    # dls.search(graph, canvas, "Oradea", "Bucharest", depth = 3)
    # dls.id(graph, canvas, "Oradea", "Bucharest")
    # ucs.search(graph, canvas, "Oradea", "Drobeta")
    # hc.search(graph, canvas, "Oradea", "Bucharest")
    # bestFS.search(graph, canvas, "Oradea", "Bucharest")
    # a_star.search(graph, canvas, "Oradea", "Mehadia")

    window.mainloop()
