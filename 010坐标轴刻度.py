"""
坐标轴刻度：

"""
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-10, 11)
plt.figure()  # 获得当前Figure
fig1 = plt.gcf()
fig1.add_subplot()
ax1 = plt.gca()  # 获得当前Figure中的axes
ax1.plot(x, x**2)
# 方法1：
ax1.locator_params('x', nbins=30)  # nbins表示列数,可以指定具体的轴
# 方法2：
plt.locator_params('y', nbins=20)

plt.show()
