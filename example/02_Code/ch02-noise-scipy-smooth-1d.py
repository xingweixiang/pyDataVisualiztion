import numpy
from numpy import *
from pylab import *

WINDOWS = ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']

def smooth(x, window_len=11, window='hanning'):

    if x.ndim != 1:
        raise ValueError("smooth only accepts 1 dimension arrays.")

    if x.size < window_len:
        raise ValueError("Input vector needs to be bigger than window size.")

    if window_len < 3:
        return x

    if not window in WINDOWS:
        raise ValueError("Window is one of 'flat', 'hanning', 'hamming', "
                          "'bartlett', 'blackman'")


    s=numpy.r_[x[window_len-1:0:-1], x, x[-1:-window_len:-1]]

    if window == 'flat': #moving average
        w = numpy.ones(window_len, 'd')
    else:
        w = eval('numpy.' + window + '(window_len)')

    y = numpy.convolve(w/w.sum(), s, mode='valid')
    return y


t = linspace(-4, 4, 100)

x = sin(t)
xn = x + randn(len(t))*0.1

y = smooth(x)

ws = 31

subplot(211)
plot(ones(ws))


for w in WINDOWS[1:]:
    eval('plot('+w+'(ws) )')

axis([0, 30, 0, 1.1])

legend(WINDOWS)

title("Smoothing windows")

# add second plot
subplot(212)
plot(x)

plot(xn)
for w in WINDOWS:
    plot(smooth(xn, 10, w))

# add legend for every graph
l=['original signal', 'signal with noise']
l.extend(WINDOWS)
legend(l)

title("Smoothed signal")
plt.savefig('./img/scipy-smooth.jpg')
show()
