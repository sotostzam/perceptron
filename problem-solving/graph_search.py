import blind_search_algorithms.bfs as bfs
import blind_search_algorithms.dls as dls
import blind_search_algorithms.ucs as ucs
import heuristic_search_algorithms.hill_climbing as hc
import heuristic_search_algorithms.bestFS as bestFS
import heuristic_search_algorithms.a_star as a_star
import graph
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time

class gui():

    def __init__(self, width, height):
        self.window = tk.Tk()
        self.window.title("Search Algorithms")
        self.window.rowconfigure(0, minsize=500, weight=1)
        self.window.columnconfigure(0, minsize=200, weight=1)

        # Main Menu
        self.main_menu = tk.Frame(self.window)
        self.main_menu.grid(row=0, column=0, sticky="ns", padx=10, pady=10)
        self.main_menu.rowconfigure(0, minsize=20, weight=0)

        self.top_label = tk.Label(self.main_menu, text = "Choose search algorithm:")
        self.top_label.grid(row=0, column=0)

        self.algorithms = ['Breadth-first Search', 
                           'Depth-first Search',
                           'Depth Limited Search',
                           'Iterative Deepening Search',
                           'Uniform Cost Search',
                           'Hill Climbing',
                           'Best First Search',
                           'Beam Search',
                           'A* (A-star)',]
        self.combo = ttk.Combobox(self.main_menu, values = self.algorithms, state="readonly", width=25)
        self.combo.bind("<<ComboboxSelected>>", self.comboSelection)
        self.combo.grid(row=1, column=0)

        self.node_selection = tk.Frame(self.main_menu)
        self.node_selection.grid(row=2, column=0, sticky="ns")
        self.node_selection.columnconfigure(0, minsize=20)

        self.node_start = tk.Label(self.node_selection, text="From:")
        self.node_start.grid(row=0, column=0, sticky="we")
        self.node_goal = tk.Label(self.node_selection, text="To:")
        self.node_goal.grid(row=0, column=1, sticky="we")

        self.node_start_input = tk.Entry(self.node_selection, justify='center')
        self.node_start_input.grid(row=1, column=0, sticky="we")
        self.node_start_input.insert(0, "Arad")
        self.node_goal_input = tk.Entry(self.node_selection, justify='center')
        self.node_goal_input.grid(row=1, column=1, sticky="we")
        self.node_goal_input.insert(0, "Bucharest")

        self.depth_selection = tk.Frame(self.main_menu)
        self.depth_selection.grid(row=3, column=0, sticky="ns", pady=10)
        self.depth_label = tk.Label(self.depth_selection, text="Depth limit:")
        self.depth_label.grid(row=0, column=0)
        self.depth_input = tk.Entry(self.depth_selection, justify='center', state="disabled")
        self.depth_input.grid(row=1, column=0, sticky="we")
        self.depth_selection.grid_remove()
    
        self.beam_selection = tk.Frame(self.main_menu)
        self.beam_selection.grid(row=3, column=0, sticky="ns", pady=10)
        self.beam_label = tk.Label(self.beam_selection, text="Beam value:")
        self.beam_label.grid(row=0, column=0)
        self.beam_input = tk.Entry(self.beam_selection, justify='center')
        self.beam_input.grid(row=1, column=0, sticky="we")
        self.beam_selection.grid_remove()

        self.btn_start = tk.Button(self.main_menu, width=20, height=2, command=self.run, text="Run")
        self.btn_start.grid(row=4, column=0, padx=5, pady=10)
        self.btn_start.configure(state='disabled')

        # Canvas Panel Parameters
        self.canvas = tk.Canvas(master = self.window, width = width, height = height, bg="white")
        self.canvas.grid(row=0, column=1, sticky="nsew")

    # Run application with selected algorithm
    def run(self):
        selection = self.combo.current()
         # Make sure nodes are undiscovered initially
        graph.reset_nodes()
        origin = self.node_start_input.get()
        goal = self.node_goal_input.get()
        path = None
        if graph.get_node_obj(origin) is None:
            tk.messagebox.showwarning("Warning", "Starting node does not exist!")
        else:
            self.btn_start.config(state="disabled")
            # Algorithms return either a tuple of (found_path, total_cost) or False
            if selection is 0:
                path = bfs.search(graph, app, origin, goal)
            elif selection is 1:
                path = dls.search(graph, app, origin, goal)
            elif selection is 2:
                selected_depth = int(self.depth_input.get())
                path = dls.search(graph, app, origin, goal, depth = selected_depth)
            elif selection is 3:
                path = dls.id(graph, app, origin, goal)
            elif selection is 4:
                path = ucs.search(graph, app, origin, goal)
            else:
                if graph.get_node_obj(goal) is None:
                    tk.messagebox.showwarning("Warning", "Target node does not exist!")
                else:
                    if selection is 5:
                        path = hc.search(graph, app, origin, goal)
                    elif selection is 6:
                        path = bestFS.search(graph, app, origin, goal)
                    elif selection is 7:
                        selected_beam = int(self.beam_input.get())
                        path = bestFS.search(graph, app, origin, goal, beam = selected_beam)
                    else:
                        path = a_star.search(graph, app, origin, goal)
            if path is None:
                pass
            elif path is not False:
                app.update_canvas(path[0], found = True)
                tk.messagebox.showinfo("Results", "Path sucessfully found!\n Total cost: " + str(path[1]))
            else:
                tk.messagebox.showwarning("Results", "Path to target node not found.")
            self.btn_start.config(state="normal")

    # ComboBox selection callback
    def comboSelection(self, event):
        self.btn_start.configure(state='normal')
        # DFS Enable depth selection
        if self.combo.current() > 0 and self.combo.current() <= 3:
            self.depth_selection.grid()
            if self.combo.current() is 2:
                self.depth_input.configure(state='normal')
            else:
                self.depth_input.configure(state='disabled')
        else:
            self.depth_selection.grid_remove()
        # BestFS Enable beam selection
        if self.combo.current() is 7:
            self.beam_selection.grid()
        else:
            self.beam_selection.grid_remove()

    # Helper function to reset canvas items
    def reset_canvas(self):
        for item in graph.nodes:
            if item.discovered:
                self.canvas.itemconfig(item.obj, fill='blue')
            else:
                self.canvas.itemconfig(item.obj, fill='grey')
        for item in graph.edges:
            self.canvas.itemconfig(item[3], width = 3, fill='black')

    # Helper function to update canvas
    def update_canvas(self, path, search_node = None, time_value = .5, found = None):
        self.reset_canvas()
        if search_node != None:
            new_path = path.copy()
            new_path.append(search_node)
            path = new_path.copy()
        for item in range(0, len(path)):
            if found:
                self.canvas.itemconfig(path[item].obj, fill='green')
            else:
                self.canvas.itemconfig(path[item].obj, fill='red')
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
    
    def update_depth(self, depth):
        self.depth_input.configure(state='normal')
        app.depth_input.delete(0, 'end')
        app.depth_input.insert(0, str(depth))
        self.depth_input.configure(state='disabled')

if __name__ == "__main__":
    app = gui(800, 500)
    graph = graph.Graph()
    graph.load_data('tour_romania.json', app.canvas)
    graph.show_info(app.canvas)
    app.window.mainloop()
