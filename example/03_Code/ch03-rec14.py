import matplotlib.pyplot as plt

import numpy as np
import matplotlib as mpl

def process_signals(x, y):
    return (1 - (x ** 2 + y ** 2)) * np.exp(-y ** 3 / 3)
x = np.arange(-1.5, 1.5, 0.1)
y = np.arange(-1.5, 1.5, 0.1)
X, Y = np.meshgrid(x, y)
Z = process_signals(X, Y)
N = np.arange(-1, 1.5, 0.3)  # 作为等值线的间隔
CS = plt.contour(Z, N, linewidths=2, cmap=mpl.cm.jet)
plt.clabel(CS, inline=True, fmt='%1.1f', fontsize=10)  # 等值线标签
plt.colorbar(CS)
plt.savefig('./img/rec14.jpg')
plt.show()

