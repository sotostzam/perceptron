import tkinter as tk
import numpy as np
import time
import random

# Window Interface Parameters
window = tk.Tk()
window.title("Reinforcement Learning")
window.rowconfigure(0, minsize=500, weight=1)
window.columnconfigure(1, minsize=500, weight=1)

main_menu = tk.Frame(window)

episodes_text = tk.StringVar()
tries_text = tk.StringVar()
rewards_text = tk.StringVar()
episodes_text.set("Episode: N/A")
tries_text.set("Tries left: N/A")
rewards_text.set("Reward: N/A")

label_epoch  = tk.Label(main_menu, textvariable=episodes_text)
label_tries  = tk.Label(main_menu, textvariable=tries_text)
label_reward = tk.Label(main_menu, textvariable=rewards_text)

label_epoch.grid(row=0, column=0, sticky="ew", padx=5, pady=10)
label_tries.grid(row=1, column=0, sticky="ew", padx=5, pady=10)
label_reward.grid(row=2, column=0, sticky="ew", padx=5, pady=10)

btn_start = tk.Button(main_menu, text="Start", width=20, height=2)
btn_reset = tk.Button(main_menu, text="Reset", width=20, height=2)
btn_exit  = tk.Button(main_menu, text="Exit",  width=20, height=2, command=window.destroy)

btn_start.grid(row=3, column=0, sticky="ew", padx=5, pady=10)
btn_reset.grid(row=4, column=0, sticky="ew", padx=5, pady=10)
btn_exit.grid(row=5, column=0, sticky="ew", padx=5, pady=10)

main_menu.grid(row=0, column=0, sticky="ns")

canvas_width  = 500
canvas_height = 500
w, h = canvas_width // 2, canvas_height // 2
canvas = tk.Canvas(master = window, width = canvas_width, height = canvas_height, bg="grey")
canvas.grid(row=0, column=1, sticky="nsew")

####################################### FIX ME ################################################
# Reward Table
boundaries = np.ones((canvas_width//50, canvas_height//50)) * - 1
# Wall objects
wall_objects = [[0 for x in range(canvas_width//50)] for y in range(canvas_height//50)]
max_reward = 0
###############################################################################################

LEARNING_RATE   = 0.1
DISCOUNT        = 0.95              # How much value future rewards over current rewards
EPISODES        = 25000
INITIAL_POS     = [0, 0]
AGENT_LOCATION  = INITIAL_POS       # Agent starting Position (columns, rows)
GOAL_LOCATION   = [9, 9]

q_table = np.random.uniform(low=-2, high=0, size = (canvas_width//50, canvas_height//50, 4))   # Needs fixing

wall_objects[AGENT_LOCATION[0]][AGENT_LOCATION[1]] = canvas.create_rectangle(AGENT_LOCATION[0], AGENT_LOCATION[1], AGENT_LOCATION[0] + 50, AGENT_LOCATION[1] + 50, fill="red")

def translateCoordinates(x, y, action):
    global GOAL_LOCATION
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
                        GOAL_LOCATION = [i, j]
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
canvas.bind("<Button 1>", lambda event : getAction(event, 1))
canvas.bind("<Button 2>", lambda event : getAction(event, 2))
canvas.bind("<Button 3>", lambda event : getAction(event, 3))

def can_move(direction):
    try:
        if direction == 0 and AGENT_LOCATION[0] > 0:      # Move Left
            if boundaries[AGENT_LOCATION[0] - 1, AGENT_LOCATION[1]] > -10:
                return True
            else:
                return False
        elif direction == 1 and AGENT_LOCATION[0] < 9 :       # Move Right
            if boundaries[AGENT_LOCATION[0] + 1, AGENT_LOCATION[1]] > -10:
                return True
            else:
                return False
        elif direction == 2 and AGENT_LOCATION[1] > 0:                                                                # Move Up
            if boundaries[AGENT_LOCATION[0], AGENT_LOCATION[1] - 1] > -10:
                return True
            else:
                return False
        elif direction == 3 and AGENT_LOCATION[1] < 9:                                                                # Move Down
            if boundaries[AGENT_LOCATION[0], AGENT_LOCATION[1] + 1] > -10:
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
        max_reward += boundaries[AGENT_LOCATION[0], AGENT_LOCATION[1]]
        agent_moved = True
    elif action == 1 and can_move(1):       # Move Right
        x = 50
        AGENT_LOCATION[0] += 1
        max_reward += boundaries[AGENT_LOCATION[0], AGENT_LOCATION[1]]
        agent_moved = True
    elif action == 2 and can_move(2):       # Move Up
        y = -50
        AGENT_LOCATION[1] -= 1
        max_reward += boundaries[AGENT_LOCATION[0], AGENT_LOCATION[1]]
        agent_moved = True
    elif action == 3 and can_move(3):       # Move Down
        y = 50
        AGENT_LOCATION[1] += 1
        max_reward += boundaries[AGENT_LOCATION[0], AGENT_LOCATION[1]]
        agent_moved = True
    if agent_moved:
        canvas.move(object_ID, x, y)
        wall_objects[previous_location[0]][previous_location[1]] = 0
        wall_objects[AGENT_LOCATION[0]][AGENT_LOCATION[1]] = object_ID
        rewards_text.set("Reward: " + str(max_reward))
        return -1
    else:
        max_reward -= 100
        rewards_text.set("Reward: " + str(max_reward))
        return -100

def reset():
    global AGENT_LOCATION
    canvas.delete(wall_objects[AGENT_LOCATION[0]][AGENT_LOCATION[1]])
    AGENT_LOCATION = INITIAL_POS
    wall_objects[AGENT_LOCATION[0]][AGENT_LOCATION[1]] = canvas.create_rectangle(AGENT_LOCATION[0], AGENT_LOCATION[1], AGENT_LOCATION[0] + 50, AGENT_LOCATION[1] + 50, fill="red")

done = False
def train():
    btn_start.config(state="disabled")
    global max_reward
    action = np.argmax(q_table[AGENT_LOCATION[0]][AGENT_LOCATION[1]])
    current_state = AGENT_LOCATION
    for i in range (1, EPISODES):
        episodes_text.set("Episode: " + str(i))
        max_reward = 0
        for j in range (100, 0, -1):
            tries_text.set("Tries left: " + str(j))
            reward = move(action)
            new_state = tuple(q_table[AGENT_LOCATION[0]][AGENT_LOCATION[1]].astype(np.int))
            if not done:
                max_future_q = np.max(new_state)
                current_q    = q_table[current_state[0]][current_state[1]][action]
                new_q        = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
                q_table[new_state[0]][new_state[1]][action] = new_q
            if AGENT_LOCATION == GOAL_LOCATION:
                print("GOAL!")
                reset()
                break
            #if i == 1 or i % 100 == 0: 
            canvas.update()
            time.sleep(.1)
            current_state = new_state
    btn_start.config(state="normal")

def keypress(event):
    if event.char == "a" or event.keycode == 37:    move(0)
    elif event.char == "d" or event.keycode == 39:  move(1)
    elif event.char == "w" or event.keycode == 38:  move(2)
    elif event.char == "s" or event.keycode == 40:  move(3)

window.bind("<Key>", keypress)
btn_start.configure(command=train)

window.mainloop()