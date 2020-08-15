"""
文字：
"""
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-10, 11)
plt.plot(x, x**2)
plt.text(0, 40, 'y=x**2', family='fantasy', size=10, color='r',
         style='italic', weight='black', bbox=dict(facecolor='y', alpha=0.5))
# 0,40表示x,y坐标,family表示字体类型，size表示字体大小,style='italic'表示斜体
# weight表示字体的粗细：black表示粗体，light表示细，bbox表示一个框框
# 利用ax1.text()同样可以实现
plt.show()
