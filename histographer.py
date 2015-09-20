import matplotlib.pyplot as plt
import random
import numpy as np
import hashlib
import math

random.seed(1)
def drange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step

def hashList(listU):
    hashedList = []
    for entry in listU:
        hashedList.append(hashlib.sha256(str(entry)))
    return sorted(hashedList,key=lambda i: (i.hexdigest(), 16))

k = 2427754752 + 1
flatColorDBlue = '#34495e'
flatColorMatrix = ['#e74c3c','#3498db','#f1c40f']
dist = []
peaks = []
for x in range(0,3):
    peaks.append([random.randint(0,k),float(random.randint(1,10)/100)])
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

print dist
randomUserList = random.sample(range(1000000), len(dist))
hashedUserList = hashList(randomUserList)
sortedDist = sorted(dist)
print len(sortedDist)
print len(randomUserList)
tau = math.floor(len(sortedDist)/len(hashedUserList))

positions = []
tauStep = 0
for user in hashedUserList:
    try:
        items = sortedDist[int(tauStep):int((tauStep + tau + 1))]
    except:
        items = sortedDist[int(tauStep):]
    tauStep += tau
    avgPosition = np.mean(items)
    positions.append(avgPosition)
    print tauStep

yInts,edges = np.histogram(dist,bins=50)
edgepoints = []
for i in range(len(edges)-1):
    edgepoints.append(int((edges[i] + edges[1+i])/2))
yPercents = []
for y in yInts:
    yPercents.append(float(y)/float(yInts.sum()))
plt.bar(edgepoints,yPercents,width=1.0,facecolor=flatColorDBlue,edgecolor=flatColorDBlue)
plt.xlabel('Keyspace Position')
plt.ylabel('Keyspace Fullness')
plt.title('Curve Fitting of Keyspace Distribution')
yInts,edges = np.histogram(positions,bins=50)
edgepoints = []
for i in range(len(edges)-1):
    edgepoints.append(int((edges[i] + edges[1+i])/2))
yPercents = []
for y in yInts:
    yPercents.append(float(y)/float(yInts.sum()))
plt.plot(edgepoints,yPercents)
ax = plt.gca()
ax.set_xlim([0,k])
plt.legend(loc='best',fancybox=True, framealpha=0.8)
plt.savefig('histogram.pdf',format='pdf')
plt.show()


