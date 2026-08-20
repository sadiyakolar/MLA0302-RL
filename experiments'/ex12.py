#A robot vacuum cleaner navigates a house with various rooms and obstacles. Use the SARSA
algorithm to learn the optimal cleaning policy that maximizes the cleaned area while
minimizing energy usage. Implement this in Python.

import numpy as np
import random

n = int(input("Enter Number of Rooms: "))

rewards = []
for i in range(n):
    reward = int(input(f"Enter Reward for Room {i+1}: "))
    rewards.append(reward)

alpha = float(input("Enter Learning Rate: "))
gamma = float(input("Enter Discount Factor: "))
epsilon = float(input("Enter Epsilon: "))
episodes = int(input("Enter Number of Episodes: "))

q_table = np.zeros((n, 3))

actions = ["Left", "Clean", "Right"]

for episode in range(episodes):

    state = random.randint(0, n - 1)

    if random.random() < epsilon:
        action = random.randint(0, 2)
    else:
        action = np.argmax(q_table[state])

    while True:

        if action == 0:
            next_state = max(0, state - 1)
        elif action == 2:
            next_state = min(n - 1, state + 1)
        else:
            next_state = state

        reward = rewards[next_state]

        if random.random() < epsilon:
            next_action = random.randint(0, 2)
        else:
            next_action = np.argmax(q_table[next_state])

        q_table[state][action] += alpha * (
            reward + gamma * q_table[next_state][next_action]
            - q_table[state][action]
        )

        state = next_state
        action = next_action

        if state == n - 1:
            break

print("Learned Q-Table:")
print(q_table)

print("\nBest Action for Each Room:")
for i in range(n):
    print(f"Room {i+1} | Reward = {rewards[i]} -> {actions[np.argmax(q_table[i])]}")
