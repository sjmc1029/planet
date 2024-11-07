import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 타이틀
st.title("외계 행성 트랜짓 시뮬레이션")

# 행성 반지름과 궤도 주기 슬라이더
planet_radius = st.slider("행성 반지름 (지구 반지름의 배수)", 0.1, 2.0, 1.0)
orbital_period = st.slider("궤도 주기 (일)", 1, 100, 10)

# 시간과 밝기 설정
time = np.linspace(0, orbital_period * 2, 1000)
brightness = np.ones_like(time)

# 행성의 트랜짓 효과 시뮬레이션
transit_duration = orbital_period * 0.05  # 트랜짓 시간
transit_start = orbital_period / 2 - transit_duration / 2
transit_end = transit_start + transit_duration

# 트랜짓에 따른 광도 변화
for i, t in enumerate(time):
    if transit_start <= t % orbital_period <= transit_end:
        brightness[i] = 1 - 0.01 * (planet_radius ** 2)

# 그래프 출력
plt.figure(figsize=(10, 4))
plt.plot(time, brightness, label="광도 변화")
plt.xlabel("시간")
plt.ylabel("광도")
plt.title("행성 트랜짓에 의한 별의 광도 변화")
plt.ylim(0.9, 1.0)
st.pyplot(plt)
