# coding:utf-8
import copy

path = '/home/arnold-hu/garage/soduku/very_hard.txt'
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

invalid = []



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
                invalid.append(grids[count])
                count += 1
            elif i != '\n' and i != ' ':
                count += 1
            if count >= 81:
                break

def init_sudo(units):
    for i in grids:
        units[i] = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    invalid = []


def simple_vanish(units, invalid):
    flag = True
    while flag:
        flag = False
        for i in grids:
            if i not in invalid:
                for j in conter_units[i]:
                    if j in invalid:
                        if units[j][0] in units[i]:
                            units[i].remove(units[j][0])
                            flag = True
                            if len(units[i]) == 1:
                                invalid.append(i)
                                break

def check(units, invalid):
    for i in invalid:
        for j in conter_units[i]:
            if j in invalid:
                if units[i][0] == units[j][0]:
                    print 'False: '+ i + ' links ' + j
                    return False
    return True

def get_shortest_ava_unit(units, invalid):
    count = 100
    for i in grids:
        if i not in invalid and len(units[i]) < count:
            count = len(units[i])
            short_u = i
    return short_u




def deep_vanish(units, invalid):
    global result_units
    invalid_copy = invalid[:]
    units_copy = copy.deepcopy(units)
    tag = get_shortest_ava_unit(units_copy, invalid_copy)
    invalid_copy.append(tag)
    tags = units_copy[tag][:]
    for ava in tags:
        units_copy[tag] = [ava]
        simple_vanish(units_copy, invalid_copy)
        if not check(units_copy, invalid_copy):
            units_copy = copy.copy(units)
            invalid_copy = invalid[:]
            invalid_copy.append(tag)
            continue
        else:
            if len(invalid_copy) == 81:
                result_units = units_copy
                return True
            else:
                result = deep_vanish(units_copy, invalid_copy)
                if result:
                    return True
                else:
                    units_copy = copy.copy(units)
                    invalid_copy = invalid[:]
                    invalid_copy.append(tag)
                    continue
    return False

if __name__ == "__main__":
    init_sudo(units)
    test = units['a1']
    test_conter = conter_units['a1']
    init_sudo_with_file(units)
    display_sudo(units)

    simple_vanish(units, invalid)
    print '*'*20 + 'simple_vanish' + '*'*20
    display_sudo(units)
    print '*'*20 + 'deep_vanish' + '*'*20
    if deep_vanish(units, invalid):
        display_sudo(result_units)
    else:
        print 'False'
