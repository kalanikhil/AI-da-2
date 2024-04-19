# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bWbK4Jd4FJBtyhG1xLkopT3DcEBzlMCn
"""

import numpy as np

# Define the environment (Grid World)
grid_size = (3, 4)
num_actions = 4  # 4 possible actions: up, down, left, right

# Define the reward structure of the environment
rewards = np.zeros(grid_size)
rewards[2, 3] = 1  # Goal state with a reward of 1

# Define the Q-table
Q = np.zeros(grid_size + (num_actions,))

# Define hyperparameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Epsilon-greedy exploration rate

# Define helper function to choose an action
def choose_action(state):
    if np.random.rand() < epsilon:
        return np.random.randint(num_actions)  # Random action (exploration)
    else:
        return np.argmax(Q[state])  # Greedy action (exploitation)

# Define helper function to update Q-values
def update_Q(state, action, reward, next_state):
    best_next_action = np.argmax(Q[next_state])
    td_target = reward + gamma * Q[next_state][best_next_action]
    td_error = td_target - Q[state][action]
    Q[state][action] += alpha * td_error

# Training loop
num_episodes = 1000
for episode in range(num_episodes):
    state = (0, 0)  # Start state
    while state != (2, 3):  # Continue until reaching the goal state
        action = choose_action(state)
        next_state = (max(0, min(state[0] + (action - 1) // 2, grid_size[0] - 1)),
                      max(0, min(state[1] + (action - 2) % 2, grid_size[1] - 1)))
        reward = rewards[next_state]
        update_Q(state, action, reward, next_state)
        state = next_state

# After training, the Q-table contains the learned action-values

# Print the learned Q-values
print("Learned Q-values:")
print(Q)

# You can use the learned Q-values to find the optimal policy and make decisions accordingly.