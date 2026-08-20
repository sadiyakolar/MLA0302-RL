#Implement Q-learning to develop an AI agent that plays a simple grid-based game (e.g., a
basic version of Pac-Man). The agent should learn to collect rewards (e.g., food) and avoid
penalties (e.g., ghosts). Write a Python program to train and evaluate the AI agent

import numpy as np
import random

rows = int(input("Enter Number of Rows: "))
cols = int(input("Enter Number of Columns: "))

food_row = int(input("Enter Food Row: "))
food_col = int(input("Enter Food Column: "))

ghost_row = int(input("Enter Ghost Row: "))
ghost_col = int(input("Enter Ghost Column: "))

alpha = float(input("Enter Learning Rate: "))
gamma = float(input("Enter Discount Factor: "))
epsilon = float(input("Enter Epsilon: "))
episodes = int(input("Enter Number of Episodes: "))

states = rows * cols
q_table = np.zeros((states, 4))

actions = ["Up", "Down", "Left", "Right"]

for episode in range(episodes):

    row = 0
    col = 0

    while True:

        state = row * cols + col

        if random.random() < epsilon:
            action = random.randint(0, 3)
        else:
            action = np.argmax(q_table[state])

        new_row = row
        new_col = col

        if action == 0:
            new_row = max(0, row - 1)
        elif action == 1:
            new_row = min(rows - 1, row + 1)
        elif action == 2:
            new_col = max(0, col - 1)
        else:
            new_col = min(cols - 1, col + 1)

        reward = 0

        if new_row == food_row and new_col == food_col:
            reward = 10
        elif new_row == ghost_row and new_col == ghost_col:
            reward = -10

        next_state = new_row * cols + new_col

        q_table[state][action] += alpha * (
            reward + gamma * np.max(q_table[next_state])
            - q_table[state][action]
        )

        row = new_row
        col = new_col

        if reward == 10 or reward == -10:
            break

print("Learned Q-Table:")
print(q_table)

print("\nBest Action for Each State:")
for i in range(states):
    print(f"State {i} -> {actions[np.argmax(q_table[i])]}")
