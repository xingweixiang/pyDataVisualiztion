from matplotlib.pyplot import *
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

t = range(1000)
y = [sqrt(i) for i in t]
plt.plot(t, y, color='r', lw=2)
plt.fill_between(t, y, color='y')
plt.show()
plt.savefig('./img/rec15.jpg')
