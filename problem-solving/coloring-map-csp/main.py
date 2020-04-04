import map

def main():
    australia = map.Region()
    australia.populate()
    australia.backtracking_search()
    australia.window.mainloop()

if __name__ == "__main__":
    main()