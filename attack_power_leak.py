import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs("assets", exist_ok=True)

# Load spike data from normal mode
spike_indices = np.load("assets/spike_data_normal.npy")

# Count spikes per neuron (power = spike count)
num_neurons = 100
power_leak = np.zeros(num_neurons)

for i in spike_indices:
    power_leak[int(i)] += 1

# Normalize power values (0 to 1 scale)
power_leak_norm = power_leak / power_leak.max()

# Visualize power heatmap
plt.figure(figsize=(10, 3))
plt.bar(range(num_neurons), power_leak_norm, color='red')
plt.xlabel("Neuron Index")
plt.ylabel("Normalized Power")
plt.title("Estimated Power Leakage (Normal Mode)")
plt.grid(True)
plt.tight_layout()
plt.savefig("assets/power_leak_normal.png")
plt.show()

np.save("assets/power_leak_normal.npy", power_leak)
