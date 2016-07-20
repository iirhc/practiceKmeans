import random
import math
import os
import copy

name = 'iris.data.txt'
iris = []
for line in open(name, 'r', encoding='UTF-8'):
    iris.append([str.strip() for str in line.split(',')])

k = 3
diam = 4
points = []
lastpoints = []
groups = []
newgroups = []
distances = [] #distance of the point to each group center
for p in range(k):
    points.append(iris[random.randint(0,len(iris))][:-1])
    lastpoints.append([])
    for d in range(diam):
        lastpoints[p].append(0)
    groups.append([])
    newgroups.append([])
    print(points[p])
    distances.append(0.0)

groups[0] = iris
count = 0

for i in range(300):
    for groupNo in range(k):
        for dataNo in range(len(groups[groupNo])):
            for centerNo in range(k):
                distances[centerNo] = 0
                for diamNo in range(diam):
                    distances[centerNo] += (float(groups[groupNo][dataNo][diamNo])-float(points[centerNo][diamNo]))**2
                distances[centerNo] = math.sqrt(distances[centerNo])
            #print(distances)
            #os.system("pause")
            classify = distances.index(min(distances))
            newgroups[classify].append(groups[groupNo][dataNo])
    groups = newgroups
    for groupNo in range(k):
        for diamNo in range(diam):
            total = 0
            for dataNo in range(len(newgroups[groupNo])):
                total += float(newgroups[groupNo][dataNo][diamNo])
            #if len(newgroups[groupNo])!=0:
            points[groupNo][diamNo] = total/len(newgroups[groupNo])
    diff = 0
    for groupNo in range(k):
        for diamNo in range(diam):
            diff += abs(float(points[groupNo][diamNo])-float(lastpoints[groupNo][diamNo]))
    newgroups = [[],[],[]]
    print(diff)
    if diff < 0.000000000001:
        break
    lastpoints = copy.deepcopy(points)
    count+=1

for j in range(k):
    print(points[j])
for j in range(k):
    print(len(groups[j]))

print(count)
print("=============")
