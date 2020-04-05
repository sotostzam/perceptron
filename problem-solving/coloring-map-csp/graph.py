import tkinter as tk
import random, time

class Node():
    def __init__(self, canvas, value, pos, color):
        self.value = value
        self.pos = pos
        self.color = color
        self.obj = canvas.create_oval(pos[0]-25, pos[1]-25, pos[0]+25, pos[1]+25, fill="white", outline="black", width = 2)
        self.name = canvas.create_text(pos[0], pos[1], font=("Purisa", 12, "bold"), text = value, fill="black")
        self.neighbors = []

    def set_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

class Region():
    def __init__(self, randomize = False):
        # Window and canvas initialization parameters
        self.width  = 500
        self.height = 400
        self.window = tk.Tk()
        self.window.title("Australia Map coloring CSP")
        self.canvas = tk.Canvas(master = self.window, width = self.width, height = self.height, bg = "white")
        self.canvas.grid(row = 0, column = 0, sticky = "nsew")

        self.image = tk.PhotoImage(file = "australia.png")
        self.image.zoom(2, 2)
        self.canvas.create_image(50, 0, image = self.image, anchor = "nw")

        self.states = []
        self.lines  = []
        self.colors = ["red", "green", "blue"]

        self.states.append(Node(self.canvas, "WA" , [130, 190], None))
        self.states.append(Node(self.canvas, "NT" , [250, 120], None))
        self.states.append(Node(self.canvas, "SA" , [270, 225], None))
        self.states.append(Node(self.canvas, "Q"  , [365, 165], None))
        self.states.append(Node(self.canvas, "NSW", [380, 260], None))
        self.states.append(Node(self.canvas, "V"  , [345, 310], None))
        self.states.append(Node(self.canvas, "T"  , [365, 370], None))

        self.get_node_obj("SA").set_neighbor(self.get_node_obj("WA"))
        self.get_node_obj("SA").set_neighbor(self.get_node_obj("NT"))
        self.get_node_obj("SA").set_neighbor(self.get_node_obj("Q"))
        self.get_node_obj("SA").set_neighbor(self.get_node_obj("NSW"))
        self.get_node_obj("SA").set_neighbor(self.get_node_obj("V"))
        self.get_node_obj("WA").set_neighbor(self.get_node_obj("NT"))
        self.get_node_obj("WA").set_neighbor(self.get_node_obj("SA"))
        self.get_node_obj("SA").set_neighbor(self.get_node_obj("NT"))
        self.get_node_obj("NT").set_neighbor(self.get_node_obj("Q"))
        self.get_node_obj("NT").set_neighbor(self.get_node_obj("WA"))
        self.get_node_obj("NT").set_neighbor(self.get_node_obj("SA"))
        self.get_node_obj("Q").set_neighbor(self.get_node_obj("NSW"))
        self.get_node_obj("Q").set_neighbor(self.get_node_obj("NT"))
        self.get_node_obj("Q").set_neighbor(self.get_node_obj("SA"))
        self.get_node_obj("NSW").set_neighbor(self.get_node_obj("V"))
        self.get_node_obj("NSW").set_neighbor(self.get_node_obj("SA"))
        self.get_node_obj("NSW").set_neighbor(self.get_node_obj("Q"))
        self.get_node_obj("V").set_neighbor(self.get_node_obj("SA"))
        self.get_node_obj("V").set_neighbor(self.get_node_obj("NSW"))

        for state in self.states:
            neighbors = state.neighbors
            for neighbor in neighbors:
                exist = False
                for connection in self.lines:
                    if connection[0] is state and connection[1] is neighbor:
                        exist = True
                        break
                    elif connection[0] is neighbor and connection[1] is state:
                        exist = True
                        break
                if not exist:
                    self.lines.append((state, neighbor))
                    line = self.canvas.create_line(state.pos[0], state.pos[1], neighbor.pos[0], neighbor.pos[1], width = 2, fill = 'black')
                    self.canvas.tag_lower(line)
        
        if randomize:
            random.shuffle(self.states)

    # Helper function to return the node object from a name
    def get_node_obj(self, node):
        for item in self.states:
            if node is item.value:
                return item

    # Helper function to select the next node that has no color
    def get_uncolored_node(self):
        for state in self.states:
            if state.color is None:
                return state

    # Helper function to check if color satisfies constraints
    def is_valid_color(self, state, color, update = True):
        if len(state.neighbors) > 0:
            if update:
                self.set_color(state, color)
                self.canvas.update()
            for neighbor in state.neighbors:
                if color == neighbor.color and neighbor.color != None:
                    if update:
                        self.uncolor(state)
                        self.canvas.update()
                    return False
            return True
        else:
            return True

    # Function to check if constraints are satisfied
    def constrains_satisfied(self):
        for state in self.states:
            if state.color is None:
                return False
            if self.is_valid_color(state, state.color, update = False) is False:
                return False
        return True

    # Helper function to set color to a node
    def set_color(self, node, color):
        node.color = color
        self.canvas.itemconfig(node.obj, fill=color)
        self.canvas.itemconfig(node.name, fill="white")
        self.canvas.update()
        time.sleep(0.3)

    # Helper function to remove color from a node
    def uncolor(self, node):
        node.color = None
        self.canvas.itemconfig(node.obj, fill="white")
        self.canvas.itemconfig(node.name, fill="black")
        self.canvas.update()
