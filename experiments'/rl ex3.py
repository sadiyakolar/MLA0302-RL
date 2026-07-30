import random
import math

prices = [100, 120, 150]
prob = [0.3, 0.5, 0.7]
steps = 100

epsilon = 0.1

eg_reward = [0, 0, 0]
eg_count = [0, 0, 0]

ucb_reward = [0, 0, 0]
ucb_count = [1, 1, 1]

ts_success = [1, 1, 1]
ts_failure = [1, 1, 1]

eg_total = 0
ucb_total = 0
ts_total = 0

for t in range(steps):

    if random.random() < epsilon:
        arm = random.randint(0, 2)
    else:
        avg = []
        for i in range(3):
            if eg_count[i] == 0:
                avg.append(0)
            else:
                avg.append(eg_reward[i] / eg_count[i])
        arm = avg.index(max(avg))

    reward = prices[arm] if random.random() < prob[arm] else 0
    eg_reward[arm] += reward
    eg_count[arm] += 1
    eg_total += reward

for t in range(steps):

    values = []
    for i in range(3):
        avg = ucb_reward[i] / ucb_count[i]
        bonus = math.sqrt((2 * math.log(t + 2)) / ucb_count[i])
        values.append(avg + bonus)

    arm = values.index(max(values))

    reward = prices[arm] if random.random() < prob[arm] else 0
    ucb_reward[arm] += reward
    ucb_count[arm] += 1
    ucb_total += reward

for t in range(steps):

    samples = []
    for i in range(3):
        samples.append(random.betavariate(ts_success[i], ts_failure[i]))

    arm = samples.index(max(samples))

    if random.random() < prob[arm]:
        reward = prices[arm]
        ts_success[arm] += 1
    else:
        reward = 0
        ts_failure[arm] += 1

    ts_total += reward

print("Epsilon-Greedy Revenue =", eg_total)
print("UCB Revenue =", ucb_total)
print("Thompson Sampling Revenue =", ts_total)

best = max(eg_total, ucb_total, ts_total)

if best == eg_total:
    print("Best Strategy: Epsilon-Greedy")
elif best == ucb_total:
    print("Best Strategy: UCB")
else:
    print("Best Strategy: Thompson Sampling")
