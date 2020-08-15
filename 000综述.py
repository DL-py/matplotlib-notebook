"""
matplotlib:可视化工具箱
"""
"""
1.使用方法：
1.1导入from matplotlib import pyplot as plt
1.2绘图结束后需要加入plt.show()
1.3matplotlib中所有的绘图都希望提供numpy数组类型的数据
"""
"""
2.说明：
2.1matplotlib有3种绘图方式：
1.pyplot方法：用于进行快速的交互式绘图
2.pylab方法：将numpy和pyplot放入独立的命名空间，使用方法与matlab相同，不推荐使用
3.面向对象的方式：matplotlib的精髓，用于定制图像,面向对象没有交互功能。
2.2matplotlib中的对象:
1.Figure对象：整个图形区域
2.Axes对象：有坐标轴的绘图对象
3.Axis对象：Axes对象中的x,y,z轴
注意：一个Figure对象可以含有多个Axes对象，一个Axes对象可以含有2个或3个Axis对象
"""
"""
3.常用的格式：
3.1常用的颜色：
1.r 红色、b 蓝色、g 绿色、y 黄色、k 黑色
3.2常用的点的形状：
'.'、','、'o'、'v'、'<'、'>'、'v'
3.3常用的线型：
'-' 实线 '--' '-.' ':'
"""