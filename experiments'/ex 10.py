import random

actions = ["Buy", "Sell", "Hold"]

for i in range(10):

    action = random.choice(actions)
    reward = random.randint(-5, 15)

    print(action, "Reward =", reward)
