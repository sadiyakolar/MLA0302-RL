#A call center wants to optimize the assignment of customer service representatives to
incoming calls. Implement a Monte Carlo simulation to estimate the value function for
different assignment policies in Python.

import random

print("CALL CENTER MONTE CARLO SIMULATION")

representatives = int(
    input("Enter Number of Representatives: ")
)

episodes = int(
    input("Enter Number of Episodes: ")
)

calls = int(
    input("Enter Number of Calls per Episode: ")
)

returns = [0] * representatives
count = [0] * representatives

for episode in range(episodes):

    episode_rewards = [0] * representatives

    for call in range(calls):

        representative = random.randint(
            0, representatives - 1
        )

        reward = random.randint(1, 10)

        episode_rewards[representative] += reward

    for i in range(representatives):

        returns[i] += episode_rewards[i]
        count[i] += 1

print("\nMonte Carlo Value Function")

values = []

for i in range(representatives):

    value = returns[i] / count[i]

    values.append(value)

    print(
        "Representative",
        i + 1,
        "Value =",
        round(value, 2)
    )

best = values.index(max(values))

print("\nBest Representative:",
      best + 1)

print("Highest Value:",
      round(values[best], 2))

print("\nSimulation Completed")
