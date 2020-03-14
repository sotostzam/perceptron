import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfile
import numpy as np
import time
import random
import sys

# Q-Learning parameters
LEARNING_RATE = 0.05                                    # How big or small step to make each iteration
DISCOUNT      = 0.95                                    # How much value future rewards over current rewards
EPISODES      = 500                                     # Maximum number of episodes to run
epsilon       = 1                                       # Epsilon greedy strategy (Exploration percentage)

# Initialization of tables (10 x 10) and positions
initial_pos    = np.array([1, 0])                       # Initial position, used for starting position and resetting
agent_pos      = np.copy(initial_pos)                   # Agent starting position (columns, rows)
goal_pos       = np.array([8, 9])                       # Goal position
q_table        = np.zeros((10, 10, 4))                  # Initialize Q-table state-space (states * available actions)
reward_table   = np.ones((10, 10)) * - 1                # Initialize reward table to -1
canvas_objects = np.zeros((10, 10), dtype=int)          # Canvas objects table

# Save custom maze to a csv file
def saveMaze():
    global agent_pos, reward_table, initial_pos
    maze_file = np.copy(reward_table)
    for i in range (0, maze_file.shape[0]):
        for j in range (0, maze_file.shape[1]):
            if maze_file[i, j] == -10:
                maze_file[i, j] = 1
            elif maze_file[i, j] == 100:
                maze_file[i, j] = 3
            elif maze_file[i, j] == -1:
                maze_file[i, j] = 0
            else:
                pass
    maze_file[agent_pos[0], agent_pos[1]] = 2
    try:
        np.savetxt("./q-learning/maze.csv", maze_file.astype(int), fmt='%i', delimiter=",")
        print('Successfully saved maze')
    except:
        print("Error saving maze:", sys.exc_info()[0])

# Load custom maze from csv file
def loadMaze():
    global agent_pos, canvas_objects, reward_table, initial_pos
    canvas.delete("all")
    canvas_objects.fill(0)
    reward_table.fill(-1)
    try:
        maze_file = np.genfromtxt(askopenfilename(initialdir='/q-learning/'), delimiter=',', dtype = np.int)
    except:
        print("Error loading maze:", sys.exc_info()[0])
    for i in range (0, maze_file.shape[0]):
        for j in range (0, maze_file.shape[1]):
            if maze_file[i, j] == 1:
                reward_table[i, j] = -10
                canvas_objects[i, j] = canvas.create_rectangle(j * 50, i * 50, j * 50 + 50, i * 50 + 50, fill="black")
            elif maze_file[i, j] == 2:
                initial_pos = [i, j]
                agent_pos = np.copy(initial_pos)
                canvas_objects[i, j] = canvas.create_oval(agent_pos[1] * 50, agent_pos[0] * 50, agent_pos[1] * 50 + 50, agent_pos[0] * 50 + 50, fill="red")
            elif maze_file[i, j] == 3:
                goal_pos = [i, j]
                reward_table[goal_pos[0], goal_pos[1]] = 100
                canvas_objects[goal_pos[0], goal_pos[1]] = canvas.create_rectangle(goal_pos[1] * 50, goal_pos[0] * 50, goal_pos[1] * 50 + 50, goal_pos[0] * 50 + 50, fill="green")
            else:
                pass

# Method to add or remove canvas objects
def drawOnCanvas(event, action):
    x = np.floor(event.x / 50).astype(int)      # Attention! This is mouse x coordinate but indicates columns in tables!
    y = np.floor(event.y / 50).astype(int)      # Attention! This is mouse y coordinate but indicates rows in tables!
    global goal_pos
    if action == 1:
        if canvas_objects[y, x] == 0:
            canvas_objects[y, x] = canvas.create_rectangle(x * 50, y * 50, x * 50 + 50, y * 50 + 50, fill="black")
        else:
            canvas.delete(canvas_objects[y][x])
            canvas_objects[y, x] = 0
            canvas_objects[y, x] = canvas.create_rectangle(x * 50, y * 50, x * 50 + 50, y * 50 + 50, fill="black")
        reward_table[y, x] = -10
    elif action == 2:
        print("Q-Value: " + str(q_table[y, x]))
    else:
        canvas.delete(canvas_objects[y, x])
        canvas_objects[y, x] = 0
        reward_table[y, x] = -1

# Reset agent to original position
def reset():
    global agent_pos, canvas_objects, initial_pos
    canvas.delete(canvas_objects[agent_pos[0], agent_pos[1]])
    canvas_objects[agent_pos[0], agent_pos[1]] = 0
    agent_pos = np.copy(initial_pos)
    canvas_objects[agent_pos[0], agent_pos[1]] = canvas.create_oval(agent_pos[1] * 50, agent_pos[0] * 50, agent_pos[1] * 50 + 50, agent_pos[0] * 50 + 50, fill="red")

# Check every available option on a specific state
def get_movement_availability():
    global agent_pos
    movement = np.array([False, False, False, False])
    if agent_pos[1] > 0 and reward_table[agent_pos[0], agent_pos[1] - 1] > -10:  # Check left
        movement[0] = True
    if agent_pos[1] < 9 and reward_table[agent_pos[0], agent_pos[1] + 1] > -10:  # Check right
        movement[1] = True
    if agent_pos[0] > 0 and reward_table[agent_pos[0] - 1, agent_pos[1]] > -10:  # Check up
        movement[2] = True
    if agent_pos[0] < 9 and reward_table[agent_pos[0] + 1, agent_pos[1]] > -10:  # Check down
        movement[3] = True
    return movement

# Move agent to new state and return a reward for this action
def move(direction):
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
            canvas_objects[previous_location[0], previous_location[1]] = 0                    # FIXME should be
            canvas_objects[agent_pos[0], agent_pos[1]] = agent_ID                             # FIXME DELETED
            return 100
        else:
            canvas.move(agent_ID, x, y)
            canvas_objects[previous_location[0], previous_location[1]] = 0
            canvas_objects[agent_pos[0], agent_pos[1]] = agent_ID
            return reward_table[agent_pos[0], agent_pos[1]]
    else:
        return -10

def start():
    global epsilon
    btn_start.config(state="disabled")
    best_reward = 0
    success_times = 0
    b_rewards_text.set("Best score: " + str(best_reward))
    success_text.set("Success: " + str(success_times) + "%")
    exploration_text.set("Exploration rate: " + str(100 * epsilon) + "%")

    for i in range (1, EPISODES + 1):
        episodes_text.set("Episode: " + str(i))
        max_reward = 0

        # Reduce the greedy parameter
        if epsilon > 0.01 and i > 1:
            epsilon *= 97/100
            exploration_text.set("Exploration rate: " + str(round(100 * epsilon, 2)) + "%")

        for j in range (200, 0, -1):
            tries_text.set("Tries left: " + str(j))
            current_state = tuple(np.copy(agent_pos))

            # If random number is less than ε then explore else exploit (make agent greedy)
            if random.uniform(0, 1) < epsilon:
                action = random.randint(0, 3)
            else:
                action = np.argmax(q_table[agent_pos[0], agent_pos[1]])
            reward = move(action)
            max_reward += reward
            rewards_text.set("Reward: " + str(max_reward))
            new_state = tuple(q_table[agent_pos[0], agent_pos[1]])       # See new state
            max_future_q = np.max(new_state)
            current_q    = q_table[current_state[0], current_state[1]][action]
            new_q = current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q - current_q)
            q_table[current_state[0]][current_state[1]][action] = new_q

            if reward == 100:
                success_times += 1
                success_text.set("Success: " + str(round((100 * success_times / i), 2)) + "%")
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

# User Interface Parameters
window = tk.Tk()
window.title("Reinforcement Learning")
window.rowconfigure(0, minsize=500, weight=1)
window.columnconfigure(1, minsize=100, weight=1)

# Left Panel Parameters
main_menu = tk.Frame(window)
main_menu.grid(row=0, column=0, sticky="ns")

btn_start = tk.Button(main_menu, text="Start", width=20, height=2)
btn_reset = tk.Button(main_menu, text="Reset", width=20, height=2)
btn_save = tk.Button(main_menu, text="Save Custom Maze", width=20, height=2)
btn_load = tk.Button(main_menu, text="Load Custom Maze", width=20, height=2)
btn_exit  = tk.Button(main_menu, text="Exit",  width=20, height=2, command=window.destroy)

btn_start.grid(row=0, column=0, sticky="ew", padx=5, pady=10)
btn_reset.grid(row=1, column=0, sticky="ew", padx=5, pady=10)
btn_save.grid(row=2, column=0, sticky="ew", padx=5, pady=10)
btn_load.grid(row=3, column=0, sticky="ew", padx=5, pady=10)
btn_exit.grid(row=4, column=0, sticky="ew", padx=5, pady=10)

info_menu = tk.Frame(window)
info_menu.grid(row=0, column=2, sticky="ns")

episodes_text    = tk.StringVar()
tries_text       = tk.StringVar()
rewards_text     = tk.StringVar()
b_rewards_text   = tk.StringVar()
success_text     = tk.StringVar()
exploration_text = tk.StringVar()

episodes_text.set("Episode: N/A")
tries_text.set("Tries left: N/A")
rewards_text.set("Reward: N/A")
b_rewards_text.set("Best Score: N/A")
success_text.set("Success: N/A")
exploration_text.set("Exploration rate: N/A")

label_epoch       = tk.Label(info_menu, width=20, textvariable=episodes_text)
label_tries       = tk.Label(info_menu, width=20, textvariable=tries_text)
label_reward      = tk.Label(info_menu, width=20, textvariable=rewards_text)
label_b_reward    = tk.Label(info_menu, width=20, textvariable=b_rewards_text)
label_success     = tk.Label(info_menu, width=20, textvariable=success_text)
label_exploration = tk.Label(info_menu, width=20, textvariable=exploration_text)

label_epoch.grid(row=0, column=0, sticky="ew", padx=5, pady=10)
label_tries.grid(row=1, column=0, sticky="ew", padx=5, pady=10)
label_reward.grid(row=2, column=0, sticky="ew", padx=5, pady=10)
label_b_reward.grid(row=3, column=0, sticky="ew", padx=5, pady=10)
label_success.grid(row=4, column=0, sticky="ew", padx=5, pady=10)
label_exploration.grid(row=5, column=0, sticky="ew", padx=5, pady=10)

# Canvas Panel Parameters
canvas = tk.Canvas(master = window, width = 500, height = 500, bg="grey")
canvas.grid(row=0, column=1, sticky="nsew")

# Bind Events
canvas.bind("<Button 1>", lambda event : drawOnCanvas(event, 1))  # Place canvas object
canvas.bind("<Button 2>", lambda event : drawOnCanvas(event, 2))  # Show Q-Table's value
canvas.bind("<Button 3>", lambda event : drawOnCanvas(event, 3))  # Delete canvas object

# Initialization of starting state parameters
canvas_objects[agent_pos[0], agent_pos[1]] = canvas.create_oval(agent_pos[1] * 50, agent_pos[0] * 50, agent_pos[1] * 50 + 50, agent_pos[0] * 50 + 50, fill="red")
canvas_objects[goal_pos[0], goal_pos[1]]   = canvas.create_rectangle(goal_pos[1] * 50, goal_pos[0] * 50, goal_pos[1] * 50 + 50, goal_pos[0] * 50 + 50, fill="green")
reward_table[goal_pos[0], goal_pos[1]]     = 100

btn_start.configure(command=start)
btn_reset.configure(command=reset)
btn_save.configure(command=saveMaze)
btn_load.configure(command=loadMaze)
window.mainloop()
