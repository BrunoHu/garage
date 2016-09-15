# coding:utf-8
import numpy as np
import copy
import random
import traceback
import math


class Matrix(object):
    def __init__(self, matrix=None, size=4, start_unit=3, data=None, flag=0):
        # self.ava_move = []
        self.score = None
        self.empty_list = set()
        self.start_unit = start_unit
        self.size = size
        self.flag = flag       # 0->min 1->max
        self.from_direction = None
        self.ava_move = set()
        self.dead = False
        if data is not None:
            self.data = np.copy(data)
            self._refresh_empty_list()
            self.size = len(data)
            self.check_move()
        elif matrix is not None:
            self.data = np.copy(matrix.data)
            self.empty_list = copy.copy(matrix.empty_list)
            self.size = matrix.size
            self.start_unit = matrix.start_unit
            self.flag = matrix.flag
            self.ava_move = copy.copy(matrix.ava_move)
        else:
            self._gen_data()
            self.check_move()
            # self.check_avaliable_move()

    def _gen_data(self):
        self.data = np.zeros([self.size, self.size], dtype=int)
        map(
            lambda x: self.empty_list.add(x),
            [(i, j) for i in range(self.size) for j in range(self.size)]
        )
        sample = random.sample(self.empty_list, self.start_unit)
        for item in sample:
            self.data[item] = 1
            self.empty_list.remove(item)

    def get_score(self):
        if self.dead:
            return 1000000000
        score_sum = 0
        full = 0
        # for i in range(self.size):
        #     for j in range(self.size):
        #         result = self._compute_unit_score(i, j)
        #         score_sum += result
        #         if self.data[i, j] > 0:
        #             full += 1
        # score_sum += full ** 3

        for i in range(self.size):
            score_sum += self._line_score(self.data[i, :])
            score_sum += self._line_score(self.data[:, i])
            for j in range(self.size):
                result = 0
                # result += self._compute_unit_score(i, j)
                result += self._compute_unit_score2(i, j)
                score_sum += result
                if self.data[i, j] > 0:
                    full += 1
        # for i in range(self.size):
        #     score_sum += self._line_score(self.data[:, i])
        #     score_sum += self._line_score(self.data[i, :])
        score_sum += full**2
        return score_sum

    def _compute_unit_score(self, i, j):
        score = 0
        value = self.data[i, j]
        if i - 1 >= 0 and j - 1 >= 0:
            score += abs(value - self.data[i - 1, j - 1])
        if i - 1 >= 0 and j + 1 <= 3:
            score += abs(value - self.data[i - 1, j + 1])
        if i + 1 <= 3 and j - 1 >= 0:
            score += abs(value - self.data[i + 1, j - 1])
        if i + 1 <= 3 and j + 1 <= 3:
            score += abs(value - self.data[i + 1, j + 1])
        return score

    def _compute_unit_score2(self, i, j):
        index = 0
        value = self.data[i, j]
        bundary = (0, 3)
        if i not in bundary:
            index += 1
        if j not in bundary:
            index += 1
        # score = self._compute_unit_score(i, j)
        return value ** index

    @staticmethod
    def _line_score(line):
        l1 = sorted(line)
        l2 = sorted(line, reverse=True)
        score1 = sum([abs(a - b)**2 for a, b in zip(line, l1)])
        score2 = sum([abs(a - b)**2 for a, b in zip(line, l2)])
        return min(score1, score2) * np.mean(line)

    def push(self, direction):
        """
        0 -> move up
        1 -> move right
        2 -> move down
        3 -> move left
        """
        for i in range(self.size):
            if direction == 0:
                self.data[:, i] = self._line_push(self.data[:, i], 1)
            if direction == 1:
                self.data[i, :] = self._line_push(self.data[i, :], 0)
            if direction == 2:
                self.data[:, i] = self._line_push(self.data[:, i], 0)
            if direction == 3:
                self.data[i, :] = self._line_push(self.data[i, :], 1)
        self._refresh_empty_list()
        self.flag = 1

    def _line_push(self, line, direction):
        """0 -> right    1 -> left"""
        if direction == 1:
            zip_list = [x for x in line if x != 0]
            for i in range(len(zip_list) - 1):
                if zip_list[i] == zip_list[i + 1]:
                    zip_list[i] += 1
                    zip_list[i + 1] = 0
            result = [x for x in zip_list if x != 0]
            result.extend([0] * (len(line) - len(result)))
            return np.array(result)
        if direction == 0:
            return self._line_push(line[::-1], 1)[::-1]

    def _refresh_empty_list(self):
        self.empty_list = set()
        map(
            lambda pair: self.empty_list.add(pair),
            [(i, j) for i in range(self.size) for j in range(self.size) if self.data[(i, j)] == 0]
        )

    def _gen_random(self, pair=None, number=None):
        if number is None:
            p = random.randint(1, 4)
            if p == 4:
                number = 2
            else:
                number = 1
        if pair is None:
            pair = random.sample(self.empty_list, 1)[0]
            self.data[pair] = number
            self.empty_list.remove(pair)
        elif len(self.empty_list) != 0:
            self.data[pair] = number
            self.empty_list.remove(pair)

        self.flag = 0

        return self.check_move()
        # self.check_avaliable_move()

        # return self._check_alive()

    # def _check_alive(self):
    #     if len(self.empty_list) > 0:
    #         return True
    #     for i in range(self.size):
    #         for j in range(self.size):
    #             if self._alive_score(i, j) != 2:
    #                 return True
    #     return False


    def check_move(self):
        move = set()
        for i in range(self.size):
            for j in range(self.size):
                if i == self.size - 1 and j == self.size - 1:
                    pass
                elif i == self.size - 1:
                    self._check_right(i, j, move)
                elif j == self.size - 1:
                    self._check_down(i, j, move)
                else:
                    self._check_right(i, j, move)
                    self._check_down(i, j, move)
        self.ava_move = move
        if len(move) == 0:
            self.dead = True
            return 0
        else:
            return 1

    def _check_right(self, i, j, move_set):
        left_value = self.data[i, j]
        right_value = self.data[i, j + 1]
        if left_value == 0 and right_value > 0:
            move_set.add(3)
        if left_value > 0 and right_value == 0:
            move_set.add(1)
        if left_value == right_value and left_value > 0:
            move_set.add(1)
            move_set.add(3)

    def _check_down(self, i, j, move_set):
        up_value = self.data[i, j]
        down_value = self.data[i + 1, j]
        if up_value == 0 and down_value > 0:
            move_set.add(0)
        if up_value > 0 and down_value == 0:
            move_set.add(2)
        if up_value == down_value and up_value > 0:
            move_set.add(0)
            move_set.add(2)

    # def check_avaliable_move(self):
    #     ava = []
    #     new_matrix = Matrix(self)
    #     new_matrix.push(0)
    #     if not (self.data == new_matrix.data).all():
    #         ava.append(0)
    #     new_matrix = Matrix(self)
    #     new_matrix.push(1)
    #     if not (self.data == new_matrix.data).all():
    #         ava.append(1)
    #     new_matrix = Matrix(self)
    #     new_matrix.push(2)
    #     if not (self.data == new_matrix.data).all():
    #         ava.append(2)
    #     new_matrix = Matrix(self)
    #     new_matrix.push(3)
    #     if not (self.data == new_matrix.data).all():
    #         ava.append(3)
    #     self.ava_move = ava

    # def _alive_score(self, i, j):
    #     score = 0
    #     if i == self.size - 1 and j == self.size - 1:
    #         score = 2
    #     elif i == self.size - 1:
    #         score += 1
    #         if self.data[i, j] != self.data[i, j + 1]:
    #             score += 1
    #     elif j == self.size - 1:
    #         score += 1
    #         if self.data[i, j] != self.data[i + 1, j]:
    #             score += 1
    #     else:
    #         if self.data[i, j] != self.data[i + 1, j]:
    #             score += 1
    #         if self.data[i, j] != self.data[i, j + 1]:
    #             score += 1
    #     return score


    def __str__(self):
        # return np.exp2(self.data).__str__()
        s = []
        for i in range(self.size):
            for j in range(self.size):
                value = self.data[i, j]
                if value == 0:
                    s.append('*\t')
                else:
                    s.append('%s\t' % 2**value)
            s.append('\n')
        return ''.join(s)

    def __repr__(self):
        return self.info()
        # return np.exp2(self.data).__str__()

        # for i in range(self.size):
        #     for j in range(self.size):
        #         value = self.data[i, j]
        #         if value == 0:
        #             print ''.center(8)
        #         else:
        #             print '%s'.center(8) % 2**value

    def info(self):
        s = ("empty list: %s\nscore: %s\nava move: %s\nflag: %s\ndirection: %s\nmatrix data: \n%s"
         % (self.empty_list, self.score, self.ava_move, self.flag, self.from_direction, self.__str__()))
        return s

    def _child(self):
        """generator for DFS"""
        if self.flag == 0:
            # for direction in self.ava_move:
            for direction in self.ava_move:
                new_matrix = Matrix(self)
                new_matrix.push(direction)
                new_matrix.father = self
                new_matrix.from_direction = direction
                yield new_matrix
        if self.flag == 1:
            for pair in self.empty_list:
                new_matrix = Matrix(self)
                new_matrix._gen_random(pair, 1)
                new_matrix.father = self
                yield new_matrix
                new_matrix = Matrix(self)
                new_matrix._gen_random(pair, 2)
                new_matrix.father = self
                yield new_matrix


def evaluate_direction_with_log(node, layer=2):
    # global pruning_time
    print "###### now is layer %s ######" % layer
    print node.info()
    print "tmp score %s" % node.get_score()

    if layer == 0:
        print "###### leaf node, trace back ######"
        print "####### leaf node score %s ######" % node.get_score()
        return node.get_score()

    if node.dead:
        print "###### dead matrix ######"
        return 1000000000

    else:
        for child in node._child():
            score = evaluate_direction_with_log(child, layer=layer - 1)
            print "** get score %s from child **" % score
            print "** now the father score is %s **" % node.score
            if score == -1:
                continue
            if node.score is None:
                node.score = score
                print "** father node update to %s **" % node.score
            elif node.flag == 0 and score < node.score:
                node.score = score
                print "** father node update to %s **" % node.score
            elif node.flag == 1 and score > node.score:
                node.score = score
                print "** father node update to %s **" % node.score
            elif node.flag not in (0, 1):
                raise
            if check_need_pruning(node):
                # pruning_time += 1
                print "######  pruning now, trace back ######"
                print "self score: %s" % node.score
                print "father score: %s" % node.father.score
                return -1
        print "** finish a loop return score is %s **" % node.score
        return node.score


def evaluate_direction(node, layer=2):
    if layer == 0:
        return node.get_score()

    if node.dead:
        return 1000000000

    else:
        for child in node._child():
            score = evaluate_direction(child, layer=layer - 1)
            if score == -1:
                continue
            if node.score is None:
                node.score = score
            elif node.flag == 0 and score < node.score:
                node.score = score
            elif node.flag == 1 and score > node.score:
                node.score = score
            elif node.flag not in (0, 1):
                raise
            if check_need_pruning(node):
                return -1
        return node.score


def check_need_pruning(node):
    if node.score is None:
        return False
    if node.father is None:
        return False
    if node.father.score is None:
        return False

    if node.flag == 0 and node.score <= node.father.score:
        return True

    if node.flag == 1 and node.score >= node.father.score:
        return True

    if node.flag not in (0, 1):
        raise
    return False


def choose_direction(node, depth=2, has_log=False):
    # global depth_sum
    # depth_sum += depth
    best_direction = -1
    min_score = 10000000000000
    for child in node._child():
        if has_log:
            score = evaluate_direction_with_log(child, depth * 2 - 1)
        else:
            score = evaluate_direction(child, depth * 2 - 1)
        if score < min_score:
            min_score = score
            best_direction = child.from_direction


    return best_direction, min_score


# def choose_direction(node, depth=10, turns=500):
#     best_direction = -1
#     min_score = 1000000000000000
#     for child in node._child():
#         score = evaluate_direction_by_mentcaro(child, depth=5, turns=2000)
#         if score < min_score:
#             min_score = score
#             best_direction = child.from_direction
#     return best_direction, min_score




def evaluate_direction_by_mentcaro(node, depth=100, turns=100):
    score = 0
    for i in xrange(turns):
        new_node = Matrix(node)
        for j in range(depth):
            new_node._gen_random()
            if not new_node.check_move():
                score += 1000000000
                break
            direction = random.sample(new_node.ava_move, 1)[0]
            new_node.push(direction)
        score += node.get_score()
    return score * 1.0 / turns




direction_dic = {
        0: "up",
        1: "right",
        2: "down",
        3: "left"
    }


def run_ai():
    n = Matrix()
    print "start"
    print n.info()
    turn = 1
    # while True:
    #     print "*" * 30
    #     if n.flag == 0:
    #         if not n._check_alive():
    #             break
    #         print "#### turn %s ####" % turn
    #         depth = int(math.sqrt(n.size**2 + 2 - len(n.empty_list)))
    #         print "search depth %s" % depth
    #         try:
    #             direction, min_score = choose_direction(n, depth)
    #         except Exception:
    #             print traceback.format_exc()
    #             raise
            # print "#### predict direction is %s ####" % direction_dic[direction]
            # print "#### best score is %s ####" % min_score
            # n.push(direction)
            # print n.info()
    #         turn += 1
    #     else:
    #         if len(n.empty_list) == 0:
    #             break
    #         print "#### random gen a unit ####"
    #         n._gen_random()
    #         print n.info()
    while not n.dead:
        print "#### turn %s ####" % turn
        turn += 1
        print "*"*30
        depth = int(math.sqrt(n.size**2 + 2 - len(n.empty_list)))
        # depth = 2
        # if len(n.empty_list) < 5:
        #     depth = 3
        print "search depth %s" % depth
        try:
            direction, min_score = choose_direction(n, depth)
        except Exception:
            print traceback.format_exc()
            raise
        print "#### predict direction is %s ####" % direction_dic[direction]
        print "#### best score is %s ####" % min_score
        n.push(direction)
        print n.info()
        print "#### random gen a unit ####"
        n._gen_random()
        print n.info()
    print "done"


if __name__ == "__main__":
    # global depth_sum
    # global pruning_time

##  test direction push-----------------
    # m = np.array([[1,1,1,1], [1,2,3,4], [1,1,2,3], [6,7,8,9]])
    # test = Matrix(data=m)
    # test.info()
    # print "*"*20
    # test.push(0)
    # test.info()
    # print "*"*20
    # test.push(1)
    # test.info()
    # print "*"*20
    # test.push(2)
    # test.info()
    # print "*"*20
    # test.push(3)
    # test.info()
    # test.push(3)
    # test.info()
####------------------------


### test alive--------

    # m = np.array([[1,2,3,4], [4,3,2,1], [1,2,3,4], [4,3,2,1]])
    # test = Matrix(data=m)
    # print test.info()
    # print test._check_alive()
    # print test.get_score()

    # n = np.array([[1,1,1,1], [1,2,3,4], [1,1,2,3], [6,7,8,9]])
    # test2 = Matrix(data=n)
    # print test2.info()
    # print test2._check_alive()
    # print test2.__str__()


### check _child
    # n = np.array([[1,1,1,1], [1,2,3,4], [0,0,0,0], [2,2,2,2]])
    # test = Matrix(data=n)
    # print test.info()
    # for child in test._child():
    #     print child.info()

    # print "*"*30

    # test2 = Matrix(data=n, flag=1)
    # print test2.info()
    # for child in test2._child():
    #     print child.info()


### start --------

    # n = np.array([[1,1,1,1], [0,0,0,0], [0,0,0,0], [0,0,0,0]])
    # test = Matrix(data=n)
    # print "#### origin matrix  ####"
    # print test.info()
    # print "###########"
    # print choose_direction(test)

    # n = np.array([[1,2,3,4], [4,3,2,1], [1,2,3,4], [4,3,0,3]])
    # test = Matrix(data=n)
    # print "#### origin matrix  ####"
    # print test.info()
    # print "###########"
    # print choose_direction(test)


# check ---------
    # n = np.array([[3,1,4,3], [4,6,5,2], [6,7,4,1], [11,5,3,0]])
    # m = Matrix(data=n)
    # print m.info()
    # # print choose_direction(m, 1, has_log=True)
    # for i in range(1,6):
    #     print i
    #     print choose_direction(m, i)
    run_ai()