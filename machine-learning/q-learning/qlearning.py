import tkinter as tk
import tkinter.font as tkFont
from tkinter.filedialog import askopenfilename, asksaveasfile
import numpy as np
import time
import random
import sys

# GUI parameters
tile_size = 70                                          # Tile's size (in pixels)
best_reward   = 0                                       # Best reward found (Used for visualization)
success_times = 0                                       # Number of successful times (Used for visualization)
current_it = 1                                          # Current number of episodes

# Q-Learning parameters
LEARNING_RATE = 0.05                                    # How big or small step to make each iteration
DISCOUNT      = 0.95                                    # How much value future rewards over current rewards
EPISODES      = 250                                     # Maximum number of episodes to run
PENALTY       = -10                                     # Penalty for going off limits
epsilon       = 1                                       # Epsilon greedy strategy (Exploration percentage)

# Initialization of tables (10 x 10) and positions
initial_pos    = np.array([1, 0])                       # Initial position, used for starting position and resetting
agent_pos      = np.copy(initial_pos)                   # Agent starting position (columns, rows)
goal_pos       = np.array([8, 9])                       # Goal position
goal_ID        = -1                                     # Goal's object ID
q_table        = np.zeros((10, 10, 4))                  # Initialize Q-table state-space (states * available actions)
rewards        = np.ones((10, 10)) * - 1                # Initialize reward table to -1
canvas_objects = np.zeros((10, 10), dtype=int)          # Canvas objects table

# Save custom maze to a csv file
def saveMaze():
    global agent_pos, rewards, initial_pos
    maze_file = np.copy(rewards)
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
    global agent_pos, canvas_objects, rewards, initial_pos, goal_pos, goal_ID
    try:
        maze_file = np.genfromtxt(askopenfilename(initialdir='/q-learning/'), delimiter=',', dtype = np.int)
        canvas.delete("all")
        canvas_objects.fill(0)
        rewards.fill(-1)
        for i in range (0, maze_file.shape[0]):
            for j in range (0, maze_file.shape[1]):
                if maze_file[i, j] == 1:
                    rewards[i, j] = -10
                    canvas_objects[i, j] = canvas.create_rectangle(j * tile_size,
                                                                   i * tile_size,
                                                                   j * tile_size + tile_size,
                                                                   i * tile_size + tile_size,
                                                                   fill="black")
                elif maze_file[i, j] == 2:
                    initial_pos = [i, j]
                    agent_pos = np.copy(initial_pos)
                    canvas_objects[i, j] = canvas.create_oval(agent_pos[1] * tile_size,
                                                              agent_pos[0] * tile_size,
                                                              agent_pos[1] * tile_size + tile_size,
                                                              agent_pos[0] * tile_size + tile_size,
                                                              fill="red")
                elif maze_file[i, j] == 3:
                    goal_pos = [i, j]
                    rewards[goal_pos[0], goal_pos[1]] = 100
                    canvas_objects[goal_pos[0], goal_pos[1]] = canvas.create_rectangle(goal_pos[1] * tile_size,
                                                                                       goal_pos[0] * tile_size,
                                                                                       goal_pos[1] * tile_size + tile_size,
                                                                                       goal_pos[0] * tile_size + tile_size,
                                                                                       fill="green")
                    goal_ID = canvas_objects[goal_pos[0], goal_pos[1]]
                else:
                    pass
    except OSError:
        pass
    except:
        print("Error loading maze:", sys.exc_info()[0])


# Method to add or remove canvas objects
def drawOnCanvas(event, action):
    x = np.floor(event.x / tile_size).astype(int)      # Attention! This is mouse x coordinate but indicates columns in tables!
    y = np.floor(event.y / tile_size).astype(int)      # Attention! This is mouse y coordinate but indicates rows in tables!
    global goal_pos
    if action == 1:
        if canvas_objects[y, x] == canvas_objects[tuple(agent_pos)] or canvas_objects[y, x] == canvas_objects[tuple(goal_pos)]:
            print("You can't place block here.")
        else:
            if canvas_objects[y, x] == 0:
                canvas_objects[y, x] = canvas.create_rectangle(x * tile_size, y * tile_size, x * tile_size + tile_size, y * tile_size + tile_size, fill="black")
            else:
                canvas.delete(canvas_objects[y][x])
                canvas_objects[y, x] = 0
                canvas_objects[y, x] = canvas.create_rectangle(x * tile_size, y * tile_size, x * tile_size + tile_size, y * tile_size + tile_size, fill="black")
            rewards[y, x] = -10
    elif action == 2:
        print("Q-Value at (" + str(y) + ", " + str(x) + "): " + str(q_table[y, x]))
    else:
        if canvas_objects[y, x] == canvas_objects[tuple(agent_pos)] or canvas_objects[y, x] == canvas_objects[tuple(goal_pos)]:
            print("You can't delete this object.")
        else:
            canvas.delete(canvas_objects[y, x])
            canvas_objects[y, x] = 0
            rewards[y, x] = -1

# Reset application to initial values
def reset():
    global agent_pos, q_table, canvas_objects, rewards, initial_pos, goal_pos, epsilon, best_reward, success_times
    if epsilon_value.get() == 1:
        epsilon = 1
        exploration_text.set("Explore: 100%")
    best_reward = 0
    b_rewards_text.set("Best Reward: N/A")
    success_times = 0
    success_text.set("Success: N/A")
    canvas.delete("all")
    canvas_objects.fill(0)
    rewards.fill(-1)
    q_table.fill(0)
    agent_pos = np.copy(initial_pos)
    canvas_objects[agent_pos[0], agent_pos[1]] = canvas.create_oval(agent_pos[1] * tile_size,
                                                                    agent_pos[0] * tile_size,
                                                                    agent_pos[1] * tile_size + tile_size,
                                                                    agent_pos[0] * tile_size + tile_size,
                                                                    fill="red")
    rewards[goal_pos[0], goal_pos[1]] = 100
    canvas_objects[goal_pos[0], goal_pos[1]] = canvas.create_rectangle(goal_pos[1] * tile_size,
                                                                       goal_pos[0] * tile_size,
                                                                       goal_pos[1] * tile_size + tile_size,
                                                                       goal_pos[0] * tile_size + tile_size,
                                                                       fill="green")

# Reset agent to original position
def reset_agent():
    global agent_pos, canvas_objects, initial_pos, goal_ID
    canvas.delete(canvas_objects[agent_pos[0], agent_pos[1]])
    canvas_objects[agent_pos[0], agent_pos[1]] = 0
    agent_pos = np.copy(initial_pos)
    canvas_objects[agent_pos[0], agent_pos[1]] = canvas.create_oval(agent_pos[1] * tile_size,
                                                                    agent_pos[0] * tile_size,
                                                                    agent_pos[1] * tile_size + tile_size, 
                                                                    agent_pos[0] * tile_size + tile_size,
                                                                    fill="red")
    if canvas_objects[goal_pos[0], goal_pos[1]] == 0:
        canvas_objects[goal_pos[0], goal_pos[1]] = goal_ID

# Check every available option on a specific state
def is_valid_move(direction):
    global agent_pos
    if   direction == 0 and agent_pos[1] > 0 and rewards[agent_pos[0], agent_pos[1] - 1] != -10:   # Check left
        return True
    elif direction == 1 and agent_pos[1] < 9 and rewards[agent_pos[0], agent_pos[1] + 1] != -10:   # Check right
        return True
    elif direction == 2 and agent_pos[0] > 0 and rewards[agent_pos[0] - 1, agent_pos[1]] != -10:   # Check up
        return True
    elif direction == 3 and agent_pos[0] < 9 and rewards[agent_pos[0] + 1, agent_pos[1]] != -10:   # Check down
        return True
    else:
        return False

# Move agent to new state and return a reward for this action
def move(direction):
    global agent_pos
    x, y = 0, 0
    agent_ID = canvas_objects[agent_pos[0]][agent_pos[1]]
    previous_location = np.copy(agent_pos)

    if   direction == 0 and is_valid_move(0):       # Move Left
        x = -tile_size
        agent_pos[1] -= 1
    elif direction == 1 and is_valid_move(1):       # Move Right
        x = tile_size
        agent_pos[1] += 1
    elif direction == 2 and is_valid_move(2):       # Move Up
        y = -tile_size
        agent_pos[0] -= 1
    elif direction == 3 and is_valid_move(3):       # Move Down
        y = tile_size
        agent_pos[0] += 1
    else:
        return tuple(q_table[agent_pos[0], agent_pos[1]]), PENALTY

    canvas.move(agent_ID, x, y)
    canvas_objects[previous_location[0], previous_location[1]] = 0
    canvas_objects[agent_pos[0], agent_pos[1]] = agent_ID
    return tuple(q_table[agent_pos[0], agent_pos[1]]), rewards[agent_pos[0], agent_pos[1]]

def start():
    global epsilon, best_reward, success_times, current_it
    btn_start.config(state="disabled")
    btn_reset.config(state="disabled")
    btn_save.config(state="disabled")
    btn_load.config(state="disabled")

    for i in range (current_it, current_it + EPISODES):
        episodes_text.set("Episode: " + str(i))
        max_reward = 0

        # Reduce the greedy parameter
        if i > 1 and epsilon_value.get() == 1 and epsilon > 0.01:
            epsilon *= 97/100
            exploration_text.set("Explore: " + str(round(100 * epsilon, 2)) + "%")
        if i == 1 and epsilon_value.get() == 1:
            exploration_text.set("Explore: " + str(round(100 * epsilon, 2)) + "%")

        for j in range (200, 0, -1):
            tries_text.set("Moves left: " + str(j))
            current_state = tuple(np.copy(agent_pos))

            # If random number is less than ε then explore else exploit (make agent greedy)
            if epsilon_value.get() == 1 and random.uniform(0, 1) < epsilon:
                action = random.randint(0, 3)
            else:
                action = np.argmax(q_table[agent_pos[0], agent_pos[1]])
            new_state, reward = move(action)
            max_reward += reward
            rewards_text.set("Reward: " + str(max_reward))
            max_future_q = np.max(new_state)
            current_q    = q_table[current_state[0], current_state[1]][action]
            new_q = current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q - current_q)
            q_table[current_state[0]][current_state[1]][action] = new_q

            if reward == rewards[goal_pos[0], goal_pos[1]]:
                success_times += 1
                break

            if ff_value.get() == 1:
                if i == 1 or i % 50 == 0:
                    canvas.update()
                    time.sleep(.1)
            else:
                canvas.update()
                time.sleep(.1)

            current_state = new_state
            label_epoch.update()
        
        if i == 1 or best_reward < max_reward:
            best_reward = max_reward
        b_rewards_text.set("Best reward: " + str(best_reward))
        success_text.set("Success: " + str(round((100 * success_times / i), 2)) + "%")
        canvas.update()
        reset_agent()

    current_it += EPISODES
    btn_start.config(state="normal")
    btn_reset.config(state="normal")
    btn_save.config(state="normal")
    btn_load.config(state="normal")

# Set agent position
def setInputs(option):
    global initial_pos, agent_pos, canvas_objects, goal_pos, rewards
    try:
        if option == 0:
            agent_row = int(agent_row_input.get())
            agent_col = int(agent_col_input.get())
            if canvas_objects[agent_row, agent_col] != canvas_objects[goal_pos[0], goal_pos[1]]:
                canvas.delete(canvas_objects[agent_pos[0], agent_pos[1]])
                canvas.delete(canvas_objects[agent_row, agent_col])
                canvas_objects[agent_pos[0], agent_pos[1]] = 0
                canvas_objects[agent_row, agent_col] = 0
                initial_pos = [agent_row, agent_col]
                agent_pos = np.copy(initial_pos)
                canvas_objects[agent_row, agent_col] = canvas.create_oval(agent_pos[1] * tile_size,
                                                                          agent_pos[0] * tile_size,
                                                                          agent_pos[1] * tile_size + tile_size,
                                                                          agent_pos[0] * tile_size + tile_size,
                                                                          fill="red")
                agent_label['text'] = "Agent's Position: (" + str(agent_pos[0]) + "," + str(agent_pos[1]) + ")"
            else:
                print("You can't place agent on top of the goal position!")
        else:
            goal_row = int(goal_row_input.get())
            goal_col = int(goal_col_input.get())
            if canvas_objects[goal_row, goal_col] != canvas_objects[tuple(agent_pos)]:
                canvas.delete(canvas_objects[goal_pos[0], goal_pos[1]])
                canvas.delete(canvas_objects[goal_row, goal_col])
                rewards[goal_pos[0], goal_pos[1]] = -1
                goal_pos = [goal_row, goal_col]
                rewards[goal_pos[0], goal_pos[1]] = 100
                canvas_objects[goal_pos[0], goal_pos[1]] = canvas.create_rectangle(goal_pos[1] * tile_size,
                                                                                   goal_pos[0] * tile_size,
                                                                                   goal_pos[1] * tile_size + tile_size,
                                                                                   goal_pos[0] * tile_size + tile_size,
                                                                                   fill="green")
                goal_label['text'] = "Goals's Position: (" + str(goal_pos[0]) + "," + str(goal_pos[1]) + ")"
            else:
                print("You can't place goal on top of the agent position!")
    except Exception:
        print("Please make sure you filled both row and column number and that it is a single number (0-9)")
        pass

# Enable-Disable Epsilon-greedy Parameter
def toggle_epsilon():
    if (epsilon_value.get() == 1):
        exploration_text.set("Explore: 100%")
    else:
        exploration_text.set("Explore: N/A")

# User Interface Parameters
window = tk.Tk()
window.title("Reinforcement Learning - Maze Solving Agent")
window.rowconfigure(0, minsize=500, weight=1)
window.columnconfigure(0, minsize=300, weight=1)
window.columnconfigure(2, minsize=300, weight=1)
mainFontStyle = tkFont.Font(family="Lucida Grande", size=20)
secondaryFontStyle = tkFont.Font(family="Lucida Grande", size=16)

# Main Menu
main_menu = tk.Frame(window)
main_menu.grid(row=0, column=0, sticky="ns")
main_menu.rowconfigure(0, minsize=150, weight=1)
inputs = tk.Frame(main_menu)
inputs.grid(row=0, column=0, sticky="w")

# Agent position inputs
agent_frame = tk.Frame(inputs)
agent_frame.grid(row=0, column=0, sticky="w", pady = 15)

agent_label = tk.Label(agent_frame, text="Agent's Position: (" + str(agent_pos[0]) + "," + str(agent_pos[1]) + ")", font=mainFontStyle)
agent_label.grid(row=0, column=0, sticky="w")

agent_params = tk.Frame(agent_frame)
agent_params.grid(row=1, column=0, sticky="w")

agent_row = tk.Label(agent_params, text="Row:", font=secondaryFontStyle)
agent_row.grid(row=0, column=0, sticky="w")
agent_row_input = tk.Entry(agent_params, width=2)
agent_row_input.grid(row=0, column=1, sticky="ew")

agent_col = tk.Label(agent_params, text=" - Col:", font=secondaryFontStyle)
agent_col.grid(row=0, column=2, sticky="w")

agent_col_input = tk.Entry(agent_params, width=2)
agent_col_input.grid(row=0, column=3, sticky="ew")
btn_agent = tk.Button(agent_params, text="Set", command=lambda: setInputs(0))
btn_agent.grid(row=0, column=4, sticky="ew", padx=5)

# Goal position inputs
goal_frame = tk.Frame(inputs)
goal_frame.grid(row=1, column=0, sticky="w", pady = 15)

goal_label = tk.Label(goal_frame, text="Goal's Position: (" + str(goal_pos[0]) + "," + str(goal_pos[1]) + ")", font=mainFontStyle)
goal_label.grid(row=0, column=0, sticky="w")

goal_params = tk.Frame(goal_frame)
goal_params.grid(row=1, column=0, sticky="w")

goal_row = tk.Label(goal_params, text="Row:", font=secondaryFontStyle)
goal_row.grid(row=0, column=0, sticky="w")
goal_row_input = tk.Entry(goal_params, width=2)
goal_row_input.grid(row=0, column=1, sticky="ew")

goal_col = tk.Label(goal_params, text=" - Col:", font=secondaryFontStyle)
goal_col.grid(row=0, column=2, sticky="w")

goal_col_input = tk.Entry(goal_params, width=2)
goal_col_input.grid(row=0, column=3, sticky="ew")
btn_goal = tk.Button(goal_params, text="Set", command=lambda: setInputs(1))
btn_goal.grid(row=0, column=4, sticky="ew", padx=5)

# Epsilon Checkbox Area
epsilon_param = tk.Frame(inputs)
epsilon_param.grid(row=2, column=0, sticky="w")

epsilon_value = tk.IntVar(value=1)
greedy_cb = tk.Checkbutton(epsilon_param, pady=15, text='ε-greedy strategy', font=mainFontStyle,
                           variable=epsilon_value, onvalue=1, offvalue=0, command=lambda: toggle_epsilon())
greedy_cb.grid(row=0, column=0)

# Fast-Forward Checkbox Area
ff_param = tk.Frame(inputs)
ff_param.grid(row=3, column=0, sticky="w")

ff_value = tk.IntVar(value=1)
ff_cb = tk.Checkbutton(ff_param, pady=15, text='Fast-Forward', font=mainFontStyle, variable=ff_value, onvalue=1, offvalue=0)
ff_cb.grid(row=0, column=0)

# Left Panel Parameters
btn_menu = tk.Frame(main_menu, bg='grey')
btn_menu.grid(row=1, column=0, sticky="s", pady=10)

btn_start = tk.Button(btn_menu, width=18, height=1, command=start, text="Start", font=secondaryFontStyle)
btn_reset = tk.Button(btn_menu, width=18, height=1, command=reset, text="Reset", font=secondaryFontStyle)
btn_save  = tk.Button(btn_menu, width=18, height=1, command=saveMaze, text="Save Custom Maze", font=secondaryFontStyle)
btn_load  = tk.Button(btn_menu, width=18, height=1, command=loadMaze, text="Load Custom Maze", font=secondaryFontStyle)
btn_exit  = tk.Button(btn_menu, width=18, height=1, command=window.destroy, text="Exit", font=secondaryFontStyle)

btn_start.grid(row=0, column=0, sticky="ns", padx=10, pady=10)
btn_reset.grid(row=1, column=0, sticky="ns", padx=10, pady=10)
btn_save.grid(row=2, column=0, sticky="ns", padx=10, pady=10)
btn_load.grid(row=3, column=0, sticky="ns", padx=10, pady=10)
btn_exit.grid(row=4, column=0, sticky="ns", padx=10, pady=10)

# Canvas Panel Parameters
canvas = tk.Canvas(master = window, width = tile_size * 10, height = tile_size * 10, bg="grey")
canvas.grid(row=0, column=1, sticky="nsew")

# Bind Events
canvas.bind("<Button 1>", lambda event : drawOnCanvas(event, 1))  # Place canvas object
canvas.bind("<Button 2>", lambda event : drawOnCanvas(event, 2))  # Show Q-Table's value
canvas.bind("<Button 3>", lambda event : drawOnCanvas(event, 3))  # Delete canvas object

info_menu = tk.Frame(window)
info_menu.grid(row=0, column=2, sticky="ew", padx=20)

episodes_text    = tk.StringVar()
tries_text       = tk.StringVar()
rewards_text     = tk.StringVar()
b_rewards_text   = tk.StringVar()
success_text     = tk.StringVar()
exploration_text = tk.StringVar()

episodes_text.set("Episode: 1")
tries_text.set("Moves left: 200")
rewards_text.set("Reward: N/A")
b_rewards_text.set("Best Reward: N/A")
success_text.set("Success: N/A")
exploration_text.set("Explore: 100%")

label_epoch       = tk.Label(info_menu, textvariable=episodes_text, font=mainFontStyle)
label_tries       = tk.Label(info_menu, textvariable=tries_text, font=mainFontStyle)
label_reward      = tk.Label(info_menu, textvariable=rewards_text, font=mainFontStyle)
label_b_reward    = tk.Label(info_menu, textvariable=b_rewards_text, font=mainFontStyle)
label_success     = tk.Label(info_menu, textvariable=success_text, font=mainFontStyle)
label_exploration = tk.Label(info_menu, textvariable=exploration_text, font=mainFontStyle)

label_epoch.grid(row=0, column=0, sticky="w", pady=10)
label_tries.grid(row=1, column=0, sticky="w", pady=10)
label_reward.grid(row=2, column=0, sticky="w", pady=10)
label_b_reward.grid(row=3, column=0, sticky="w", pady=10)
label_success.grid(row=4, column=0, sticky="w", pady=10)
label_exploration.grid(row=5, column=0, sticky="w", pady=10)

# Initialization of starting state parameters
canvas_objects[agent_pos[0], agent_pos[1]] = canvas.create_oval(agent_pos[1] * tile_size,
                                                                agent_pos[0] * tile_size,
                                                                agent_pos[1] * tile_size + tile_size,
                                                                agent_pos[0] * tile_size + tile_size,
                                                                fill="red")
canvas_objects[goal_pos[0], goal_pos[1]] = canvas.create_rectangle(goal_pos[1] * tile_size,
                                                                     goal_pos[0] * tile_size,
                                                                     goal_pos[1] * tile_size + tile_size,
                                                                     goal_pos[0] * tile_size + tile_size,
                                                                     fill="green")
rewards[goal_pos[0], goal_pos[1]] = 100

window.mainloop()
