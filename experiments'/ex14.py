import numpy as np

rows = int(input("Enter Number of Rows: "))
cols = int(input("Enter Number of Columns: "))

goal_row = int(input("Enter Goal Row: "))
goal_col = int(input("Enter Goal Column: "))

obs_row = int(input("Enter Obstacle Row: "))
obs_col = int(input("Enter Obstacle Column: "))

gamma = float(input("Enter Discount Factor: "))
iterations = int(input("Enter Number of Iterations: "))

states = rows * cols

value = np.zeros(states)
policy = np.zeros(states, dtype=int)

actions = ["Up", "Down", "Left", "Right"]

for k in range(iterations):

    while True:

        delta = 0

        for state in range(states):

            row = state // cols
            col = state % cols

            if (row == goal_row and col == goal_col) or (row == obs_row and col == obs_col):
                continue

            action = policy[state]

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

            next_state = new_row * cols + new_col

            reward = -1

            if new_row == goal_row and new_col == goal_col:
                reward = 10
            elif new_row == obs_row and new_col == obs_col:
                reward = -10

            old = value[state]
            value[state] = reward + gamma * value[next_state]

            delta = max(delta, abs(old - value[state]))

        if delta < 0.01:
            break

    for state in range(states):

        row = state // cols
        col = state % cols

        if (row == goal_row and col == goal_col) or (row == obs_row and col == obs_col):
            continue

        best_action = 0
        best_value = -9999

        for action in range(4):

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

            next_state = new_row * cols + new_col

            reward = -1

            if new_row == goal_row and new_col == goal_col:
                reward = 10
            elif new_row == obs_row and new_col == obs_col:
                reward = -10

            temp = reward + gamma * value[next_state]

            if temp > best_value:
                best_value = temp
                best_action = action

        policy[state] = best_action

print("Value Function:")
print(value.reshape(rows, cols))

print("\nOptimal Policy:")
for i in range(states):
    print(f"State {i} -> {actions[policy[i]]}")
