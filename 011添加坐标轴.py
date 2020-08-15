"""
添加坐标轴：

"""
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(2, 20)
plt.plot(x, x**2)
# 方法1：
plt.twinx()  # 创建另一个坐标轴，共享x轴
plt.plot(x, np.log(x), 'r')


# 方法2:面向对象的方式：
fig2 = plt.figure()
ax1 = fig2.add_subplot()
ax1.plot(x, x**2)
ax1.set_ylabel('y1')  # 用于设置y轴的坐标
ax2 = ax1.twinx()  # ax2的类型与ax1的类型相同twiny与twinx类似
ax2.plot(x, np.log(x), 'r')
ax2.set_ylabel('y2')
plt.show()
