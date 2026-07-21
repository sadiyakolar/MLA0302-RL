SIZE = 4
ITEM_REWARD = 2
GOAL_REWARD = 5
OBSTACLE_PENALTY = -2
item = (1, 2)
goal = (3, 3)
obstacle = (2, 1)
V = [[0 for j in range(SIZE)] for i in range(SIZE)]
gamma = 0.9
for iteration in range(10):
    new_V = [[0 for j in range(SIZE)] for i in range(SIZE)]
    for i in range(SIZE):
        for j in range(SIZE):
            if (i, j) == goal:
                new_V[i][j] = GOAL_REWARD
            elif (i, j) == item:
                new_V[i][j] = ITEM_REWARD + gamma * V[i][j]
            elif (i, j) == obstacle:
                new_V[i][j] = OBSTACLE_PENALTY + gamma * V[i][j]
            else:
                new_V[i][j] = gamma * V[i][j]
    V = new_V
print("Value Function:")
for row in V:
    print(row)
