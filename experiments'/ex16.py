#16) A robot navigates a grid to perform tasks. Use Bellman’s optimality equation to compute the
optimal state-value function for the robot’s navigation tasks. Implement this in Python and
demonstrate the optimal path.


import numpy as np

rows = int(input("Enter Number of Rows: "))
cols = int(input("Enter Number of Columns: "))

goal_row = int(input("Enter Goal Row: "))
goal_col = int(input("Enter Goal Column: "))

gamma = float(input("Enter Discount Factor: "))
iterations = int(input("Enter Number of Iterations: "))

value = np.zeros((rows, cols))

actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
action_name = ["Up", "Down", "Left", "Right"]

for k in range(iterations):

    new_value = value.copy()

    for i in range(rows):
        for j in range(cols):

            if i == goal_row and j == goal_col:
                continue

            best = -9999

            for dr, dc in actions:

                nr = max(0, min(rows - 1, i + dr))
                nc = max(0, min(cols - 1, j + dc))

                reward = -1

                if nr == goal_row and nc == goal_col:
                    reward = 10

                temp = reward + gamma * value[nr][nc]

                if temp > best:
                    best = temp

            new_value[i][j] = best

    value = new_value

print("\nOptimal State Value Function:")
print(value)

print("\nOptimal Path:")

r = 0
c = 0

print("Start ->", (r, c))

visited = set()

while (r != goal_row or c != goal_col):

    visited.add((r, c))

    best = -9999
    next_r = r
    next_c = c
    move = ""

    for i in range(4):

        nr = max(0, min(rows - 1, r + actions[i][0]))
        nc = max(0, min(cols - 1, c + actions[i][1]))

        if (nr, nc) not in visited and value[nr][nc] > best:
            best = value[nr][nc]
            next_r = nr
            next_c = nc
            move = action_name[i]

    if next_r == r and next_c == c:
        break

    print(move, "->", (next_r, next_c))

    r = next_r
    c = next_c

if r == goal_row and c == goal_col:
    print("Goal Reached!")
else:
    print("Goal Not Reached!")
