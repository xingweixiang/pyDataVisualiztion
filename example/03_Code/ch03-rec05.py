from matplotlib.pyplot import *
#设置图表的线型、属性和格式化字符串
import numpy as np
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
y = np.cos(x)
y1 = np.sin(x)
# 线段颜色，线条风格，线条宽度，线条标记，标记的边缘颜色，标记边缘宽度，标记内颜色，标记大小
plot([1, 2], c='r', ls='-', lw=2, marker='D', mec='g', mew=2, mfc='b', ms=30)
plot(x, y1)
# 图表名称
title("Functions $\sin$ and $\cos$")
# x,y轴坐标范围
xlim(-3, 3)
ylim(-1, 4)
# 坐标上刻度
xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
yticks([-1, 0, 1],
       [r'$-1$', r'$0$', r'$+1$'])
grid()
savefig('./img/rec05.jpg')
show()

