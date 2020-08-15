"""
网格:

"""
from matplotlib import pyplot as plt
import numpy as np
x = np.arange(10)
plt.plot(x, x**2, 'r')
plt.grid(color='r', lw='1', ls='--')
# lw表示线宽，ls表示线型
plt.show()
