import graph, search

def main():
    board = graph.Board(8)
    # search.bt_search(board)         # Backtracking Search
    search.bt_mrv(board)              # Backtracking with MRV Search
    board.window.mainloop()

if __name__ == "__main__":
    main()