import random
SIZE = 5
dirt = [(1, 2), (2, 4), (4, 1)]
obstacles = [(1, 1), (3, 3)]
position = [0, 0]
reward = 0
actions = ["UP", "DOWN", "LEFT", "RIGHT"]
print("Robot Starting Position:", tuple(position))
for step in range(20):
    action = random.choice(actions)
    new_pos = position.copy()
    if action == "UP" and position[0] > 0:
        new_pos[0] -= 1
    elif action == "DOWN" and position[0] < SIZE - 1:
        new_pos[0] += 1
    elif action == "LEFT" and position[1] > 0:
        new_pos[1] -= 1
    elif action == "RIGHT" and position[1] < SIZE - 1:
        new_pos[1] += 1
    position = new_pos
    if tuple(position) in dirt:
        reward += 1
        print(position, "-> Dirt Cleaned (+1)")
        dirt.remove(tuple(position))
    elif tuple(position) in obstacles:
        reward -= 1
        print(position, "-> Obstacle (-1)")
    else:
        print(position, "-> Empty Cell")
    if len(dirt) == 0:
        print("All dirt cleaned!")
        break
print("Total Reward =", reward)
