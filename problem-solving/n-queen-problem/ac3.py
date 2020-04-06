def search(graph):
    result = recursive_ac3(graph)
    if result:
        print("Solution found:")
        item = 0
        while item < len(graph.grid):
            tempRow = "["
            for i in range(0, len(graph.grid)):
                tempRow += str(graph.grid[i][item]) + ", "
            print(tempRow[0:-2] + "]")
            item += 1
    else:
        print("Can not find solution.")

def recursive_ac3(graph):
    if not graph.get_unassigned_queen():
        return graph.grid
    current_queen = graph.get_unassigned_queen()
    if current_queen:
        for row in range(0, len(graph.grid[current_queen.num - 1])):
            if graph.is_valid_move(current_queen, row):
                graph.place_queen(current_queen, row)
                result = recursive_ac3(graph)
                if result is not False:
                        return result
        graph.reset_queen(current_queen)
    return False