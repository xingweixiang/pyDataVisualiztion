import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import random
import matplotlib.dates as mdates
from mpl_toolkits.mplot3d import Axes3D

mpl.rcParams['font.size'] = 10
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for z in [2015, 2016, 2017]:
    xs = range(1, 13)
    ys = 1000 * np.random.rand(12)
    color = plt.cm.Set2(random.choice(range(plt.cm.Set2.N)))
    ax.bar(xs, ys, zs=z, zdir='y', color=color, alpha=0.8)
ax.xaxis.set_major_locator(mpl.ticker.FixedLocator(xs))
ax.yaxis.set_major_locator(mpl.ticker.FixedLocator(ys))
ax.set_xlabel('M')
ax.set_ylabel('Y')
ax.set_zlabel('Sales')
plt.savefig('./img/rec01.jpg')
plt.show()

