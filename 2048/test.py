# coding:utf-8


import unittest
import numpy as np
import ai_2048


class TestDict(unittest.TestCase):
    def setUp(self, **kw):
        self.data = np.array([[1, 2, 3, 4], [0, 0, 0, 0], [1, 2, 3, 4], [2, 0, 2, 0]])

    def test_init(self):
        init_matrx = ai_2048.Matrix()
        self.assertEquals(len(init_matrx.empty_list), 13)
        self.assertEquals(init_matrx.flag, 0)
        self.assertTrue(isinstance(init_matrx.empty_list, set))

        copy_data_matrix = ai_2048.Matrix(data=self.data)
        self.assertEquals(copy_data_matrix.empty_list, set([(1,0),(1,1),(1,2),(1,3),(3,1),(3,3)]))
        self.assertEquals(copy_data_matrix.flag, 0)
        self.assertTrue(isinstance(copy_data_matrix.empty_list, set))

        copy_matrix_matrix = ai_2048.Matrix(matrix=copy_data_matrix)
        self.assertEquals(copy_matrix_matrix.empty_list, set([(1,0),(1,1),(1,2),(1,3),(3,1),(3,3)]))
        self.assertEquals(copy_matrix_matrix.flag, 0)
        self.assertTrue(isinstance(copy_matrix_matrix.empty_list, set))


    def test_push(self):
        m = ai_2048.Matrix(data=self.data)
        m.push(0)
        expect_up = np.array([[2,3,4,5], [2,0,2,0], [0,0,0,0], [0,0,0,0]])
        self.assertTrue((m.data == expect_up).all())
        m.push(1)
        expect_right = np.array([[2,3,4,5], [0,0,0,3], [0,0,0,0], [0,0,0,0]])
        self.assertTrue((m.data == expect_right).all())
        m.push(2)
        expect_down = np.array([[0,0,0,0], [0,0,0,0], [0,0,0,5], [2,3,4,3]])
        self.assertTrue((m.data == expect_down).all())
        m.push(3)
        expect_left = np.array([[0,0,0,0], [0,0,0,0], [5,0,0,0], [2,3,4,3]])
        self.assertTrue((m.data == expect_left).all())


    def test_gen(self):
        m = ai_2048.Matrix(data=self.data, flag=1)
        m._gen_random_2(pair=(1,0))
        self.assertEqual(m.data[(1,0)], 1)

        m._gen_random_2()
        self.assertEqual(len(m.empty_list), 4)

    def test_flag(self):
        m = ai_2048.Matrix(data=self.data)
        self.assertEquals(m.flag, 0)

        m.push(0)
        self.assertEquals(m.flag, 1)

        m._gen_random_2()
        self.assertEquals(m.flag, 0)


if __name__ == '__main__':
    unittest.main()
