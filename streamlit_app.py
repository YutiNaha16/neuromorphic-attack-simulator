import streamlit as st
import numpy as np
from PIL import Image
import os

st.set_page_config(page_title="NeuroStrike Dashboard", layout="wide")

st.title("  Neuromorphic Attack Simulation")
st.markdown("Visualize SNN Behavior + Power Leakage Side-Channel Attack")

# Dropdown to select mode
mode = st.selectbox("Select Mode", ["Normal", "Power Attack"])

col1, col2 = st.columns(2)

# Raster Plot Display
with col1:
    st.subheader(" Spike Raster Plot")
    raster_path = "assets/spike_raster_normal.png" if mode == "Normal" else "assets/spike_raster_attacked.png"
    if os.path.exists(raster_path):
        st.image(Image.open(raster_path), use_container_width=True)
    else:
        st.warning(f"Raster plot not found at {raster_path}")

# Power Leakage Display
with col2:
    st.subheader(" Estimated Power Leakage")
    power_path = "assets/power_leak_normal.png" if mode == "Normal" else "assets/power_leak_attacked.png"
    if os.path.exists(power_path):
        st.image(Image.open(power_path), use_container_width=True)
    else:
        st.warning(f"Power chart not found at {power_path}")

# Power Meter (fun visual)
st.sidebar.header(" Power Meter")
power_array_path = "assets/power_leak_normal.npy" if mode == "Normal" else "assets/power_leak_attacked.npy"

if os.path.exists(power_array_path):
    power_array = np.load(power_array_path)
    avg_power = np.mean(power_array)
    st.sidebar.progress(min(int(avg_power), 100))
    st.sidebar.text(f"Avg Power Level: {avg_power:.2f}")
else:
    st.sidebar.warning("Power data missing.")
# Power anomaly detection (basic threshold logic)
if os.path.exists(power_array_path):
    power_array = np.load(power_array_path)
    avg_power = np.mean(power_array)

    st.sidebar.progress(min(int(avg_power), 100))
    st.sidebar.text(f"Avg Power Level: {avg_power:.2f}")

    # ⚠Detection threshold (tune as you like)
    if mode == "Power Attack" and avg_power > 50:
        st.sidebar.error("Abnormal Power Detected! Possible Attack")
    elif mode == "Normal" and avg_power <= 50:
        st.sidebar.success("Power Levels Normal")
    else:
        st.sidebar.warning("Unusual: No specific condition matched")

# Footer
st.markdown("---")
st.markdown("Made with  Brian2 [GitHub](https://github.com/YutiNaha16")
