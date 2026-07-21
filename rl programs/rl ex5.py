SIZE = 5

pickup = (4, 4)

gamma = 0.9

values = [[0 for j in range(SIZE)] for i in range(SIZE)]

while True:

    delta = 0
    new_values = [[0 for j in range(SIZE)] for i in range(SIZE)]

    for i in range(SIZE):
        for j in range(SIZE):

            if (i, j) == pickup:
                new_values[i][j] = 10
                continue

            actions = []

            if i > 0:
                actions.append(values[i - 1][j])

            if i < SIZE - 1:
                actions.append(values[i + 1][j])

            if j > 0:
                actions.append(values[i][j - 1])

            if j < SIZE - 1:
                actions.append(values[i][j + 1])

            new_values[i][j] = -1 + gamma * max(actions)

            delta = max(delta, abs(new_values[i][j] - values[i][j]))

    values = new_values

    if delta < 0.01:
        break

policy = [["" for j in range(SIZE)] for i in range(SIZE)]

for i in range(SIZE):
    for j in range(SIZE):

        if (i, j) == pickup:
            policy[i][j] = "Goal"
            continue

        best = -9999
        move = ""

        if i > 0 and values[i - 1][j] > best:
            best = values[i - 1][j]
            move = "UP"

        if i < SIZE - 1 and values[i + 1][j] > best:
            best = values[i + 1][j]
            move = "DOWN"

        if j > 0 and values[i][j - 1] > best:
            best = values[i][j - 1]
            move = "LEFT"

        if j < SIZE - 1 and values[i][j + 1] > best:
            best = values[i][j + 1]
            move = "RIGHT"

        policy[i][j] = move

print("Optimal Policy")

for row in policy:
    print(row)

print("\nValue Function")

for row in values:
    print(row)
