from matplotlib.pyplot import *

import matplotlib.pyplot as plt
import numpy as np

plt.figure()
ax = plt.gca()
y = np.random.randn(9)
col_labels = ['c1', 'c2', 'c3']
row_labels = ['r1', 'r2', 'r3']
table_vals = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
row_colors = ['r', 'g', 'b']
my_table = plt.table(cellText=table_vals,
                     colWidths=[0.1] * 3,
                     rowLabels=row_labels,
                     colLabels=col_labels,
                     rowColours=row_colors,
                     loc='upper right')
plt.plot(y)
plt, show()
plt.savefig('./img/rec12.jpg')
