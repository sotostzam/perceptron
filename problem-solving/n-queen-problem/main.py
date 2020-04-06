import graph, ac3

def main():
    board = graph.Board(8)
    ac3.search(board)
    board.window.mainloop()

if __name__ == "__main__":
    main()