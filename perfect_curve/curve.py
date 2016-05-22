#! usr/bin/python
# coding=utf-8

import random

def line(dots):
    length = len(dots)
    line_x = [x[0] for x in dots]
    line_y = [x[1] for x in dots]
    tmp1 = sum([x*y for x in line_x for y in line_y])
    tmp2 = sum(line_x)*sum(line_y)/length
    tmp3 = sum([x**2 for x in line_x])
    tmp4 = sum(line_x)**2/n
    a = (tmp1 - tmp2)/(tmp3 - tmp4)
    b = sum(line_y)/length - a*(sum(line_x)/length)
    return a, b


def cut_pieces(dots, pieces):
    sort_dots = sorted(dots, key=lambda x:x[0])
    length = len(dots)
    average = length/pieces
    rest = length%pieces
    random_list = random.shuffle(([1]*rest).extend([0]*(length-rest)))
    nums = [x + average for x in random_list]
    result = []
    for i in nums:
        tmp=[]
        for j in range(i):
            tmp.append(sort_dots.pop())
        result.append(tmp)
    return result


def get_neighbur(dots, x, n):
    length　＝　len(dots)
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


