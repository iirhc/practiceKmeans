import random
import math
import os

name = 'iris.data.txt'
iris = []
for line in open(name, 'r', encoding='UTF-8'):
    iris.append([str.strip() for str in line.split(',')])

k = 3
diam = 4
points = []
groups = []
newgroups = []
distances = [] #distance of the point to each group center
for p in range(k):
    points.append(iris[random.randint(0,len(iris))][:-1])
    groups.append([])
    newgroups.append([])
    print(points[p])
    distances.append(0.0)
#os.system("pause")

# this should be first time clusters
groups[0] = iris

for i in range(10):
    for groupNo in range(k):
        for dataNo in range(len(groups[groupNo])):
            distances[groupNo] = 0
            for centerNo in range(k):
                for diamNo in range(diam):
                    distances[centerNo] += (float(groups[groupNo][dataNo][diamNo])-float(points[centerNo][diamNo]))**2
                distances[centerNo] = math.sqrt(distances[centerNo])
            classify = distances.index(min(distances))
            newgroups[classify].append(groups[groupNo][dataNo])
    groups = newgroups
    for groupNo in range(k):
        for diamNo in range(diam):
            total = 0
            for dataNo in range(len(newgroups[groupNo])):
                total += float(newgroups[groupNo][dataNo][diamNo])
            avg = total/len(newgroups[groupNo])
            points[groupNo][diamNo] = avg
    newgroups = [[],[],[]]
    for j in range(k):
        print(points[j])
    for j in range(k):
        print(len(groups[j]))
    print("=============")
"""
for itemNum in range(len(iris)):
    for groupNum in range(k):
        distances[groupNum] = 0
        for diamNum in range(diam):
            distances[groupNum] += (float(iris[itemNum][diamNum]) - points[groupNum][diamNum])**2
        distances[groupNum] = math.sqrt(distances[groupNum])
    groups[distances.index(min(distances))].append(iris[itemNum])
"""
"""
for j in range(k):
    print(len(groups[j]))
"""
