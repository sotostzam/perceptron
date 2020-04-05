def backtracking_search(graph):
    if recursive_backtracking(graph):
        print("Graph colored successfully!")
    else:
        print("Can not satisfy contraints.")

def recursive_backtracking(graph):
    if graph.constrains_satisfied():
        return graph.states
    current_state = graph.get_uncolored_node()
    if current_state:
        for color in graph.colors:
            if graph.is_valid_color(current_state, color):
                graph.set_color(current_state, color)
                result = recursive_backtracking(graph)
                if result is not False:
                    return result
                graph.uncolor(current_state)
    return False
