import matplotlib.pyplot as mpl
#设置刻度、时间刻度标签、网格
from pylab import *

import datetime
import numpy as np

fig = figure()
ax = gca()
# 时间区间
start = datetime.datetime(2017, 11, 11)
stop = datetime.datetime(2017, 11, 30)
delta = datetime.timedelta(days=1)
dates = mpl.dates.drange(start, stop, delta)
values = np.random.rand(len(dates))
ax.plot_date(dates, values, ls='-')
date_format = mpl.dates.DateFormatter('%Y-%m-%d')
ax.xaxis.set_major_formatter(date_format)
fig.autofmt_xdate()
savefig('./img/rec06.jpg')
show()

