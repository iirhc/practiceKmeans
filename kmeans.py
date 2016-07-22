import copy
import math
import random
import os
import matplotlib.pyplot as plt

def calcDistance(a, b):
    diam = len(a)
    d = 0
    for i in range(diam):
        d += (a[i]-b[i])**2
    return math.sqrt(d)

def calcCenter(s):
    num = len(s)
    diam = len(s[0])-1
    res = []
    for i in range(diam):
        t = 0
        for n in range(num):
            a = s[n][i]
            if type(a) == type(1.1):
                t += a
        res.append(t/num)
    return res

name = 'iris.data.txt'
iris = []
for line in open(name, 'r', encoding='UTF-8'):
    iris.append([str.strip() for str in line.split(',')])
# change data from string to float
for i in range(len(iris)):
    for j in range(4):
        iris[i][j] = float(iris[i][j])

k = 3 # group number
diam = 4 # dimension
points = []
lastpoints = []
groups = []
newgroups = []
distances = [] # distance of the point to each group center
# choose random k numbers as start points
while len(points) < k:
    rn = random.randint(0, len(iris))
    if rn not in points:
        points.append(rn)
# initialize
for p in range(k):
    points[p] = iris[points[p]][:4]
    print(points[p]) # show initail group center points
    groups.append([])
    distances.append(0)
lastpoints = copy.deepcopy(points)
newgroups = copy.deepcopy(groups)
groups[0] = copy.deepcopy(iris)
count = 0

# iterate at most 300 times
for i in range(300):
    # cluster
    for groupNo in range(k):
        for data in groups[groupNo]:
            for centerNo in range(k):
                distances[centerNo] = calcDistance(data[:4], points[centerNo])
            classify = distances.index(min(distances))
            newgroups[classify].append(data)
    groups = copy.deepcopy(newgroups)
    for g in range(k):
        newgroups[g] = []
    # recalculate group center points
    for groupNo in range(k):
        points[groupNo] = calcCenter(groups[groupNo])
    # calculate how much center points change
    diff = 0
    for groupNo in range(k):
        diff += calcDistance(points[groupNo], lastpoints[groupNo])
    print(diff) # show total group center points moving distance every iteration
    if diff < 0.000000000001:
        break
    lastpoints = copy.deepcopy(points)
    # count times of iterating
    count += 1

# show final group center points
for j in range(k):
    print(points[j])
# show how many data in each gruops
for j in range(k):
    print(len(groups[j]))
# show times of iterating
print(count)
print("=============")

# initialize pyplot
todraw = []
for g in range(k):
    todraw.append([])
xy = [[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]
color = ['r', 'g', 'b']
x_min, x_max = 0, 10
y_min, y_max = 0, 5
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())

# draw with scatter
for f in range(len(xy)):
    plt.figure(f+1, figsize=(8, 6))
    for g in range(k):
        todraw[g] = []
    for groupNo in range(k):
        for data in groups[groupNo]:
            todraw[groupNo].append([data[xy[f][0]-1], data[xy[f][1]-1]])
    for groupNo in range(k):
        for drawdata in todraw[groupNo]:
            plt.scatter(drawdata[0], drawdata[1], c = color[groupNo])
plt.show()
