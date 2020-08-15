"""
子图：
"""
from matplotlib import pyplot as plt
import numpy as np
x = np.arange(1, 4)
# 方法1：add_subplot()方法
fig1 = plt.figure()
# 表示生成2*2个图形，左上角标号是1，右上角标号是2
ax1 = fig1.add_subplot(2, 2, 1)
# ax1 = fig1.add_subplot(221) 当每个数字都小于10的时候，两者等价
ax1.plot(x, x**2)

# 方法2：plt.subplot()与方法1类似

# 方法3：plt.axes()函数
fig2 = plt.figure()
# ax2 = plt.axes()  充满整个fig2对象
# ax2 = plt.axes((0.1, 0.1, 0.5, 0.5), facecolor='k')
# 指定具体的位置,facecolor用于是指定背景色

# 方法4：fig2.add_axes()函数
ax3 = fig2.add_axes((0.1, 0.1, 0.5, 0.5), facecolor='w')

plt.show()
