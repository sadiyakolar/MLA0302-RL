#Simulate an RL framework to optimize a manufacturing process, where actions represent
different machine settings and rewards are based on product quality. Implement the
environment, policy, and value function in Python.

import numpy as np
import random

n = int(input("Enter Grid Size: "))

alpha = float(input("Enter Learning Rate: "))
gamma = float(input("Enter Discount Factor: "))
episodes = int(input("Enter Number of Episodes: "))

q = np.zeros((n, n, 4))

actions = ["Up", "Down", "Left", "Right"]

for episode in range(episodes):

    r = 0
    c = 0
    path = []

    for step in range(20):

        state = (r, c)
        action = random.randint(0, 3)

        nr, nc = r, c

        if action == 0:
            nr -= 1
        elif action == 1:
            nr += 1
        elif action == 2:
            nc -= 1
        else:
            nc += 1

        if nr < 0 or nr >= n or nc < 0 or nc >= n:
            reward = -5
            nr, nc = r, c
        elif nr == n-1 and nc == n-1:
            reward = 10
        else:
            reward = -1

        path.append((r, c, action, reward))

        r, c = nr, nc

        if r == n-1 and c == n-1:
            break

    G = 0

    for r, c, action, reward in reversed(path):
        G = reward + gamma * G
        q[r][c][action] += alpha * G

print("\nTraining Completed")

r = 0
c = 0

print("\nOptimal Path:")

for step in range(20):

    print((r, c))

    if r == n-1 and c == n-1:
        break

    action = np.argmax(q[r][c])

    if action == 0:
        r = max(0, r-1)
    elif action == 1:
        r = min(n-1, r+1)
    elif action == 2:
        c = max(0, c-1)
    else:
        c = min(n-1, c+1)

print((r, c))
