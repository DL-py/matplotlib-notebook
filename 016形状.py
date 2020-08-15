"""
区域填充：

"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpaches
fig, ax = plt.subplots()  # 这种方式可以同时返回Figure对象和axes对象
# 方法：生成圆
circle = mpaches.Circle(np.array([0.2, 0.2]), 0.03)
ax.add_patch(circle)
# 方法：生成矩形
rect = mpaches.Rectangle([0.1, 0.1], 0.05, 0.03, color='r')
ax.add_patch(rect)
# [0.1, 0.1]表示左下角的坐标，0.2表示宽，0.1表示高
# 方法：生成多边形
polygon = mpaches.RegularPolygon([0.225, 0.12], 5, 0.03, color='y')
ax.add_patch(polygon)
# 方法：椭圆生成的方法：
ellips = mpaches.Ellipse([0.125, 0.2], 0.03, 0.04)
ax.add_patch(ellips)
plt.axis('equal')  # 表示x,y坐标轴刻度相等
ax.grid(alpha=0.3)
plt.show()






