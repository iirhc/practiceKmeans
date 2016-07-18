name = 'iris.data.txt'
iris = []
for line in open(name, 'r', encoding='UTF-8'):
    iris.append([str.strip() for str in line.split(',')])
print(iris)
