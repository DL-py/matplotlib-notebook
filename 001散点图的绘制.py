"""
1.散点图：
1.1注意：
1.必须同时指定x,y才能进行绘制
2.x,y需要是数组类型的数据
1.2说明：
1.s=2用于改变点的大小
2.color='r'用于改变点的颜色
3.alpha=0.6用于改变线的透明度
"""
from matplotlib import pyplot as plt
import numpy as np
x = np.arange(10)

# 绘图方法1:pyplot方法
plt.scatter(x, x**2, s=2, color='r', alpha=0.5)

# 绘图方法2：面向对象的方法
fig = plt.figure()  # 用于生一个Figure对象
ax = fig.add_subplot()  # 用于在Figure对象中生成一个Axes对象
ax.scatter(x, x**2, s=2, color='r', alpha=0.5)
plt.show()
