#A financial institution wants to optimize its investment strategy. Use a basic policy gradient
method to simulate and optimize the investment policy for maximum returns. Implement
this in Python.


import random
import math

print("FINANCIAL INVESTMENT USING POLICY GRADIENT")

investments = int(
    input("Enter Number of Investments: ")
)

episodes = int(
    input("Enter Number of Episodes: ")
)

learning_rate = float(
    input("Enter Learning Rate: ")
)

policy = [0.0] * investments

returns = [0] * investments

for episode in range(episodes):

    probabilities = []

    total = 0

    for i in range(investments):
        p = math.exp(policy[i])
        probabilities.append(p)
        total += p

    for i in range(investments):
        probabilities[i] /= total

    random_number = random.random()

    cumulative = 0
    action = 0

    for i in range(investments):

        cumulative += probabilities[i]

        if random_number <= cumulative:
            action = i
            break

    reward = random.randint(1, 10)

    returns[action] += reward

    for i in range(investments):

        if i == action:
            gradient = 1 - probabilities[i]
        else:
            gradient = -probabilities[i]

        policy[i] += learning_rate * reward * gradient

    if episode % 5 == 0:

        print(
            "Episode:",
            episode + 1,
            "Selected Investment:",
            action + 1,
            "Reward:",
            reward
        )

print("\nFinal Investment Policy")

total = 0
probabilities = []

for i in range(investments):
    p = math.exp(policy[i])
    probabilities.append(p)
    total += p

for i in range(investments):

    probabilities[i] /= total

    print(
        "Investment",
        i + 1,
        "Probability =",
        round(probabilities[i], 3)
    )

best = probabilities.index(
    max(probabilities)
)

print("\nBest Investment:",
      best + 1)

print("Training Completed")
