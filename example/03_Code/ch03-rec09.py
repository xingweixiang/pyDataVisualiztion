import matplotlib.pyplot as plt
#误差条形图
import numpy as np

x = np.arange(0, 10, 1)
y = np.log(x)
xe = 0.1 * np.abs(np.random.randn(len(y)))
plt.bar(x, y, yerr=xe, width=0.4, align='center',
        ecolor='r', color='cyan', label='experimert')
plt.xlabel('x')
plt.ylabel('y')
plt.title('measurements')
plt.legend(loc='upper left')  # 这种图例用法更直接
plt.savefig('./img/rec09.jpg')
plt.show()

