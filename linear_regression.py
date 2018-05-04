import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create fake data

observations = 1000

xs = np.random.uniform(low = -10, high = 10, size = (observations,1))
zs = np.random.uniform(-10, 10, (observations,1))

inputs = np.column_stack((xs, zs))

# Create targets

noise = np.random.uniform(-1,1,(observations,1))
targets = 2*xs - 3*zs + 5 + noise

targets = targets.reshape(observations,1)

# Initialise Variables

init_range = 0.1
weights = np.random.uniform(-init_range, init_range, size=(2,1))
biases = np.random.uniform(-init_range, init_range, size=1)

learning_rate = 0.02

# Train model

for i in range (1000):
    outputs = np.dot(inputs, weights) + biases
    deltas = outputs - targets
    
    loss = np.sum(deltas **2 ) / 10 / observations
    
    print(loss)
    
    deltas_scaled = deltas / observations
    
    weights = weights - learning_rate * np.dot(inputs.T, deltas_scaled)
    biases = biases - learning_rate * np.sum(deltas_scaled)

print (weights, biases)
