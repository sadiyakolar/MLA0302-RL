import random

actions = ["Buy", "Sell", "Hold"]
profit = 0

for day in range(10):

    action = random.choice(actions)

    if action == "Buy":
        reward = random.randint(5,15)

    elif action == "Sell":
        reward = random.randint(0,10)

    else:
        reward = random.randint(-2,5)

    profit += reward

    print("Day", day+1, "-", action, "Reward =", reward)

print("\nTotal Profit =", profit)
