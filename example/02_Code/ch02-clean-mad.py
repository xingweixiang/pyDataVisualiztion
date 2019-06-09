import numpy as np
import matplotlib.pyplot as plt

def is_outlier(points, threshold=3.5):
    """
    1、生成0-1之间的随机数据
    2、加入一些异常值
    3、用is_outlier()方法检测异常值
    4、绘制出两个数据集合（X和filtered）的图表，观察它们的区别
    """
    if len(points.shape) == 1:
        points = points[:,None]

    # compute median value    
    median = np.median(points, axis=0)
    
    # compute diff sums along the axis
    diff = np.sum((points - median)**2, axis=-1)
    diff = np.sqrt(diff)
    # compute MAD
    med_abs_deviation = np.median(diff)

    modified_z_score = 0.6745 * diff / med_abs_deviation

    # return a mask for each outlier
    return modified_z_score > threshold

# Random data
x = np.random.random(100)

# histogram buckets
buckets = 50

# Add in a few outliers
x = np.r_[x, -49, 95, 100, -100]

filtered = x[~is_outlier(x)]

# plot histograms
plt.figure()

plt.subplot(211)
plt.hist(x, buckets)
plt.xlabel('Raw')

plt.subplot(212)
plt.hist(filtered, buckets)
plt.xlabel('Cleaned')
plt.savefig('./img/clean-mad.jpg')
plt.show()

