import graph, bs

def main():
    # Randomize means the order of the state-nodes is randomized
    region = graph.Region(randomize = True)
    bs.backtracking_search(region)
    region.window.mainloop()

if __name__ == "__main__":
    main()