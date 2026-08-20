#Implement an epsilon-greedy strategy to optimize content recommendations on an online
learning platform. Write a Python script to simulate and analyze its performance over
multiple runs.


import numpy as np
import random

states = int(input("Enter Number of Racing States: "))
episodes = int(input("Enter Number of Episodes: "))

actions = ["Brake", "Accelerate", "Turn"]

actor = np.zeros((states, 3))
critic = np.zeros(states)

alpha = 0.1
gamma = 0.9

for episode in range(episodes):

    state = random.randint(0, states - 1)

    action = np.argmax(actor[state])

    if random.random() < 0.3:
        action = random.randint(0, 2)

    rewards = [2, 10, 5]
    reward = rewards[action]

    next_state = random.randint(0, states - 1)

    td_error = reward + gamma * critic[next_state] - critic[state]

    critic[state] += alpha * td_error

    actor[state][action] += alpha * td_error

    print("Episode:", episode + 1)

print("\nTraining Completed")

print("\nActor Values:")
print(actor)

print("\nBest Driving Action:")

for i in range(states):
    action = np.argmax(actor[i])
    print("State", i + 1, "->", actions[action])
