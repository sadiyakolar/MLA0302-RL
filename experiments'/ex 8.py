#Simulate an autonomous car navigating a simple road network with intersections. Design
policies for the car to follow traffic rules and reach the destination safely. Implement these
policies in Python and evaluate their effectiveness.

import random

print("AUTONOMOUS CAR ROAD NAVIGATION")

states = int(input("Enter Number of Road States: "))
episodes = int(input("Enter Number of Episodes: "))

actions = ["Left", "Right"]

q = []

for i in range(states):
    q.append([0, 0])

alpha = 0.1
gamma = 0.9
epsilon = 0.2

for episode in range(episodes):

    state = 0
    total_reward = 0

    for step in range(20):

        if random.random() < epsilon:
            action = random.randint(0, 1)
        else:
            action = q[state].index(max(q[state]))

        if action == 0:
            next_state = max(0, state - 1)
            reward = 2
        else:
            next_state = min(states - 1, state + 1)
            reward = 5

        if next_state == states - 1:
            reward = 10

        q[state][action] = q[state][action] + alpha * (
            reward +
            gamma * max(q[next_state]) -
            q[state][action]
        )

        total_reward += reward
        state = next_state

        if state == states - 1:
            break

    if episode % 5 == 0:
        print("Episode:", episode + 1,
              "Reward:", total_reward)

print("\nLearned Road Policy")

for state in range(states):

    action = q[state].index(max(q[state]))

    print("State", state + 1,
          "->", actions[action])

print("\nTraining Completed")
