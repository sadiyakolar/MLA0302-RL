#A delivery robot operates in a warehouse with predefined delivery points. Using Bellman
equations, compute the state-value function for navigating to each delivery point.
Implement this in Python and visualize the value function for different policies.

import numpy as np

print("DELIVERY ROBOT USING BELLMAN EQUATION")

n = int(input("Enter Number of Delivery Points: "))
gamma = float(input("Enter Discount Factor: "))
iterations = int(input("Enter Number of Iterations: "))

rewards = []

for i in range(n):
    r = float(input("Enter Reward for Delivery Point " + str(i + 1) + ": "))
    rewards.append(r)

value = np.zeros(n)

for iteration in range(iterations):

    new_value = np.zeros(n)

    for state in range(n):

        left = max(0, state - 1)
        right = min(n - 1, state + 1)

        left_value = rewards[left] + gamma * value[left]
        right_value = rewards[right] + gamma * value[right]

        new_value[state] = max(left_value, right_value)

    value = new_value

print("\nFinal State-Value Function")

for i in range(n):
    print("Delivery Point", i + 1, "=", round(value[i], 2))

best = np.argmax(value)

print("\nBest Delivery Point:", best + 1)
print("Highest Value:", round(value[best], 2))
