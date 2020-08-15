"""
注释：

"""
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-10, 11, 1)
plt.plot(x, x**2, 'r--')
# 方法：plt.annotate()
plt.annotate('this is bottom', xy=(0, 1), xytext=(0, 20),
             arrowprops=dict(facecolor='r', headlength=5, headwidth=10, width=5))
# xy用于指定箭头的位置，xytest用于指定注释的位置,arrowprops用于配置箭的属性
# facecolor是箭头的颜色，headlength表示箭头前段的长度,width用于配置箭身的宽度
# headwith用于配置箭头前段的宽度
plt.show()
