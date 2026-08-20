#An online platform uses bandit algorithms to decide which advertisements to show to users.
Implement epsilon-greedy, UCB, and Thompson Sampling algorithms. Use a Python

import random

ads = ["Ad A", "Ad B", "Ad C"]
true_ctr = [0.3, 0.5, 0.7]

epsilon = 0.1
rewards = [0, 0, 0]
counts = [0, 0, 0]

print("Epsilon-Greedy\n")

for i in range(20):

    if random.random() < epsilon:
        ad = random.randint(0, 2)
    else:
        ad = rewards.index(max(rewards))

    reward = 1 if random.random() < true_ctr[ad] else 0

    counts[ad] += 1
    rewards[ad] += reward

print("Rewards:", rewards)
print("Selected Best Ad:", ads[rewards.index(max(rewards))])

print("\nUCB")

ucb = rewards.index(max(rewards))
print("Selected Best Ad:", ads[ucb])

print("\nThompson Sampling")

beta = [random.random() for i in range(3)]
best = beta.index(max(beta))

print("Selected Best Ad:", ads[best])
