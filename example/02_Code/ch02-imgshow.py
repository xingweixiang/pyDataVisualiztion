import scipy.misc
import matplotlib.pyplot as plt
#lena = scipy.misc.lena()
lena = scipy.misc.ascent()
plt.gray()
plt.imshow(lena)
plt.colorbar()
plt.show()
