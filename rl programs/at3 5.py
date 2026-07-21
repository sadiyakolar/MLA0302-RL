import numpy as np

gamma = 0.9

V = np.zeros(4)

reward = [0, 0, 0, 10]

for i in range(10):
    newV = np.copy(V)

    for s in range(3):
        newV[s] = reward[s] + gamma * V[s + 1]

    newV[3] = reward[3]

    V = newV

print("Optimal State Values")
print(V)
