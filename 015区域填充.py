"""
区域填充：

"""
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-2*np.pi, 2*np.pi, 100)
fig1 = plt.figure()
ax1 = fig1.add_subplot()
# 方法：fill填充与x轴的区域
ax1.fill(x, np.sin(x), 'g', alpha=0.3)
ax1.fill(x, np.sin(2*x), 'y', alpha=0.3)
fig2 = plt.figure()
# 方法2：fill_between在两条曲线之间进行填充,并通过where进行判断：
# 数据较少时可能会出现空白区域，interpolate=True表示可以自动将空白区域填充颜色
plt.fill_between(x, np.sin(x), np.sin(2*x), where=np.sin(x) > np.sin(2*x),
                 facecolor='g', interpolate=True)
plt.show()
