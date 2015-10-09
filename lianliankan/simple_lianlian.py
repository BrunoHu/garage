# coding:utf-8
import random

length = 4
width = 4


def set_up_random_matrix(length, width):
    matrix = []
    random_list = set_random_list(length * width / 2)
    for i in range(width):
        line = []
        for j in range(length):
            line.append([i + 1, j + 1, random_list[i * length + j]])
        matrix.append(line)
    return matrix


def expand_matrix(matrix):
    width = len(matrix)
    length = len(matrix[0])

    new_matrix = []
    # add the first expand line
    new_line = []
    for i in range(length + 2):
        new_line.append([0, i, -1])
    new_matrix.append(new_line)

    for i in range(width):
        new_line = []
        new_line.append([i + 1, 0, -1])
        for j in range(length):
            new_line.append(matrix[i][j])
        new_line.append([i + 1, length + 1, -1])
        new_matrix.append(new_line)

    new_line = []
    for i in range(length + 2):
        new_line.append([width + 1, i, -1])
    new_matrix.append(new_line)
    return new_matrix


def show(matrix):
    width = len(matrix)
    length = len(matrix[0])
    for i in range(width):
        for j in range(length):
            print str(matrix[i][j][2]) + '\t',
        print '\n'


def is_linked(matrix, flag):
    position = []
    for i in matrix:
        for j in i:
            if j[2] == flag:
                position.append([j[0], j[1]])
    node_in_depth_0 =[]
    node_in_depth_0.extend(search_with_direction(0, matrix, position[0], flag))
    print node_in_depth_0
    if  ('ok' in node_in_depth_0):
        return True, position
    # else:
    #     for i in node_in_depth_0:
    #         if (search_with_direction(3-i[1], matrix, i[0]) == 'ok'):
    #             return True,position
    #         else:
    #             for j in search_with_direction(3-i[1], matrix, i[0]):
    #                 if(search_with_direction(3-j[1], matrix, j[0]) == 'ok'):
    #                     return True,position
    node_in_depth_1 = []
    for i in node_in_depth_0:
        temp = search_with_direction(i[1], matrix, i[0], flag)
        node_in_depth_1.extend(temp)
    if ('ok' in node_in_depth_1):
        return True, position
    print node_in_depth_1
    node_in_depth_2 = []

    for j in node_in_depth_1:
        node_in_depth_2.extend(search_with_direction(j[1], matrix, j[0], flag))
    if ('ok' in node_in_depth_2):
        return True, position
    print node_in_depth_2
    return False, position


def search_with_direction(direction, matrix, position, flag):
    x = position[0]
    y = position[1]

    if direction == 0:
        line_0 = []
        if search_with_direction(1, matrix, position, flag) == 'ok':
            return ['ok']
        else:
            line_0.extend(search_with_direction(1, matrix, position, flag))

        if search_with_direction(2, matrix, position, flag) == 'ok':
            return ['ok']
        else:
            line_0.extend(search_with_direction(2, matrix, position, flag))
        return line_0

    if direction == 1:  # 东西方向
        line_1 = []
        i = 1
        while (y + i < len(matrix[0])):
            if matrix[x][y + i][2] == flag:
                return ['ok']
            elif (matrix[x][y + i][2] > 0):
                break
            else:
                line_1.append([[x, y + i], 2])
            i = i + 1

        i = 1
        while (y - i >= 0):
            if matrix[x][y - i][2] == flag:
                return ['ok']
            elif (matrix[x][y - i][2] > 0):
                break
            else:
                line_1.append([[x, y - i], 2])
            i = i + 1
        return line_1

    if direction == 2:  # 南北方向
        line_2 = []
        i = 1
        while (x + i < len(matrix)):
            if matrix[x + i][y][2] == flag:
                return ['ok']
            elif (matrix[x + i][y][2] > 0):
                break
            else:
                line_2.append([[x + i, y], 1])
            i = i + 1

        i = 1
        while (x - i >= 0):
            if matrix[x - i][y][2] == flag:
                return ['ok']
            elif (matrix[x - i][y][2] > 0):
                break
            else:
                line_2.append([[x - i, y], 1])
            i = i + 1
        return line_2


def vanish(flag, matrix):
    for i in matrix:
        for j in i:
            if (j[2] == flag):
                j[2] = 0
    return matrix


def set_random_list(n):
    random_list = [0] * n * 2
    for i in range(n):

        position = random.randint(0, n * 2 - 1)
        while (random_list[position] != 0): position = (position + 1) % (n * 2)
        random_list[position] = i + 1

        position = random.randint(0, n * 2 - 1)
        while (random_list[position] != 0): position = (position + 1) % (n * 2)
        random_list[position] = i + 1
    return random_list


matrix = set_up_random_matrix(length, width)
matrix = expand_matrix(matrix)
# for i in range(len(matrix)):
#     print matrix[i]
show(matrix)
while True:
    v = input('vanish:')
    matrix = vanish(v, matrix)
    show(matrix)
    flag = input('input flag:')
    position = []
    for k in matrix:
        for q in k:
            if q[2] == flag:
                position = [q[0], q[1]]
                break
    print is_linked(matrix, flag)
