from brian2 import *
import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs("assets", exist_ok=True)

# Simulation setup
start_scope()
duration = 1 * second  # 1 second simulation

#  Define neuron model (LIF: Leaky Integrate & Fire)
eqs = '''
dv/dt = (1.0 - v) / (10*ms) : 1
'''

# Create 100 neurons
G = NeuronGroup(100, eqs, threshold='v > 0.8', reset='v = 0', method='exact')
G.v = 'rand()'  # random initial voltage

# Monitor spikes
spike_monitor = SpikeMonitor(G)

#  Run the simulation
run(duration)

# Plot spike raster
plt.figure(figsize=(10, 4))
plt.plot(spike_monitor.t/ms, spike_monitor.i, '.k')
plt.xlabel('Time (ms)')
plt.ylabel('Neuron index')
plt.title('Spike Raster Plot (Normal Mode)')
plt.grid(True)
plt.tight_layout()


plt.savefig("assets/spike_raster_normal.png")
np.save("assets/spike_data_normal.npy", spike_monitor.i)

plt.show()
