from matplotlib.pyplot import *
#添加图例和注释
import numpy as np

x1 = np.random.normal(30, 2, 100)

plot(x1, label='plot')

# 图例

# 图标的起始位置，宽度，高度 归一化坐标

# loc 可选，为了图标不覆盖图

# ncol 图例个数

# 图例平铺

# 坐标轴和图例边界之间的间距

legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=4,

       ncol=1, mode="expand", borderaxespad=0.1)

# 注解

# Import data 注释

# （55,30） 要关注的点

# xycoords = ‘data’ 注释和数据使用相同坐标系

# xytest 注释的位置

# arrowprops注释用的箭头

annotate("Import data", (55, 30), xycoords='data',

         xytext=(5, 35),

         arrowprops=dict(arrowstyle='->'))
savefig('./img/rec07.jpg')
show()

