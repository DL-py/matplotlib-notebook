"""
极坐标：

"""
import matplotlib.pyplot as plt
import numpy as np
r = np.arange(1, 6, 1)
theta = [0, np.pi/2, np.pi, np.pi*3/2, 0]
ax = plt.subplot(111, projection='polar')  # 投影成极坐标
plt.plot(theta, r, 'r')
plt.grid(True)
plt.show()
