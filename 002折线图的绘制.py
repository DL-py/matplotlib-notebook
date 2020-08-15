"""
折线图：
2.1注意：
1.可以只提供y的数据，也可以提供多对x,y的数据
"""
from matplotlib import pyplot as plt
import numpy as np
x = np.arange(10)
# 绘图方法：
fig = plt.figure()
ax = fig.add_subplot()
ax.plot(x, x**2, 'r-.', x, 2*x, 'b-')
plt.show()