import random

rewards = [2, 5, 8, 4]

epsilon = 0.1

counts = [0, 0, 0, 0]
values = [0, 0, 0, 0]

total_reward = 0

for i in range(500):

    if random.random() < epsilon:
        arm = random.randint(0, 3)
    else:
        arm = values.index(max(values))

    reward = rewards[arm]
    total_reward += reward

    counts[arm] += 1

    values[arm] = values[arm] + (reward - values[arm]) / counts[arm]

print("Epsilon =", epsilon)
print("Estimated Values =", values)
print("Arm Selection Count =", counts)
print("Total Reward =", total_reward)
