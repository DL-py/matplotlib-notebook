"""
饼状图：
"""
from matplotlib import pyplot as plt
import numpy as np
y = np.arange(1, 4)
index = ['A', 'B', 'C']
fig1 = plt.figure()
ax = fig1.add_subplot()
# labels用于给各个扇形加入标签，autopct='%.2f'显示占比
# explode=[0.1, 0, 0]表示偏移距离,shadow表示加入阴影
ax.pie(y, labels=index, autopct='%.2f', explode=[0.1, 0, 0], shadow=True)
plt.show()


