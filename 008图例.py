"""
图例：

"""
from matplotlib import pyplot as plt
import numpy as np
x = np.arange(10)
# 方法1：
plt.figure()
plt.plot(x, x, 'r', label='a')
plt.plot(x, 2*x, label='b')
plt.plot(x, 3*x, 'k', label='y')
plt.legend(loc=1, ncol=3)
# loc表示图例的位置1为右上，2为左上，3为左下，4为右下
# ncol表示图例的列数

# 方法2：
plt.figure()
plt.plot(x, x, 'r', x, 2*x, x, 3*x, 'k')
plt.legend(['a', 'b', 'c'])


# 面向对象的方式：
fig3 = plt.figure()
ax1 = fig3.add_subplot()
l, = ax1.plot(x, x)
# 方法1：
# ax1.legend(['a'], loc=1)
# 方法2：
l.set_label('a')
ax1.legend()
# 方法3：
ax1.plot(x, 3*x, label='h')
ax1.legend()



plt.show()

