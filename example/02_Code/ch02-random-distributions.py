# coding: utf-8
import random
import matplotlib
import matplotlib.pyplot as plt

SAMPLE_SIZE = 1000

buckets = 100

plt.figure()

matplotlib.rcParams.update({'font.size': 7})

plt.subplot(621)
plt.xlabel("random.random")
res = []
for _ in range(1, SAMPLE_SIZE):
        res.append(random.random())
plt.hist(res, buckets)

plt.subplot(622)
plt.xlabel("random.uniform")
a = 1 
b = SAMPLE_SIZE
res = []
for _ in range(1, SAMPLE_SIZE):
    res.append(random.uniform(a, b))
plt.hist(res, buckets)

plt.subplot(623)
plt.xlabel("random.triangular")
low = 1
high = SAMPLE_SIZE
res = []
for _ in range(1, SAMPLE_SIZE):
    res.append(random.triangular(low, high))
plt.hist(res, buckets)

plt.subplot(624)
plt.xlabel("random.betavariate")
alpha = 1
beta = 10
res = []
for _ in range(1, SAMPLE_SIZE):
    res.append(random.betavariate(alpha, beta))
plt.hist(res, buckets)

plt.subplot(625)
plt.xlabel("random.expovariate")
lambd = 1.0 / ((SAMPLE_SIZE + 1) / 2.)
res = []
for _ in range(1, SAMPLE_SIZE):
    res.append(random.expovariate(lambd))
    
plt.hist(res, buckets)

plt.subplot(626)
plt.xlabel("random.gammavariate")
alpha = 1
beta = 10
res = []
for _ in range(1, SAMPLE_SIZE):
        res.append(random.gammavariate(alpha, beta))
plt.hist(res, buckets)

plt.subplot(627)
plt.xlabel("random.lognormvariate")
mu = 1
sigma = 0.5
res = []
for _ in range(1, SAMPLE_SIZE):
    res.append(random.lognormvariate(mu, sigma))
plt.hist(res, buckets)

plt.subplot(628)
plt.xlabel("random.normalvariate")
mu = 1
sigma = 0.5
res = []
for _ in range(1, SAMPLE_SIZE):
    res.append(random.normalvariate(mu, sigma))
plt.hist(res, buckets)

plt.subplot(629)
plt.xlabel("random.paretovariate")
alpha = 1
res = []
for _ in range(1, SAMPLE_SIZE):
    res.append(random.paretovariate(alpha))
plt.hist(res, buckets)

plt.tight_layout()
plt.show()
