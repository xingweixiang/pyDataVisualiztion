from matplotlib.pyplot import *

import matplotlib.pyplot as plt
import numpy as np

plt.figure(0)
# 子图的分割规划
a1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
a2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
a3 = plt.subplot2grid((3, 3), (1, 2), colspan=1)
a4 = plt.subplot2grid((3, 3), (2, 0), colspan=1)
a5 = plt.subplot2grid((3, 3), (2, 1), colspan=2)
all_axex = plt.gcf().axes
for ax in all_axex:
    for ticklabel in ax.get_xticklabels() + ax.get_yticklabels():
        ticklabel.set_fontsize(10)
plt.suptitle("Demo")
plt.show()
plt.savefig('./img/rec13.jpg')
