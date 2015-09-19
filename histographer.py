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
x = (0.5*(histo[1] + np.roll(histo[1], 1)))[1:]
xsto = x
y = histo[0]
xBinSize = x[1] - x[0]
indexMax, valueMax = max(enumerate(x), key=operator.itemgetter(1))
np.insert(x,0,(x[0] - xBinSize))
np.insert(y,0,y[indexMax])
indexMin, valueMin = min(enumerate(x), key=operator.itemgetter(1))
np.append(x,(x[-1] + xBinSize))
np.append(y,y[indexMin])
f2 = UnivariateSpline(x, y, k=5)
m = len(x)
var = np.var(y)
plt.hist(dist,50,color=flatColorDBlue)
plt.xlabel('Keyspace Position')
plt.ylabel('Number of Nodes in Bin')
plt.title('Curve Fitting of Keyspace Distribution')
ax = plt.gca()
ax.set_xlim([0,k])
vals = [1,1.5,4]
n = 0
for i in vals:
    print i
    scalingFactor = int((m * var)/i)
    f2.set_smoothing_factor(scalingFactor)
    pltHandle = plt.plot(xsto,f2(xsto),lw=2,label=('S = ' + str(scalingFactor)),color=flatColorMatrix[n])
    n += 1
plt.legend(loc='best',fancybox=True, framealpha=0.8)
plt.savefig('histogram.pdf',format='pdf')
plt.show()


