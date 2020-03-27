import graph, bfs, dls , ucs
import hill_climbing as hc
import bestFS, a_star
import tkinter as tk
import time

class gui():

    def __init__(self, width, height):
        self.window = tk.Tk()
        self.window.title("Search Algorithms")
        self.window.rowconfigure(0, minsize=500, weight=1)
        self.window.columnconfigure(0, minsize=150, weight=1)

        # Canvas Panel Parameters
        self.canvas = tk.Canvas(master = self.window, width = width, height = height, bg="white")
        self.canvas.grid(row=0, column=0, sticky="nsew")

    # Helper function to reset canvas items
    def reset_canvas(self):
        for item in graph.nodes:
            self.canvas.itemconfig(item.obj, fill='grey')
        for item in graph.edges:
            self.canvas.itemconfig(item[3], width = 3, fill='black')

    # Helper function to update canvas
    def update_canvas(self, path, time_value = None, found = None):
        self.reset_canvas()
        for item in range(0, len(path)):
            if found:
                self.canvas.itemconfig(path[item].obj, fill='green')
            else:
                self.canvas.itemconfig(path[item].obj, fill='red')
            self.canvas.tag_raise(path[item].obj)
            if item < len(path)-1:
                for edge in graph.edges:
                    if edge[0] == path[item] and edge[1] == path[item + 1] or edge[1] == path[item] and edge[0] == path[item + 1]:
                        self.canvas.itemconfig(edge[3], fill='red')
                        if found:
                            self.canvas.itemconfig(edge[3], fill='green')
                        else:
                            self.canvas.itemconfig(edge[3], fill='red')
        self.canvas.update()
        if time_value is not None:
            time.sleep(time_value)


if __name__ == "__main__":
    app = gui(800, 500)

    graph = graph.Graph()
    graph.load_data('tour_romania.json', app.canvas)

    # Make sure nodes are undiscovered initially
    graph.reset_nodes()

    # Algorithms return either a tuple of (found_path, total_cost) or False
    # path = bfs.search(graph, app, "Oradea", "Bucharest")
    # path = dls.search(graph, app, "Oradea", "Bucharest")
    # path = dls.search(graph, app, "Oradea", "Bucharest", depth = 3)
    # path = dls.id(graph, app, "Oradea", "Bucharest")
    # path = ucs.search(graph, app, "Oradea", "Bucharest")
    # path = hc.search(graph, app, "Oradea", "Bucharest")
    # path = bestFS.search(graph, app, "Oradea", "Bucharest")
    path = a_star.search(graph, app, "Oradea", "Bucharest")

    if path is not False:
        app.update_canvas(path[0], found = True)
    else:
        print("Not found")

    app.window.mainloop()
