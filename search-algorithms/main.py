import graph, bfs, dfs , ucs

if __name__ == "__main__":
    graph = graph.Graph()
    graph.load_data('tour_romania.json')

    bfs.search(graph, "Arad", "Bucharest")
    dfs.search(graph, "Arad", "Bucharest")
    ucs.search(graph, "Arad", "Bucharest")
