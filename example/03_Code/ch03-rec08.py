import matplotlib.pyplot as plt
#设置坐标轴
import numpy as np
x = np.linspace(-np.pi, np.pi, 500, endpoint=True)
y = np.sin(x)
plt.plot(x,y)
ax = plt.gca()
#top bottom left right 四条线段框成的
#上下边界颜色
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('r')
#坐标轴位置
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
#坐标轴上刻度位置
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.grid()
plt.show()
plt.savefig('./img/rec08.jpg')

