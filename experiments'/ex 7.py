gamma = 0.9

rewards = [0, 0, 10]

V = [0, 0, 0]

for i in range(10):
    V[2] = rewards[2]
    V[1] = rewards[1] + gamma * V[2]
    V[0] = rewards[0] + gamma * V[1]

print("State Values")

for i in range(3):
    print("State", i, "=", round(V[i],2))
