# coding:utf-8
import copy

path = '/home/arnold-hu/garage/soduku/hard.txt'
#   initiate the structure of sudoku
rows = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
cols = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')
types = ('row', 'col', 'block')

units_belongs = {}
control_units = {}

grids = [x+y for x in cols for y in rows]  #  name list of units

# contstruct the dict of units' belong
for i in grids:
    # init
    units_belongs[i] = []
    p = grids.index(i)

    # determine the row
    r = p//9
    name = 'row' + str(r+1)
    units_belongs[i].append(name)

    # determine the col
    c = p % 9
    name = 'col' + str(c+1)
    units_belongs[i].append(name)

    #  determine the block
    b = r//3*3 + c//3
    name = 'block' + str(b+1)
    units_belongs[i].append(name)

#  construct the control units
control_parts_names = [x+y for x in types for y in rows]  #  temp name list to generate the control units

for i in control_parts_names: #init the sontrol units
    control_units[i] = []

for i in units_belongs:
    for j in units_belongs[i]:
        control_units[j].append(i)

# construct conter units
conter_units = {}

for i in grids:
    conter_units[i] = []
    for j in units_belongs[i]:
        conter_units[i].extend(control_units[j])
    conter_units[i] = set(conter_units[i])
    conter_units[i].remove(i)

# construct the units
units = {}

result_units ={}

for i in grids:
    units[i] = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

inavalable = []

def display_sudo(units):
    count = 1
    for i in grids:
        if len(units[i]) == 9:
            print '*'.center(6),
        else:
            print ''.join(units[i]).center(6),
            # print len(units[i]),' ',
        if count % 9 == 0:
            print '\n'
        count += 1


def init_sudo_with_file(units):
    with open(path, 'r') as f:
        data = f.read()
        count = 0
        for i in data:
            if i in rows:
                units[grids[count]] = [i]
                inavalable.append(grids[count])
                count += 1
            elif i != '\n' and i != ' ':
                count += 1
            if count >= 81:
                break

def init_sudo(units):
    for i in grids:
        units[i] = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    inavalable = []


def simple_vanish(units, inavalable):
    flag = True
    while flag:
        flag = False
        for i in grids:
            if i not in inavalable:
                for j in conter_units[i]:
                    if j in inavalable:
                        if units[j][0] in units[i]:
                            units[i].remove(units[j][0])
                            flag = True
                            if len(units[i]) == 1:
                                inavalable.append(i)
                                break

def check(units, inavalable):
    for i in inavalable:
        for j in conter_units[i]:
            if j in inavalable:
                if units[i][0] == units[j][0]:
                    print 'False: '+ i + ' links ' + j
                    return False
    return True

def get_shortest_ava_unit(units, inavalable):
    count = 100
    for i in grids:
        if i not in inavalable and len(units[i]) < count:
            count = len(units[i])
            short_u = i
    return short_u




def deep_vanish(units, inavalable):
    # tag = get_shortest_ava_unit(units)
    # tags = units[tag][:]
    # units_copy = copy.deepcopy(units)
    # inavalable.append(tag)
    # for ava in tags:
    #     units = copy.deepcopy(units_copy)
    #     units[tag] = [ava]
    #     simple_vanish(units)
    #     if not check(units):
    #         continue
    #     if len(inavalable) < 81:
    #         result = deep_vanish(units)
    #     else:
    #         return True
    #     if not result:
    #         continue
    #     else:
    #         return True
    # inavalable.remove(tag)
    # return False
    global result_units
    inavalable_copy = inavalable[:]
    units_copy = copy.deepcopy(units)
    tag = get_shortest_ava_unit(units_copy, inavalable_copy)
    inavalable_copy.append(tag)
    tags = units_copy[tag][:]
    for ava in tags:
        units_copy[tag] = [ava]
        simple_vanish(units_copy, inavalable_copy)
        # display_sudo(units_copy)
        if not check(units_copy, inavalable_copy):
            units_copy = copy.deepcopy(units)
            inavalable_copy = inavalable[:]
            inavalable_copy.append(tag)
            continue
        else:
            if len(inavalable_copy) == 81:
                result_units = copy.deepcopy(units_copy)
                return True
            else:
                result = deep_vanish(units_copy, inavalable_copy)
                if result:
                    return True
                else:
                    units_copy = copy.deepcopy(units)
                    inavalable_copy = inavalable[:]
                    inavalable_copy.append(tag)
                    continue
    return False

if __name__ == "__main__":
    init_sudo(units)
    test = units['a1']
    test_conter = conter_units['a1']
    init_sudo_with_file(units)
    display_sudo(units)

    simple_vanish(units, inavalable)
    print '*'*20 + 'simple_vanish' + '*'*20
    display_sudo(units)
    print '*'*20 + 'deep_vanish' + '*'*20
    if deep_vanish(units, inavalable):
        display_sudo(result_units)
    else:
        print 'False'
