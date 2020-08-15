"""
条形图的绘制：
"""
from matplotlib import pyplot as plt
import numpy as np
x = np.arange(10)
y = np.arange(0, 100, 10)
y1 =np.arange(0, 50, 5)
# 垂直的条形图:height是因变量，width用于改变宽度 color用于改变颜色
plt.figure(1)
plt.bar(x, height=y, width=0.5, color='r')

# 水平的条形图
plt.figure(2)
plt.barh(x, width=y, height=0.5, color='b')

# 叠形统计图
fig3 = plt.figure()
ax = fig3.add_subplot()
ax.bar(x, height=y, width=0.5, color='r')
ax.bar(x, bottom=y, height=y1, width=0.5, color='b')

plt.show()
