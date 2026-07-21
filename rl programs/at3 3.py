import random

rewards = [2, 5, 8, 4]

random_reward = 0
greedy_reward = 0

for i in range(100):
    arm = random.randint(0, 3)
    random_reward += rewards[arm]

best_arm = rewards.index(max(rewards))

for i in range(100):
    greedy_reward += rewards[best_arm]

print("Random Reward =", random_reward)
print("Greedy Reward =", greedy_reward)
