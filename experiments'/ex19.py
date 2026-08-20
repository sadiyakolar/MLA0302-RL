#Use Monte Carlo methods to evaluate a policy for predicting customer churn in a
subscription-based service. Implement this policy evaluation in Python and analyze the
results.

import numpy as np
import random

states = int(input("Enter Number of Game States: "))
episodes = int(input("Enter Number of Episodes: "))

actions = ["Build", "Gather", "Attack"]

actor = np.zeros((states, 3))
critic = np.zeros(states)

alpha = 0.1
gamma = 0.9

for episode in range(episodes):

    state = random.randint(0, states - 1)

    action = np.argmax(actor[state])

    if random.random() < 0.3:
        action = random.randint(0, 2)

    rewards = [5, 3, 10]
    reward = rewards[action]

    next_state = random.randint(0, states - 1)

    td_error = reward + gamma * critic[next_state] - critic[state]

    critic[state] += alpha * td_error

    actor[state][action] += alpha * td_error

    print("Episode:", episode + 1)

print("\nTraining Completed")

print("\nActor Values:")
print(actor)

print("\nBest Action:")

for i in range(states):
    action = np.argmax(actor[i])
    print("State", i + 1, "->", actions[action])
