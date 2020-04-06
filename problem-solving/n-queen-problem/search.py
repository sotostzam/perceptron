import time
def bt_search(graph):
    result = backtracking(graph)
    if result:
        print("Solution found:")
        print_grid(graph.grid)
    else:
        print("Can not find solution.")

def backtracking(graph):
    if not graph.get_unassigned_queen():
        return graph.grid
    current_queen = graph.get_unassigned_queen()
    if current_queen:
        for row in range(0, len(graph.grid[current_queen.num - 1])):
            if graph.is_valid_move(current_queen, row):
                graph.place_queen(current_queen, row)
                result = backtracking(graph)
                if result is not False:
                        return result
        graph.reset_queen(current_queen)
    return False

def bt_mrv(graph):
    result = fc(graph)
    if result:
        print("Solution found:")
        print_grid(graph.grid)
    else:
        print("Can not find solution.")

def fc(graph):
    if not graph.get_unassigned_queen():
        return graph.grid
    current_queen = graph.get_unassigned_queen()
    if current_queen:
        for move in current_queen.domain:
            graph.place_queen(current_queen, move)
            changes = fw_check(graph, current_queen)
            result = fc(graph)
            if result is not False:
                    return result
            revert_domains(graph.queens, changes)
        graph.reset_queen(current_queen)
    return False

def fw_check(graph, queen):
    old_domains = []
    for item in graph.queens:
        tempList = list.copy(item.domain)
        old_domains.append(tempList)

    for i in range(queen.num, len(graph.grid)):
        if queen.pos in graph.queens[i].domain:
            graph.queens[i].domain.remove(queen.pos)

    # Upper diagonal
    temp_col = queen.num
    temp_row = queen.pos - 1
    while temp_row >= 0 and temp_col < len(graph.grid):
        if temp_row in graph.queens[temp_col].domain:
            graph.queens[temp_col].domain.remove(temp_row)
        temp_col += 1
        temp_row -= 1

    # Lower diagonal
    temp_col = queen.num
    temp_row = queen.pos + 1
    while temp_row < len(graph.grid) and temp_col < len(graph.grid):
        if temp_row in graph.queens[temp_col].domain:
            graph.queens[temp_col].domain.remove(temp_row)
        temp_col += 1
        temp_row += 1

    return old_domains

def revert_domains(queens, old_domains):
    for i in range(0, len(queens)):
        queens[i].domain = []
        queens[i].domain = old_domains[i]

# Helper function to print grid in rows and then columns
def print_grid(grid):
    item = 0
    while item < len(grid):
        tempRow = ""
        for i in range(0, len(grid)):
            tempRow += str(grid[i][item]) + ", "
        print(tempRow[0:-2] + "")
        item += 1
    print()
    time.sleep(1)