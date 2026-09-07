import numpy as np
import matplotlib.pyplot as plt


# 1. NumPy arange
# np.arange(시작, 끝, 간격)
numbers = np.arange(0, 30, 5)

print(numbers)
# [ 0  5 10 15 20 25 ]


# 2. Matplotlib 기본 그래프
ypoints = np.array([3, 8, 1, 10])

# * : 별 모양 마커
# : : 점선
# y : yellow(노란색)
plt.plot(ypoints, "*:y")

plt.show()