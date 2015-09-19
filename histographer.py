import matplotlib.pyplot as plt
import random
import numpy as np
from scipy.interpolate import UnivariateSpline
import operator

random.seed(1)
def drange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step

k = 2427754752 + 1
flatColorDBlue = '#34495e'
flatColorMatrix = ['#e74c3c','#3498db','#f1c40f']

dist = []
peaks = []
for x in range(0,3):
    peaks.append([random.randint(0,k),float(random.randint(1,10)/100)])

print peaks
for x in range(0,1000000):
    num = random.randint(0,k)
    inRange = False
    for peak in peaks:
        val = float((abs(peak[0]-num))/float(((peak[0] + num)/2)))
        if val < peak[1]:
            inRange = True
    if inRange:
        dist.append(num)
    elif random.random() < 0.001:
        dist.append(num)

histo = np.histogram(dist,50)
plt.hist(dist,50,color=flatColorDBlue)
plt.xlabel('Keyspace Position')
plt.ylabel('Number of Nodes in Bin')
plt.title('Curve Fitting of Keyspace Distribution')
ax = plt.gca()
ax.set_xlim([0,k])
plt.legend(loc='best',fancybox=True, framealpha=0.8)
plt.savefig('histogram.pdf',format='pdf')
plt.show()


