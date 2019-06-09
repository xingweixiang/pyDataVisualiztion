import matplotlib.pyplot as pl
import numpy as np

x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
y = np.cos(x)
y1 = np.sin(x)
pl.plot(x, y)
pl.plot(x, y1)
# 图表名称
pl.title("Functions $\sin$ and $\cos$")
# x,y轴坐标范围
pl.xlim(-3, 3)
pl.ylim(-1, 1)
# 坐标上刻度
pl.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
pl.yticks([-1, 0, 1],
       [r'$-1$', r'$0$', r'$+1$'])
# 网格
pl.grid()
pl.savefig('./img/sin-cos.jpg')#保存成图片
pl.show()
