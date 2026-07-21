import random

threshold = 50
energy = 0
reward = 0

for i in range(20):

    use = random.randint(1, 5)

    if energy + use <= threshold:
        energy += use
        reward += 10
    else:
        reward -= 5

print("Energy Used =", energy)
print("Total Reward =", reward)
