# encoding:utf-8
from kmeans import *
import matplotlib.pyplot as plt


#just check algorithm and give a visiual picture

def random_color(k):
    # generate a random color code like '#225c6f'
    color_rgb_element = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    color = []
    for i in range(k):
        temp = '#'
        for j in range(6):
            temp = temp + color_rgb_element[random.randint(0,15)]
        color.append(temp)
    return color

def produce_random_point(demension=2,  limit_size=100):
    point = []
    for i in range(demension):
        point.append(random.randint(1,limit_size))
    return tuple(point)

def split_tuple(centers):
    result = [[],[]]
    for i in centers:
        result[0].append(i[0])
        result[1].append(i[1])
    return result

data = []
print '这是一个k-means算法及其实例程序，程序会创建随机点集并自动使用k-means算法进行聚类，并给出一个效果图（算法本身中并没有效果图的实现）'
print '请输入随机点的个数：'
n = input('>')
print '请输入划分集合的个数k：'
k = input('>')
for i in range(n):
    data.append(produce_random_point())
centers = kmeans(data, k)



centers[0] = split_tuple(centers[0])
for i in range(k):
    centers[1][i] = split_tuple(centers[1][i])


colors = random_color(k)
fig = plt.figure(figsize=(16,12), dpi=72, facecolor="white")
for i in range(k):
    plt.scatter(centers[1][i][0], centers[1][i][1], color=colors[i])
    plt.triplot(centers[1][i][0], centers[1][i][1], linewidth=0.1)
plt.scatter(centers[0][0], centers[0][1], marker='*', s=300)
plt.show()
