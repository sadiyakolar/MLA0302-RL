import gym
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
import random

env = gym.make("MountainCar-v0")

alpha = float(input("Enter Learning Rate: "))
gamma = float(input("Enter Discount Factor: "))
epsilon = float(input("Enter Epsilon: "))
episodes = int(input("Enter Number of Episodes: "))

model = Sequential([
    Dense(24, activation="relu", input_shape=(2,)),
    Dense(24, activation="relu"),
    Dense(3, activation="linear")
])

model.compile(optimizer=Adam(learning_rate=alpha), loss="mse")

for episode in range(episodes):

    state = env.reset()

    if isinstance(state, tuple):
        state = state[0]

    state = np.reshape(state, (1, 2))

    done = False

    while not done:

        if random.random() < epsilon:
            action = env.action_space.sample()
        else:
            q = model.predict(state, verbose=0)
            action = np.argmax(q[0])

        result = env.step(action)

        if len(result) == 5:
            next_state, reward, terminated, truncated, info = result
            done = terminated or truncated
        else:
            next_state, reward, done, info = result

        next_state = np.reshape(next_state, (1, 2))

        target = reward

        if not done:
            target = reward + gamma * np.max(model.predict(next_state, verbose=0)[0])

        target_q = model.predict(state, verbose=0)
        target_q[0][action] = target

        model.fit(state, target_q, epochs=1, verbose=0)

        state = next_state

print("\nTraining Completed")

state = env.reset()

if isinstance(state, tuple):
    state = state[0]

state = np.reshape(state, (1, 2))

done = False
total_reward = 0

while not done:

    q = model.predict(state, verbose=0)
    action = np.argmax(q[0])

    result = env.step(action)

    if len(result) == 5:
        next_state, reward, terminated, truncated, info = result
        done = terminated or truncated
    else:
        next_state, reward, done, info = result

    total_reward += reward
    state = np.reshape(next_state, (1, 2))

print("Total Reward:", total_reward)

env.close()
