import map

def main():
    australia = map.Region()
    australia.populate()
    australia.set_colors(("red", "green", "blue"))
    australia.find_sceme()
    australia.window.mainloop()

if __name__ == "__main__":
    main()