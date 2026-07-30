import random

episodes = 10
total_reward = 0

for i in range(episodes):

    reward = random.randint(5, 10)
    total_reward += reward

average = total_reward / episodes

print("Total Reward :", total_reward)
print("Average Value Function :", round(average,2))
