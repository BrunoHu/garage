#! usr/bin/python
# encoding:utf-8
import sys
import math
reload(sys)
sys.setdefaultencoding("utf-8")
import random
import copy
import matplotlib.pyplot as plt
def line(dots):
    length = len(dots)
    line_x = [x[0] for x in dots]
    line_y = [x[1] for x in dots]
    tmp1 = sum([x[0] * x[1] for x in zip(line_x, line_y)])
    print "tmp1 %s" % tmp1
    tmp2 = sum(line_x)*sum(line_y)/length
    print "tmp2 %s" % tmp2
    tmp3 = sum([x**2 for x in line_x])
    print "tmp3 %s" % tmp3
    tmp4 = sum(line_x)**2/length
    print "tmp4 %s" % tmp4
    print "sum y %s" % sum(line_y)
    print "sum x %s" % sum(line_x)
    a = (tmp1 - tmp2)/(tmp3 - tmp4)
    print "a is %s" % a
    b = sum(line_y)/length - a*(sum(line_x)/length)
    print "b is %s" % b
    return a, b


def cut_pieces(dots, pieces):
    dots_copy = copy.deepcopy(dots)
    length = len(dots_copy)
    average = length/pieces
    rest = length%pieces
    if rest != 0:
        random_list = [1]*rest
        random_list.extend([0]*(pieces-rest))
        random.shuffle(random_list)
    else:
        random_list = [0]*pieces
    nums = [x + average for x in random_list]
    result = []
    for i in nums:
        tmp=[]
        for j in range(i):
            tmp.append(dots_copy.pop())
        result.append(tmp)
    return result


def get_neighbur(dots, x, n):
    length = len(dots)
    for index, pairs in dots:
        if pairs[0]<= x and dots[index+1][0] > x:
            left = index
            right = index + 1
    for i in range(n):
        if left < 0:
            left = -999999
        if right >= length:
            right = -999999
        if abs(right - x) < abs(left - x):
            right -= 1
        else:
            left -= 1
    return left, right


def get_x_dots(dots, num):
    gap = abs(dots[0][0] - dots[-1][0])/num
    dots_x = [(gap/2+dots[0][0]+gap*i) for i in range(num)]
    return dots_x


def produce_random_point(limit_size=100):
    x = random.random()*100
    y = math.sin(x/10)*100 + random.random()*30
    # y = 2*x + random.random()*20
    return (x,y)

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


if __name__ == "__main__":
    print u'请输入随机点的个数：'
    n = int(input('>'))
    print u'请输入划分数量：'
    pieces = int(input('>'))

    dots= []
    for i in range(n):
        dots.append(produce_random_point())

    dots.sort(key=lambda x:x[0])
    dots_center = get_x_dots(dots, pieces)
    dots_sets = cut_pieces(dots, pieces)
    result = []
    for index, x in enumerate(reversed(dots_center)):
        a, b = line(dots_sets[index])
        y = a * x + b
        result.append((x,y))

    colors = random_color(pieces)
    fig = plt.figure(figsize=(16,12), dpi=72, facecolor="white")
    for i,dot_set in enumerate(dots_sets):
        for dot in dot_set:
            plt.scatter(dot[0], dot[1], s=10, color=colors[i])
    for i,dot in enumerate(result):
        plt.scatter(dot[0], dot[1], marker='*', s=600, color=colors[i])
    plt.show()