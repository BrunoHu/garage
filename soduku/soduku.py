

class Node(object):
    def __init__(self, x, y, group=0, possible_list=[1,2,3,4,5,6,7,8,9]):
        self.x = x
        self.y = y
        self.group = group
        self.possible_list = possible_list[:]

    def vanish(self, v):
        if v in self.possible_list:
            self.possible_list.remove(v)

    def get_valid_value(self):
        if len(self.possible_list) == 1:
            return self.possible_list[0]
        else:
            return 0

def init_soduku(path):
    soduku = [[],[],[],[],[],[],[],[],[]]
    account = 0
    with open(path, 'r') as f:
        data = f.read()
        for i in data:
            if i == '0':
                soduku[account/9].append(Node(account/9, account%9, group=(account/27)*3+(account%9)/3))
                account = account + 1
            elif i >= '1' and i <= '9':
                soduku[account/9].append(Node(account/9, account%9,group=(account/27)*3+(account%9)/3, possible_list=[int(i)]))
                account = account + 1
        if account < 81:
            return 'error: numbers less than 9*9'
        if account > 81:
            return 'error: numbers more than 9*9'
        else:
            return soduku

def print_soduku(soduku):
    for i in soduku:
        for j in i:
            if j.get_valid_value() == 0:
                print ' ' + ' ',
            else:
                print ' ' + str(j.get_valid_value()),

            if (j.y % 3 == 2 and j.y != 8):
                print '|',
        print '\n'
        if (i[0].x % 3 == 2 and i[0].x < 8):
             print '---------*----------*----------'

def simple_process(soduku):
    pass

def vanish_cross(soduku, x, y):
    center = soduku[x][y]
    data = center.get_valid_value()
    group = center.group
    for i in soduku:
        for j in i:
            if j.x != x and j.y != y:
                if j.x == x:
                    j.vanish(data)
                elif j.y == y:
                    j.vanish(data)
                elif j.group == group:
                    j.vanish(data)









