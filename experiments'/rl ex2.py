SIZE = int(input("Enter Grid Size (e.g., 5): "))
num_items = int(input("Enter number of item locations: "))
ITEMS = []
for i in range(num_items):
    x, y = map(int, input(f"Enter Item {i+1} position (row col): ").split())
    ITEMS.append((x, y))
goal_x, goal_y = map(int, input("Enter Goal position (row col): ").split())
GOAL = (goal_x, goal_y)
num_obstacles = int(input("Enter number of obstacles: "))
OBSTACLES = []
for i in range(num_obstacles):
    x, y = map(int, input(f"Enter Obstacle {i+1} position (row col): ").split())
    OBSTACLES.append((x, y))
gamma = float(input("Enter Discount Factor (e.g., 0.9): "))
iterations = int(input("Enter Number of Iterations: "))
V = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
def next_state(i, j):
    if j < SIZE - 1:
        return (i, j + 1)
    elif i < SIZE - 1:
        return (i + 1, j)
    else:
        return (i, j)
def reward(state):
    if state in ITEMS:
        return 2
    elif state == GOAL:
        return 5
    elif state in OBSTACLES:
        return -2
    else:
        return 0
for k in range(iterations):
    new_V = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    for i in range(SIZE):
        for j in range(SIZE):
            s_next = next_state(i, j)
            r = reward(s_next)
            new_V[i][j] = r + gamma * V[s_next[0]][s_next[1]]
    V = new_V
print("\nWarehouse Robot Policy Evaluation")
print("---------------------------------")
for row in V:
    for value in row:
        print(f"{value:7.2f}", end=" ")
    print()
