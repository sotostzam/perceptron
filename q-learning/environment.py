import tkinter as tk
import numpy as np
import time
import random
import agent

# Canvas Parameters
canvas_width = 500
canvas_height = 500
root = tk.Tk()
w, h = canvas_width // 2, canvas_height // 2
canvas = tk.Canvas(root, width = canvas_width, height = canvas_height)
canvas.pack()

# Reward Table
boundaries = np.ones((canvas_width//50, canvas_height//50)) * - 1

# Wall objects
wall_objects = [[0 for x in range(canvas_width//50)] for y in range(canvas_height//50)]

max_reward = 0

agt = agent.Agent(0, 1)

# Agent starting Position (columns, rows)
AGENT_LOCATION = [0, 0]
wall_objects[AGENT_LOCATION[0]][AGENT_LOCATION[1]] = canvas.create_rectangle(AGENT_LOCATION[0], AGENT_LOCATION[1], AGENT_LOCATION[0] + 50, AGENT_LOCATION[1] + 50, fill="red")

def translateCoordinates(x, y, action):
    position_x = 0
    for i in range(0,10):
        if x > position_x and x < position_x + 50:
            position_y = 0
            for j in range(0, 10):
                if y > position_y and y < position_y + 50:
                    if action == 1:
                        print("Add wall to position: " + str(i) + "," + str(j))
                        if wall_objects[i][j] == 0:
                            wall_objects[i][j] = canvas.create_rectangle(position_x, position_y, position_x+50, position_y+50, fill="black")
                        else:
                            canvas.delete(wall_objects[i][j])
                            wall_objects[i][j] = 0
                            wall_objects[i][j] = canvas.create_rectangle(position_x, position_y, position_x+50, position_y+50, fill="black")
                        boundaries[i, j] = -10
                    elif action == 2:
                        print("Add end position: " + str(i) + "," + str(j))
                        if wall_objects[i][j] == 0:
                            wall_objects[i][j] = canvas.create_rectangle(position_x, position_y, position_x+50, position_y+50, fill="green")
                        else:
                            canvas.delete(wall_objects[i][j])
                            wall_objects[i][j] = 0
                            wall_objects[i][j] = canvas.create_rectangle(position_x, position_y, position_x+50, position_y+50, fill="green")
                        boundaries[i, j] = 100
                    else:
                        print("Remove object: " + str(i) + "," + str(j))
                        canvas.delete(wall_objects[i][j])
                        wall_objects[i][j] = 0
                        boundaries[i, j] = -1
                    break
                else:
                    position_y += 50
            break
        else:
            position_x += 50

# Determine the origin by clicking
def getAction(event, action):
    global x0,y0
    x0 = event.x
    y0 = event.y
    translateCoordinates(x0, y0, action)

#mouseclick event
root.bind("<Button 1>", lambda event : getAction(event, 1))
root.bind("<Button 2>", lambda event : getAction(event, 2))
root.bind("<Button 3>", lambda event : getAction(event, 3))

def can_move(direction):
    global max_reward
    try:
        if direction == 0 and AGENT_LOCATION[0] > 0:      # Move Left
            if boundaries[AGENT_LOCATION[0] - 1, AGENT_LOCATION[1]] > -10:
                max_reward += boundaries[AGENT_LOCATION[0] - 1, AGENT_LOCATION[1]]
                return True
            else:
                return False
        elif direction == 1 and AGENT_LOCATION[0] < 9 :       # Move Right
            if boundaries[AGENT_LOCATION[0] + 1, AGENT_LOCATION[1]] > -10:
                max_reward += boundaries[AGENT_LOCATION[0] + 1, AGENT_LOCATION[1]]
                return True
            else:
                return False
        elif direction == 2 and AGENT_LOCATION[1] > 0:                                                                # Move Up
            if boundaries[AGENT_LOCATION[0], AGENT_LOCATION[1] - 1] > -10:
                max_reward += boundaries[AGENT_LOCATION[0], AGENT_LOCATION[1] - 1]
                return True
            else:
                return False
        elif direction == 3 and AGENT_LOCATION[1] < 9:                                                                # Move Down
            if boundaries[AGENT_LOCATION[0], AGENT_LOCATION[1] + 1] > -10:
                max_reward += boundaries[AGENT_LOCATION[0], AGENT_LOCATION[1] + 1]
                return True
            else:
                return False
        else:
            pass
    except Exception:
        print(Exception)

def move(action):
    global max_reward
    x, y = 0, 0
    object_ID = wall_objects[AGENT_LOCATION[0]][AGENT_LOCATION[1]]
    previous_location = AGENT_LOCATION
    agent_moved = False
    if action == 0 and can_move(0):         # Move Left
        x = -50
        AGENT_LOCATION[0] -= 1
        agent_moved = True
    elif action == 1 and can_move(1):       # Move Right
        x = 50
        AGENT_LOCATION[0] += 1
        agent_moved = True
    elif action == 2 and can_move(2):       # Move Up
        y = -50
        AGENT_LOCATION[1] -= 1
        agent_moved = True
    elif action == 3 and can_move(3):       # Move Down
        y = 50
        AGENT_LOCATION[1] += 1
        agent_moved = True
    else:
        print("Can't move! Wall found!")
        max_reward -= 100
    if agent_moved:
        canvas.move(object_ID, x, y)
        wall_objects[previous_location[0]][previous_location[1]] = 0
        wall_objects[AGENT_LOCATION[0]][AGENT_LOCATION[1]] = object_ID
    print("Reward: " + str(max_reward))

def autoMode():
    for i in range (0, 50):
        move(random.randrange (0,4))
        canvas.update()
        time.sleep(.2)

def keypress(event):
    if event.char == "a" or event.keycode == 37:    move(0)
    elif event.char == "d" or event.keycode == 39:  move(1)
    elif event.char == "w" or event.keycode == 38:  move(2)
    elif event.char == "s": autoMode()
    elif event.keycode == 40:  move(3)
    

root.bind("<Key>", keypress)
root.bind("<Key>", keypress)

root.mainloop()