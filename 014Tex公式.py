"""
Tex公式：
# 需要用$$做开头和结尾，下划线是表示下标
遇到不会的可以参考matplotlib文档中的2.5.7小节
"""
import matplotlib.pyplot as plt
import numpy as np
fig1 = plt.figure()
ax1 = fig1.add_subplot()
ax1.set_xlim(xmin=-5, xmax=5)
ax1.set_ylim(ymin=0, ymax=10)
# 方法：
ax1.text(-4, 4, r"$\alpha_i \beta_j \pi \lambda \omega$", size=25)
ax1.text(-4, 8, r"$\sin(0)=\cos(\frac{\pi}{2})$", size=25)
ax1.text(0, 2, r"$\lim_{x \rightarrow y} \frac{1}{x^3}$", size=25)
ax1.text(0, 6, r"$\sqrt[4]{x}= \sqrt{y}$", size=25)

plt.show()
