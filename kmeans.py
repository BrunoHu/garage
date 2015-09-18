import numpy as np
import math
import random
import copy
import matplotlib.pyplot as plt

def distance(point1, point2, demension=2):
    sum = 0
    for i in range(demension):
        sum = sum + (point1[i] - point2[i])*(point1[i] - point2[i])
    return sum

def get_center(dataset):
    dem = len(dataset[0])
    point = [0.0] * dem
    for i in dataset:
        for j in range(dem):
            point[j] += i[j]
    for j in range(dem):
        point[j] = point[j] / len(dataset)
    return tuple(point)

def kmeans(dataset, k=2, demension=2):
    # initialization
    empty_set = []
    for i in range(k):
        empty_set.append([])
    # divide_set = copy.deepcopy(empty_set)
    centers = []
    residation = [10]*k
    temp = [0] * k
    for i in range(k):
        centers.append(dataset[i])
    # start rock'n roll
    while(sum(residation)>0.0001):
        divide_set = copy.deepcopy(empty_set)
        for i in dataset:
            # print "i:  " + str(i)
            for j in range(k):
                temp[j] = distance(i, centers[j], demension)
            # print "temp: " + str(temp)
            for j in range(k):
                if temp[j] == min(temp):
                    divide_set[j].append(i)
        # print 'divide_set' + str(divide_set)
        for j in range(k):
            residation[j] = distance(get_center(divide_set[j]), centers[j])
            centers[j] = copy.deepcopy(get_center(divide_set[j]))

    return [centers,divide_set]


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
# def compare(list1, list2, digit=5):
#     for i in range(len(list1)):
#         if distance(list1[i], list2[i]) > math.pow(0.1, digit):
#             return False
#     return True

#start test
data = []
for i in range(200):
    data.append(produce_random_point())
print data
k = 5
centers = kmeans(data, k)
print centers


color = np.random.rand(k)
centers[0] = split_tuple(centers[0])
for i in range(k):
    centers[1][i] = split_tuple(centers[1][i])




plt.figure(1)
for i in range(k):
    plt.scatter(centers[1][i][0], centers[1][i][1])
plt.scatter(centers[0][1], centers[0][1])
plt.show()
