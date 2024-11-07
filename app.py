import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Streamlit 레이아웃 설정
st.title("별과 행성의 궤도 운동과 파장 변화 시뮬레이션")
st.write("행성을 움직이면 별이 반대 방향으로 움직이며, 파장이 변화하는 모습을 관찰하세요.")

# 궤도 운동을 위한 초기 설정 값
star_mass = 1.0  # 태양 질량 단위
planet_mass = 0.001  # 행성의 질량 (목성 정도의 질량)
distance = 1.0  # 행성의 공전 반지름 (AU 단위)

# 사용자가 행성의 위치를 조절하도록 슬라이더를 제공
angle = st.slider("행성의 각도 (도)", 0, 360, 90)
angle_rad = np.deg2rad(angle)  # 라디안으로 변환

# 공통질량 중심 계산
common_center = (planet_mass * distance) / (star_mass + planet_mass)

# 행성과 별의 좌표 계산
planet_x = distance * np.cos(angle_rad)
planet_y = distance * np.sin(angle_rad)
star_x = -common_center * np.cos(angle_rad)
star_y = -common_center * np.sin(angle_rad)

# 파장 변화 계산 (도플러 효과 적용)
c = 299792.458  # 빛의 속도 (km/s)
velocity = (planet_mass / (planet_mass + star_mass)) * np.sqrt((4 * np.pi ** 2 * distance) / (star_mass + planet_mass))
doppler_shift = velocity / c
wavelength = 656.3  # H-alpha 파장 (nm)
shifted_wavelength = wavelength * (1 + doppler_shift * np.cos(angle_rad))

# 1. 궤도 그림 시각화
fig1, ax1 = plt.subplots()
ax1.plot(0, 0, 'yo', markersize=10, label="공통질량 중심")
ax1.plot(planet_x, planet_y, 'bo', markersize=8, label="행성")
ax1.plot(star_x, star_y, 'ro', markersize=12, label="별")
ax1.set_xlim(-1.5, 1.5)
ax1.set_ylim(-1.5, 1.5)
ax1.set_aspect('equal', 'box')
ax1.legend()
ax1.set_title("궤도 운동 시각화")
st.pyplot(fig1)

# 2. 파장 변화 시각화 (스펙트럼 형태)
fig2, ax2 = plt.subplots()
wavelengths = np.linspace(650, 660, 1000)  # 범위 내의 파장
spectrum = np.exp(-((wavelengths - shifted_wavelength) ** 2) / 0.1)  # 가우시안으로 스펙트럼 구현
ax2.plot(wavelengths, spectrum, 'k')
ax2.axvline(shifted_wavelength, color='red', linestyle='--', label=f"Shifted λ: {shifted_wavelength:.2f} nm")
ax2.set_title("파장 변화 (도플러 효과)")
ax2.set_xlabel("파장 (nm)")
ax2.set_ylabel("강도")
ax2.legend()
st.pyplot(fig2)

