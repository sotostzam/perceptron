import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfile
import numpy as np
import time
import random
import sys

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
    global agent_pos, canvas_objects, rewards, initial_pos, goal_pos
    try:
        maze_file = np.genfromtxt(askopenfilename(initialdir='/q-learning/'), delimiter=',', dtype = np.int)
        canvas.delete("all")
        canvas_objects.fill(0)
        rewards.fill(-1)
        for i in range (0, maze_file.shape[0]):
            for j in range (0, maze_file.shape[1]):
                if maze_file[i, j] == 1:
                    rewards[i, j] = -10
                    canvas_objects[i, j] = canvas.create_rectangle(j * 50, i * 50, j * 50 + 50, i * 50 + 50, fill="black")
                elif maze_file[i, j] == 2:
                    initial_pos = [i, j]
                    agent_pos = np.copy(initial_pos)
                    canvas_objects[i, j] = canvas.create_oval(agent_pos[1] * 50, agent_pos[0] * 50, agent_pos[1] * 50 + 50, agent_pos[0] * 50 + 50, fill="red")
                elif maze_file[i, j] == 3:
                    goal_pos = [i, j]
                    rewards[goal_pos[0], goal_pos[1]] = 100
                    canvas_objects[goal_pos[0], goal_pos[1]] = canvas.create_rectangle(goal_pos[1] * 50, goal_pos[0] * 50, goal_pos[1] * 50 + 50, goal_pos[0] * 50 + 50, fill="green")
                else:
                    pass
    except OSError:
        pass
    except:
        print("Error loading maze:", sys.exc_info()[0])


# Method to add or remove canvas objects
def drawOnCanvas(event, action):
    x = np.floor(event.x / 50).astype(int)      # Attention! This is mouse x coordinate but indicates columns in tables!
    y = np.floor(event.y / 50).astype(int)      # Attention! This is mouse y coordinate but indicates rows in tables!
    global goal_pos
    if action == 1:
        if canvas_objects[y, x] == 0:
            canvas_objects[y, x] = canvas.create_rectangle(x * 50, y * 50, x * 50 + 50, y * 50 + 50, fill="black")
        elif canvas_objects[y, x] == canvas_objects[tuple(agent_pos)] or canvas_objects[y, x] == canvas_objects[tuple(goal_pos)]:
            print("You can't place block here.")
        else:
            canvas.delete(canvas_objects[y][x])
            canvas_objects[y, x] = 0
            canvas_objects[y, x] = canvas.create_rectangle(x * 50, y * 50, x * 50 + 50, y * 50 + 50, fill="black")
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
    global agent_pos, canvas_objects, rewards, initial_pos, goal_pos
    canvas.delete("all")
    canvas_objects.fill(0)
    rewards.fill(-1)
    agent_pos = np.copy(initial_pos)
    canvas_objects[agent_pos[0], agent_pos[1]] = canvas.create_oval(agent_pos[1] * 50, agent_pos[0] * 50, agent_pos[1] * 50 + 50, agent_pos[0] * 50 + 50, fill="red")
    rewards[goal_pos[0], goal_pos[1]] = 100
    canvas_objects[goal_pos[0], goal_pos[1]] = canvas.create_rectangle(goal_pos[1] * 50, goal_pos[0] * 50, goal_pos[1] * 50 + 50, goal_pos[0] * 50 + 50, fill="green")

# Reset agent to original position
def reset_agent():
    global agent_pos, canvas_objects, initial_pos
    canvas.delete(canvas_objects[agent_pos[0], agent_pos[1]])
    canvas_objects[agent_pos[0], agent_pos[1]] = 0
    agent_pos = np.copy(initial_pos)
    canvas_objects[agent_pos[0], agent_pos[1]] = canvas.create_oval(agent_pos[1] * 50, agent_pos[0] * 50, agent_pos[1] * 50 + 50, agent_pos[0] * 50 + 50, fill="red")

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
        x = -50
        agent_pos[1] -= 1
    elif direction == 1 and is_valid_move(1):       # Move Right
        x = 50
        agent_pos[1] += 1
    elif direction == 2 and is_valid_move(2):       # Move Up
        y = -50
        agent_pos[0] -= 1
    elif direction == 3 and is_valid_move(3):       # Move Down
        y = 50
        agent_pos[0] += 1
    else:
        return tuple(q_table[agent_pos[0], agent_pos[1]]), PENALTY

    canvas.move(agent_ID, x, y)
    canvas_objects[previous_location[0], previous_location[1]] = 0
    canvas_objects[agent_pos[0], agent_pos[1]] = agent_ID
    return tuple(q_table[agent_pos[0], agent_pos[1]]), rewards[agent_pos[0], agent_pos[1]]

def start():
    global epsilon
    btn_start.config(state="disabled")
    btn_reset.config(state="disabled")
    btn_save.config(state="disabled")
    btn_load.config(state="disabled")
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
            new_state, reward = move(action)
            max_reward += reward
            rewards_text.set("Reward: " + str(max_reward))
            max_future_q = np.max(new_state)
            current_q    = q_table[current_state[0], current_state[1]][action]
            new_q = current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q - current_q)
            q_table[current_state[0]][current_state[1]][action] = new_q

            if reward == rewards[goal_pos[0], goal_pos[1]]:
                success_times += 1
                success_text.set("Success: " + str(round((100 * success_times / i), 2)) + "%")
                reset_agent()
                break
            if i == 1 or i % 50 == 0:
                canvas.update()
                time.sleep(.1)

            current_state = new_state
            label_epoch.update()
        
        if i == 1 or best_reward < max_reward:
            best_reward = max_reward
        b_rewards_text.set("Best score: " + str(best_reward))

        reset_agent()
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
                canvas_objects[agent_row, agent_col] = canvas.create_oval(agent_pos[1] * 50, agent_pos[0] * 50, agent_pos[1] * 50 + 50, agent_pos[0] * 50 + 50, fill="red")
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
                canvas_objects[goal_pos[0], goal_pos[1]] = canvas.create_rectangle(goal_pos[1] * 50, goal_pos[0] * 50, goal_pos[1] * 50 + 50, goal_pos[0] * 50 + 50, fill="green")
            else:
                print("You can't place goal on top of the agent position!")
    except Exception:
        print("Please make sure you filled both row and column number and that it is a single number (0-9)")
        pass
    

# User Interface Parameters
window = tk.Tk()
window.title("Reinforcement Learning")
window.rowconfigure(0, minsize=500, weight=1)
window.columnconfigure(0, minsize=150, weight=1)
window.columnconfigure(2, minsize=150, weight=1)

# Main Menu
main_menu = tk.Frame(window)
main_menu.grid(row=0, column=0, sticky="ns")
main_menu.rowconfigure(0, minsize=150, weight=1)
inputs = tk.Frame(main_menu)
inputs.grid(row=0, column=0, sticky="n", pady=5)

# Agent position inputs
agent_label = tk.Label(inputs, text="Agent Position:")
agent_label.grid(row=0, column=0, sticky="w")

agent_params = tk.Frame(inputs)
agent_params.grid(row=1, column=0, sticky="nwe")

agent_row = tk.Label(agent_params, text="Row:")
agent_row.grid(row=0, column=0, sticky="w")
agent_row_input = tk.Entry(agent_params, width=2)
agent_row_input.grid(row=0, column=1, sticky="ew")

agent_col = tk.Label(agent_params, text="Col:")
agent_col.grid(row=0, column=2, sticky="w")

agent_col_input = tk.Entry(agent_params, width=2)
agent_col_input.grid(row=0, column=3, sticky="ew")
btn_agent = tk.Button(agent_params, text="Set", command=lambda: setInputs(0))
btn_agent.grid(row=0, column=4, sticky="ew", padx=5)

# Goal position inputs
goal_label = tk.Label(inputs, text="Goal Position:")
goal_label.grid(row=2, column=0, sticky="w")

goal_params = tk.Frame(inputs)
goal_params.grid(row=3, column=0, sticky="n")

goal_row = tk.Label(goal_params, text="Row:")
goal_row.grid(row=0, column=0, sticky="w")
goal_row_input = tk.Entry(goal_params, width=2)
goal_row_input.grid(row=0, column=1, sticky="ew")

goal_col = tk.Label(goal_params, text="Col:")
goal_col.grid(row=0, column=2, sticky="w")

goal_col_input = tk.Entry(goal_params, width=2)
goal_col_input.grid(row=0, column=3, sticky="ew")
btn_goal = tk.Button(goal_params, text="Set", command=lambda: setInputs(1))
btn_goal.grid(row=0, column=4, sticky="ew", padx=5)

# Left Panel Parameters
btn_menu = tk.Frame(main_menu)
btn_menu.grid(row=1, column=0, sticky="s")

btn_start = tk.Button(btn_menu, width=20, height=2, command=start, text="Start")
btn_reset = tk.Button(btn_menu, width=20, height=2, command=reset, text="Reset")
btn_save  = tk.Button(btn_menu, width=20, height=2, command=saveMaze, text="Save Custom Maze")
btn_load  = tk.Button(btn_menu, width=20, height=2, command=loadMaze, text="Load Custom Maze")
btn_exit  = tk.Button(btn_menu, width=20, height=2, command=window.destroy, text="Exit")

btn_start.grid(row=0, column=0, sticky="ew", padx=5, pady=10)
btn_reset.grid(row=1, column=0, sticky="ew", padx=5, pady=10)
btn_save.grid(row=2, column=0, sticky="ew", padx=5, pady=10)
btn_load.grid(row=3, column=0, sticky="ew", padx=5, pady=10)
btn_exit.grid(row=4, column=0, sticky="ew", padx=5, pady=10)

# Canvas Panel Parameters
canvas = tk.Canvas(master = window, width = 500, height = 500, bg="grey")
canvas.grid(row=0, column=1, sticky="nsew")

# Bind Events
canvas.bind("<Button 1>", lambda event : drawOnCanvas(event, 1))  # Place canvas object
canvas.bind("<Button 2>", lambda event : drawOnCanvas(event, 2))  # Show Q-Table's value
canvas.bind("<Button 3>", lambda event : drawOnCanvas(event, 3))  # Delete canvas object

info_menu = tk.Frame(window)
info_menu.grid(row=0, column=2, sticky="ns", padx=3)

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

label_epoch       = tk.Label(info_menu, textvariable=episodes_text)
label_tries       = tk.Label(info_menu, textvariable=tries_text)
label_reward      = tk.Label(info_menu, textvariable=rewards_text)
label_b_reward    = tk.Label(info_menu, textvariable=b_rewards_text)
label_success     = tk.Label(info_menu, textvariable=success_text)
label_exploration = tk.Label(info_menu, textvariable=exploration_text)

label_epoch.grid(row=0, column=0, sticky="w", pady=10)
label_tries.grid(row=1, column=0, sticky="w", pady=10)
label_reward.grid(row=2, column=0, sticky="w", pady=10)
label_b_reward.grid(row=3, column=0, sticky="w", pady=10)
label_success.grid(row=4, column=0, sticky="w", pady=10)
label_exploration.grid(row=5, column=0, sticky="w", pady=10)

# Initialization of starting state parameters
canvas_objects[agent_pos[0], agent_pos[1]] = canvas.create_oval(agent_pos[1] * 50, agent_pos[0] * 50, agent_pos[1] * 50 + 50, agent_pos[0] * 50 + 50, fill="red")
canvas_objects[goal_pos[0], goal_pos[1]]   = canvas.create_rectangle(goal_pos[1] * 50, goal_pos[0] * 50, goal_pos[1] * 50 + 50, goal_pos[0] * 50 + 50, fill="green")
rewards[goal_pos[0], goal_pos[1]]     = 100

window.mainloop()
