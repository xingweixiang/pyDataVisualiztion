from pylab import *
import numpy as np

x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
y = np.cos(x)
y1 = np.sin(x)
plot(x, y)

plot(x, y1)
title("Functions $\sin$ and $\cos$")
xlim(-3.0, 3.0)
ylim(-1.0, 1.0)
xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
          [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
yticks([-1, 0, +1],
          [r'$-1$', r'$0$', r'$+1$'])
show()
