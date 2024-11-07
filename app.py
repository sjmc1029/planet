import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Streamlit layout
st.title("Orbit Simulation of Star and Planet around Center of Mass")
st.write("Move the planet to see the star's motion and observe the wavelength shift caused by the Doppler effect.")

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
max_velocity = 30  # Maximum radial velocity of the star (arbitrary units)
radial_velocity = max_velocity * np.cos(angle_rad)  # Radial velocity varies with position
doppler_shift = radial_velocity / c  # Doppler shift based on radial velocity
base_wavelength = 656.3  # H-alpha line in nm
shifted_wavelength = base_wavelength * (1 + doppler_shift)

# 1. Plotting the orbital motion
fig1, ax1 = plt.subplots()
ax1.plot(0, 0, 'yo', markersize=10, label="Center of Mass")
ax1.plot(planet_x, planet_y, 'bo', markersize=8, label="Planet")
ax1.plot(star_x, star_y, 'ro', markersize=12, label="Star")
ax1.set_xlim(-1.5, 1.5)
ax1.set_ylim(-1.5, 1.5)
ax1.set_aspect('equal', 'box')
ax1.legend()
ax1.set_title("Orbital Motion around Center of Mass")
st.pyplot(fig1)

# 2. Plotting the wavelength shift (Doppler effect)
fig2, ax2 = plt.subplots()
wavelengths = np.linspace(650, 660, 1000)  # Wavelength range
spectrum = np.exp(-((wavelengths - shifted_wavelength) ** 2) / 0.1)  # Gaussian to simulate spectral line
ax2.plot(wavelengths, spectrum, 'k')
ax2.axvline(shifted_wavelength, color='red', linestyle='--', label=f"Shifted λ: {shifted_wavelength:.2f} nm")
ax2.set_title("Wavelength Shift (Doppler Effect)")
ax2.set_xlabel("Wavelength (nm)")
ax2.set_ylabel("Intensity")
ax2.legend()
st.pyplot(fig2)
