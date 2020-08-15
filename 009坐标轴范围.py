"""
坐标轴范围：

"""
from matplotlib import pyplot as plt
import numpy as np
x = np.arange(-10, 11)
plt.plot(x, x**2)
data = plt.axis()  # 返回坐标轴的范围(0.0, 1.0, 0.0, 1.0)
# 方法1：
plt.axis([-5, 5, 0, 50])
# 方法2：
plt.xlim([-3, 3])  # 只调整x轴的范围
plt.xlim(xmin=-5, xmax=5)  # 也可以只调整一边
plt.ylim([-5, 40])  # 只调整y轴的范围
plt.ylim(ymin=0, ymax=50)
# 面向对象的方法：
fig1 = plt.figure()
ax1 = fig1.add_subplot()
ax1.set_xlim(xmin=-5, xmax=5)
ax1.set_ylim(ymin=0, ymax=10)
plt.show()
