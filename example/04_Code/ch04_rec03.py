import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import random
from mpl_toolkits.mplot3d import Axes3D

mpl.rcParams['font.size'] = 10
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
samples = 25
x = np.random.normal(5, 1, samples)  # x上正态分布
y = np.random.normal(3, .5, samples)  # y上正态分布
# xy平面上，按照10*10的网格划分，落在网格内个数hist，x划分边界、y划分边界
hist, xedges, yedges = np.histogram2d(x, y, bins=10)
elements = (len(xedges) - 1) * (len(yedges) - 1)
xpos, ypos = np.meshgrid(xedges[:-1] + .25, yedges[:-1] + .25)
xpos = xpos.flatten()  # 多维数组变为一维数组
ypos = ypos.flatten()
zpos = np.zeros(elements)
dx = .1 * np.ones_like(zpos)  # zpos一致的全1数组
dy = dx.copy()
dz = hist.flatten()
# 每个立体以（xpos,ypos,zpos)为左下角，以（xpos+dx,ypos+dy,zpos+dz）为右上角
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', alpha=0.4)
plt.savefig('./img/rec03.jpg')
plt.show()

