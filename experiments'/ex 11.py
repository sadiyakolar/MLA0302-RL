#Implement Double DQN to optimize a stock trading strategy. The agent should learn to buy,
sell, or hold stocks to maximize profits. Write a Python script to simulate the trading
environment and train the agent.

import random

print("DOUBLE DQN - STOCK TRADING")

episodes = int(input("Enter Number of Episodes: "))
learning_rate = float(input("Enter Learning Rate: "))
gamma = float(input("Enter Discount Factor: "))
epsilon = float(input("Enter Epsilon: "))

actions = ["BUY", "SELL", "HOLD"]

q_online = [0.0, 0.0, 0.0]
q_target = [0.0, 0.0, 0.0]

for episode in range(episodes):

    price = random.randint(50, 100)
    old_price = price

    if random.random() < epsilon:
        action = random.randint(0, 2)
    else:
        action = q_online.index(max(q_online))

    new_price = random.randint(50, 100)

    if action == 0:
        reward = new_price - old_price

    elif action == 1:
        reward = old_price - new_price

    else:
        reward = 0

    best_action = q_online.index(max(q_online))

    target = reward + gamma * q_target[best_action]

    q_online[action] = q_online[action] + learning_rate * (
        target - q_online[action]
    )

    if episode % 5 == 0:
        q_target = q_online.copy()

    if episode % 10 == 0:
        print(
            "Episode:", episode + 1,
            "Action:", actions[action],
            "Reward:", reward
        )

print("\nFinal Q Values")

for i in range(3):
    print(actions[i], "=", round(q_online[i], 2))

best = q_online.index(max(q_online))

print("\nBest Trading Action:", actions[best])
print("Training Completed")
