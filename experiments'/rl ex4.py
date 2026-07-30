SIZE = 5

goal = (4, 4)

policy = [["R" for j in range(SIZE)] for i in range(SIZE)]
value = [[0 for j in range(SIZE)] for i in range(SIZE)]

gamma = 0.9

while True:

    for k in range(20):
        new_value = [[0 for j in range(SIZE)] for i in range(SIZE)]

        for i in range(SIZE):
            for j in range(SIZE):

                if (i, j) == goal:
                    new_value[i][j] = 10
                    continue

                action = policy[i][j]

                ni, nj = i, j

                if action == "U" and i > 0:
                    ni -= 1
                elif action == "D" and i < SIZE - 1:
                    ni += 1
                elif action == "L" and j > 0:
                    nj -= 1
                elif action == "R" and j < SIZE - 1:
                    nj += 1

                reward = -1
                new_value[i][j] = reward + gamma * value[ni][nj]

        value = new_value

    stable = True

    for i in range(SIZE):
        for j in range(SIZE):

            if (i, j) == goal:
                continue

            actions = ["U", "D", "L", "R"]
            best_action = policy[i][j]
            best_value = -9999

            for action in actions:

                ni, nj = i, j

                if action == "U" and i > 0:
                    ni -= 1
                elif action == "D" and i < SIZE - 1:
                    ni += 1
                elif action == "L" and j > 0:
                    nj -= 1
                elif action == "R" and j < SIZE - 1:
                    nj += 1

                score = -1 + gamma * value[ni][nj]

                if score > best_value:
                    best_value = score
                    best_action = action

            if best_action != policy[i][j]:
                stable = False

            policy[i][j] = best_action

    if stable:
        break

print("Optimal Policy")

for row in policy:
    print(row)

print("\nValue Function")

for row in value:
    print(row)
