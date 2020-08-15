"""
样式美化：

"""
import matplotlib.pyplot as plt
import numpy as np
# 样式美化：
plt.style.use('ggplot')
# plt.style.use('fivethirtyeight')
# 第一个图像：
fig, ax = plt.subplots(ncols=2, nrows=2)  # 生成4个子图
ax1, ax2, ax3, ax4 = ax.ravel()  # 将4个子图分给这四个对象
x, y = np.random.normal(size=(2, 100))
ax1.plot(x, y, 'o')
# 第二个图像：
x = np.arange(10)
y = np.arange(10)
ncolors = len(plt.rcParams['axes.prop_cycle'])
shift = np.linspace(0, 10, ncolors)
for s in shift:
    ax2.plot(x, y+s, '-')
# 第三个图像：
x = np.arange(5)
y1, y2, y3 = np.random.randint(1, 25, size=(3, 5))
width = 0.25
ax3.bar(x, y1, width)
ax3.bar(x+width, y2, width, color='g')
ax3.bar(x+2*width, y3, width, color='r')

# 图像4：
for i, color in enumerate(list('rbgykmrbgykm')):
    x, y = np.random.normal(size=2)
    ax4.add_patch(plt.Circle([x, y], 0.3, color=color))

ax4.axis('equal')
plt.show()
