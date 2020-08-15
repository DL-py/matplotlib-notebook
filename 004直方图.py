"""
直方图的绘制：

"""
from matplotlib import pyplot as plt
import numpy as np
y1 = np.random.randn(100)
y = y1 + 100
# edgecolor用于指定边框颜色
plt.hist(y, bins=10, edgecolor='r')
plt.show()


