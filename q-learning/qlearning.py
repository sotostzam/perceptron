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
b_rewards_text = tk.StringVar()
success_text = tk.StringVar()
episodes_text.set("Episode: N/A")
tries_text.set("Tries left: N/A")
rewards_text.set("Reward: N/A")
b_rewards_text.set("Best Score: N/A")
success_text.set("Success times: N/A")

label_epoch  = tk.Label(main_menu, textvariable=episodes_text)
label_tries  = tk.Label(main_menu, textvariable=tries_text)
label_reward = tk.Label(main_menu, textvariable=rewards_text)
label_b_reward = tk.Label(main_menu, textvariable=b_rewards_text)
label_success = tk.Label(main_menu, textvariable=success_text)

label_epoch.grid(row=0, column=0, sticky="ew", padx=5, pady=10)
label_tries.grid(row=1, column=0, sticky="ew", padx=5, pady=10)
label_reward.grid(row=2, column=0, sticky="ew", padx=5, pady=10)
label_b_reward.grid(row=3, column=0, sticky="ew", padx=5, pady=10)
label_success.grid(row=4, column=0, sticky="ew", padx=5, pady=10)

btn_start = tk.Button(main_menu, text="Start", width=20, height=2)
btn_reset = tk.Button(main_menu, text="Reset", width=20, height=2)
btn_exit  = tk.Button(main_menu, text="Exit",  width=20, height=2, command=window.destroy)

btn_start.grid(row=5, column=0, sticky="ew", padx=5, pady=10)
btn_reset.grid(row=6, column=0, sticky="ew", padx=5, pady=10)
btn_exit.grid(row=7, column=0, sticky="ew", padx=5, pady=10)

main_menu.grid(row=0, column=0, sticky="ns")

canvas_width  = 500
canvas_height = 500
w, h = canvas_width // 2, canvas_height // 2
canvas = tk.Canvas(master = window, width = canvas_width, height = canvas_height, bg="grey")
canvas.grid(row=0, column=1, sticky="nsew")

###############################################################################################

LEARNING_RATE   = 0.05
DISCOUNT        = 0.95      # How much value future rewards over current rewards
EPISODES        = 1000
ACTIONS         = np.array([0, 1, 2, 3])

###############################################################################################

initial_pos     = np.array([1, 0])
agent_pos       = np.copy(initial_pos)       # Agent starting Position (columns, rows)
goal_pos        = np.array([8, 9])
#q_table = np.random.uniform(low=-2, high=0, size = (canvas_width//50, canvas_height//50, 4))   # Needs fixing
q_table = np.zeros((canvas_width//50, canvas_height//50, 4))

# Initialize reward table to -1
reward_table = np.ones((canvas_width//50, canvas_height//50)) * - 1
reward_table[8,9] = 100

# Canvas objects list
canvas_objects = np.zeros((canvas_width//50, canvas_height//50), dtype=int)

###############################################################################################

canvas_objects[agent_pos[0], agent_pos[1]] = canvas.create_rectangle(agent_pos[1] * 50, agent_pos[0] * 50, agent_pos[1] * 50 + 50, agent_pos[0] * 50 + 50, fill="red")
canvas_objects[goal_pos[0], goal_pos[1]] = canvas.create_rectangle(goal_pos[1] * 50, goal_pos[0] * 50, goal_pos[1] * 50 + 50, goal_pos[0] * 50 + 50, fill="green")
canvas_objects[0, 1] = canvas.create_rectangle(0 * 50, 0 * 50, 0 * 50 + 50, 0 * 50 + 50, fill="black")

########################################## TEST MAZE ##########################################

for i in range (0, 10):
    reward_table[0, i] = -10
    reward_table[9, i] = -10

for i in range (1, 8):
    reward_table[i, 9] = -10
    reward_table[i+1, 0] = -10

for i in range(0, len(reward_table)):
    for j in range(0, len(reward_table[i])):
        if reward_table[i, j] == -10:
            canvas_objects[i, j] = canvas.create_rectangle(j * 50, i * 50, j * 50 + 50, i * 50 + 50, fill="black")

###############################################################################################
def drawOnCanvas(event, action):
    x = np.floor(event.x / 50).astype(int)      # Attention! This is mouse x coordinate but indicates columns in tables!
    y = np.floor(event.y / 50).astype(int)      # Attention! This is mouse y coordinate but indicates rows in tables!
    global goal_pos
    if action == 1:
        print("Add object: " + str(y) + "," + str(x))
        if canvas_objects[y, x] == 0:
            canvas_objects[y, x] = canvas.create_rectangle(x * 50, y * 50, x * 50 + 50, y * 50 + 50, fill="black")
        else:
            canvas.delete(canvas_objects[x][y])
            canvas_objects[y, x] = 0
            canvas_objects[y, x] = canvas.create_rectangle(x * 50, y * 50, x * 50 + 50, y * 50 + 50, fill="black")
        reward_table[y, x] = -10
    elif action == 2:
        print("Q-Value: " + str(q_table[y, x]))
    else:
        print("Object removed: " + str(y) + "," + str(x))
        canvas.delete(canvas_objects[y, x])
        canvas_objects[y, x] = 0
        reward_table[y, x] = -1

def reset():
    global agent_pos
    canvas.delete(canvas_objects[agent_pos[0], agent_pos[1]])
    canvas_objects[agent_pos[0], agent_pos[1]] = 0
    agent_pos = np.copy(initial_pos)
    canvas_objects[agent_pos[0], agent_pos[1]] = canvas.create_rectangle(agent_pos[1] * 50, agent_pos[0] * 50, agent_pos[1] * 50 + 50, agent_pos[0] * 50 + 50, fill="red")

def get_movement_availability():
    global agent_pos
    movement = np.array([False, False, False, False])
    try:
        if agent_pos[1] > 0 and reward_table[agent_pos[0], agent_pos[1] - 1] > -10:  # Check left
            movement[0] = True
        if agent_pos[1] < 9 and reward_table[agent_pos[0], agent_pos[1] + 1] > -10:  # Check right
            movement[1] = True
        if agent_pos[0] > 0 and reward_table[agent_pos[0] - 1, agent_pos[1]] > -10:  # Check up
            movement[2] = True
        if agent_pos[0] < 9 and reward_table[agent_pos[0] + 1, agent_pos[1]] > -10:  # Check down
            movement[3] = True
        return movement
    except Exception:
        print(Exception)

def move(direction):
    # Should return a new state and a reward
    global agent_pos
    x, y = 0, 0
    agent_ID = canvas_objects[agent_pos[0]][agent_pos[1]]
    previous_location = np.copy(agent_pos)
    agent_moved = True
    movements_available = get_movement_availability()

    if direction == 0 and movements_available[0]:         # Move Left
        x = -50
        agent_pos[1] -= 1
    elif direction == 1 and movements_available[1]:       # Move Right
        x = 50
        agent_pos[1] += 1
    elif direction == 2 and movements_available[2]:       # Move Up
        y = -50
        agent_pos[0] -= 1
    elif direction == 3 and movements_available[3]:       # Move Down
        y = 50
        agent_pos[0] += 1
    else:
        agent_moved = False

    if agent_moved:
        if reward_table[agent_pos[0], agent_pos[1]] == 100:
            #agent_pos = np.copy(previous_location)
            #reset()
            canvas.move(agent_ID, x, y)                                                       # FIXME These lines
            canvas_objects[previous_location[0]][previous_location[1]] = 0                    # FIXME should be
            canvas_objects[agent_pos[0]][agent_pos[1]] = agent_ID                             # FIXME DELETED
            return 100
        else:
            canvas.move(agent_ID, x, y)
            canvas_objects[previous_location[0]][previous_location[1]] = 0
            canvas_objects[agent_pos[0]][agent_pos[1]] = agent_ID
            return reward_table[agent_pos[0], agent_pos[1]]
    else:
        return -10

def train():
    btn_start.config(state="disabled")
    best_reward = 0
    success_times = 0
    b_rewards_text.set("Best score: " + str(best_reward))
    success_text.set("Success times: " + str(success_times))
    for i in range (1, EPISODES):
        episodes_text.set("Episode: " + str(i))
        max_reward = 0
        for j in range (200, 0, -1):
            tries_text.set("Tries left: " + str(j))

            current_state = tuple(np.copy(agent_pos))
            
            #########################################################################
            epsilon = 0.2
            action = 0
            if random.uniform(0, 1) < epsilon:
                action = random.randint(0, 3)
            else:
                action = np.argmax(q_table[agent_pos[0], agent_pos[1]])                 # Find the max value of this
            #########################################################################

            reward = move(action)                                                       # See reward from this step

            max_reward += reward
            rewards_text.set("Reward: " + str(max_reward))

            new_state = tuple(q_table[agent_pos[0], agent_pos[1]])       # See new state
            max_future_q = np.max(new_state)

            current_q    = q_table[current_state[0], current_state[1]][action]
            new_q = current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q - current_q)

            q_table[current_state[0]][current_state[1]][action] = new_q

            if reward == 100:
                success_times += 1
                success_text.set("Success times: " + str(success_times))
                reset()
                break
            if i == 1 or i % 50 == 0:
                canvas.update()
                time.sleep(.1)

            current_state = new_state
            label_epoch.update()
        
        if best_reward == 0:
            best_reward = max_reward
        elif best_reward < max_reward:
            best_reward = max_reward
        b_rewards_text.set("Best score: " + str(best_reward))

        reset()
    btn_start.config(state="normal")

def keypress(event):
    if   event.char == "a" or event.keycode == 37: move(0)
    elif event.char == "d" or event.keycode == 39: move(1)
    elif event.char == "w" or event.keycode == 38: move(2)
    elif event.char == "s" or event.keycode == 40: move(3)

# Bind Events
canvas.bind("<Button 1>", lambda event : drawOnCanvas(event, 1))  # Place object
canvas.bind("<Button 2>", lambda event : drawOnCanvas(event, 2))  # Place goal
canvas.bind("<Button 3>", lambda event : drawOnCanvas(event, 3))  # Delete object
window.bind("<Key>", keypress)

btn_start.configure(command=train)
btn_reset.configure(command=reset)
window.mainloop()