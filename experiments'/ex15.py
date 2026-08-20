#A call center uses Monte Carlo methods to optimize the assignment of customer service
representatives to incoming calls. Implement Monte Carlo policy control in Python to
minimize average call handling time.

import numpy as np
import random

n = int(input("Enter Number of Representatives: "))

times = []
for i in range(n):
    t = int(input(f"Enter Call Handling Time for Rep {i+1}: "))
    times.append(t)

alpha = float(input("Enter Learning Rate: "))
gamma = float(input("Enter Discount Factor: "))
epsilon = float(input("Enter Epsilon: "))
episodes = int(input("Enter Number of Episodes: "))

q_table = np.zeros((n, 2))

actions = ["Assign", "Skip"]

returns = [[] for _ in range(n * 2)]

for episode in range(episodes):

    visited = []

    for state in range(n):

        if random.random() < epsilon:
            action = random.randint(0, 1)
        else:
            action = np.argmax(q_table[state])

        if action == 0:
            reward = -times[state]
        else:
            reward = -5

        visited.append((state, action, reward))

    G = 0

    for state, action, reward in reversed(visited):

        G = reward + gamma * G

        index = state * 2 + action
        returns[index].append(G)

        q_table[state][action] = q_table[state][action] + alpha * (
            np.mean(returns[index]) - q_table[state][action]
        )

print("Learned Q-Table:")
print(q_table)

print("\nBest Action for Each Representative:")
for i in range(n):
    print(f"Representative {i+1} -> {actions[np.argmax(q_table[i])]}")
