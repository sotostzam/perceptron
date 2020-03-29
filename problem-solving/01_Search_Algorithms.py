import graph
import gui_romania as gui

if __name__ == "__main__":
    graph = graph.Graph()
    app = gui.Gui(graph)
    graph.load_data('tour_romania.json', app.canvas)
    graph.show_info(app.canvas)
    app.window.mainloop()
