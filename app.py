import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Streamlit layout
st.title("Star and Planet Orbit Simulation with Doppler Effect")
st.write("Move the planet to see the star's motion and observe the wavelength shift due to the Doppler effect.")

# Constants
star_mass = 1.0       # Mass of the star (in solar mass units)
planet_mass = 0.001   # Mass of the planet (similar to Jupiter)
star_distance = 0.5   # Distance of star from the center (in arbitrary units)
planet_distance = 1.0 # Distance of planet from the center (in arbitrary units)

# Slider to adjust planet's orbital angle
angle = st.slider("Planet angle (degrees)", 0, 360, 90)
angle_rad = np.deg2rad(angle)  # Convert angle to radians

# Calculate coordinates of the star and planet around the center of mass
planet_x = planet_distance * np.cos(angle_rad)
planet_y = planet_distance * np.sin(angle_rad)

star_x = -star_distance * np.cos(angle_rad)
star_y = -star_distance * np.sin(angle_rad)

# Doppler shift calculation based on the star's radial velocity
c = 299792.458  # Speed of light in km/s
max_velocity = 30  # Adjusted max velocity for dramatic Doppler effect (km/s)
radial_velocity = max_velocity * np.cos(angle_rad)  # Radial velocity changes with angle
doppler_shift = radial_velocity / c  # Calculate the Doppler shift

# Adjusted wavelength range for dramatic effect
base_wavelength = 656.3  # H-alpha line in nm
shifted_wavelength = base_wavelength * (1 + doppler_shift)

# Layout: two columns for side-by-side display
col1, col2 = st.columns(2)

# 1. Plotting the orbital motion with line-of-sight arrow (y-axis positive direction)
with col1:
    fig1, ax1 = plt.subplots()
    ax1.plot(0, 0, 'yo', markersize=5, label="Center of Mass")  # Smaller center of mass
    ax1.plot(planet_x, planet_y, 'bo', markersize=8, label="Planet")
    ax1.plot(star_x, star_y, 'ro', markersize=12, label="Star")
    
    # Line-of-sight arrow pointing upward (positive y-direction)
    ax1.arrow(0, -1.2, 0, 1.2, head_width=0.1, head_length=0.1, fc='gray', ec='gray', label="Line of Sight")
    ax1.text(0, 1.25, 'Line of Sight', color='gray', ha='center')
    
    ax1.set_xlim(-1.5, 1.5)
    ax1.set_ylim(-1.5, 1.5)
    ax1.set_aspect('equal', 'box')
    ax1.legend()
    ax1.set_title("Orbital Motion around Center of Mass")
    st.pyplot(fig1)

# 2. Plotting the wavelength shift (Doppler effect) with baseline wavelength
with col2:
    fig2, ax2 = plt.subplots()
    # Set a narrower wavelength range for a more dramatic effect
    wavelengths = np.linspace(656.20, 656.40, 1000)  # Narrowed range for greater contrast
    spectrum = np.exp(-((wavelengths - shifted_wavelength) ** 2) / 0.00002)  # Narrow Gaussian for spectral line
    ax2.plot(wavelengths, spectrum, 'k')
    
    # Baseline wavelength with transparency
    baseline_spectrum = np.exp(-((wavelengths - base_wavelength) ** 2) / 0.00002)
    ax2.plot(wavelengths, baseline_spectrum, 'k', alpha=0.3, label="Baseline λ")  # Baseline with transparency
    
    ax2.axvline(shifted_wavelength, color='red', linestyle='--', label=f"Shifted λ: {shifted_wavelength:.3f} nm")
    ax2.set_title("Wavelength Shift (Doppler Effect)")
    ax2.set_xlabel("Wavelength (nm)")
    ax2.set_ylabel("Intensity")
    ax2.set_xlim(656.20, 656.40)  # Set x-axis range for more detail
    ax2.legend()
    st.pyplot(fig2)

