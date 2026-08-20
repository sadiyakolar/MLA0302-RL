#Set up an environment using OpenAI Gym and implement a policy to solve the MountainCar
problem. Utilize Python libraries like Keras or TensorFlow to build and train the policy.


import gymnasium as gym
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.optimizers import Adam
import random

env = gym.make("MountainCar-v0")

alpha = float(input("Enter Learning Rate: "))
gamma = float(input("Enter Discount Factor: "))
epsilon = float(input("Enter Epsilon: "))
episodes = int(input("Enter Number of Episodes: "))

model = Sequential([
    Input(shape=(2,)),
    Dense(16, activation="relu"),
    Dense(16, activation="relu"),
    Dense(3, activation="linear")
])

model.compile(optimizer=Adam(learning_rate=alpha), loss="mse")

for episode in range(episodes):

    print("Episode:", episode + 1)

    state, info = env.reset()
    state = np.reshape(state, (1, 2))

    done = False
    step = 0

    while not done and step < 20:

        if random.random() < epsilon:
            action = env.action_space.sample()
        else:
            q_values = model.predict(state, verbose=0)
            action = np.argmax(q_values[0])

        next_state, reward, terminated, truncated, info = env.step(action)

        done = terminated or truncated

        next_state = np.reshape(next_state, (1, 2))

        target = reward

        if not done:
            target = reward + gamma * np.max(model.predict(next_state, verbose=0)[0])

        target_q = model.predict(state, verbose=0)
        target_q[0][action] = target

        state = next_state
        step += 1

    model.fit(state, target_q, epochs=1, verbose=0)

print("\nTraining Completed")

state, info = env.reset()
state = np.reshape(state, (1, 2))

done = False
total_reward = 0
steps = 0

while not done and steps < 20:

    q_values = model.predict(state, verbose=0)
    action = np.argmax(q_values[0])

    next_state, reward, terminated, truncated, info = env.step(action)

    done = terminated or truncated

    total_reward += reward
    state = np.reshape(next_state, (1, 2))
    steps += 1

print("Total Reward:", total_reward)

env.close()
