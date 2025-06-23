import numpy as np
import matplotlib.pyplot as plt
import os

# Load original spike data
spikes = np.load("assets/spike_data_normal.npy")

# Simulate attack: randomly inject 300 fake spikes into low-index neurons (0–10)
num_fake_spikes = 300
fake_spikes = np.random.choice(np.arange(0, 10), size=num_fake_spikes)
attacked_spikes = np.concatenate((spikes, fake_spikes))

# Save spike raster plot
plt.figure(figsize=(10, 4))
plt.plot(np.arange(len(attacked_spikes)), attacked_spikes, '.r', label='Fake Spikes')
plt.title("Spike Raster Plot (Attacked Mode)")
plt.xlabel("Time Index (Simulated)")
plt.ylabel("Neuron Index")
plt.grid(True)
plt.tight_layout()

os.makedirs("assets", exist_ok=True)
plt.savefig("assets/spike_raster_attacked.png")
plt.close()

# Recompute power leak
num_neurons = 100
power_leak_attacked = np.zeros(num_neurons)
for i in attacked_spikes:
    if int(i) < num_neurons:
        power_leak_attacked[int(i)] += 1

# Normalize and plot
power_leak_norm = power_leak_attacked / power_leak_attacked.max()
plt.figure(figsize=(10, 3))
plt.bar(range(num_neurons), power_leak_norm, color='orange')
plt.xlabel("Neuron Index")
plt.ylabel("Normalized Power")
plt.title("Estimated Power Leakage (Attacked Mode)")
plt.grid(True)
plt.tight_layout()
plt.savefig("assets/power_leak_attacked.png")
plt.close()

# Save the attacked power values
np.save("assets/power_leak_attacked.npy", power_leak_attacked)
