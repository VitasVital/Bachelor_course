import unittest
import numpy as np
from Vitaliy_Test import Third_Task

class TestThirdTask(unittest.TestCase):
    def test_a_fun(self):
        matrix = np.array([[6, 7, 9, 8, 4, 2, 5, 3, 1],
                           [8, 3, 5, 1, 6, 7, 4, 2, 9],
                           [2, 1, 4, 9, 3, 5, 7, 6, 8],
                           [7, 6, 8, 5, 1, 3, 9, 4, 2],
                           [3, 4, 2, 6, 8, 9, 1, 5, 7],
                           [5, 9, 1, 7, 2, 4, 3, 8, 6],
                           [9, 8, 6, 3, 5, 1, 2, 7, 4],
                           [1, 2, 3, 4, 7, 8, 6, 9, 5],
                           [4, 5, 7, 2, 9, 6, 8, 1, 3]], int)
        solve = Third_Task()
        result = solve.function(matrix)
        self.assertEqual(True, result)
    def test_b_fun(self):
        matrix = np.array([[6, 7, 9, 8, 4, 2, 5, 3, 1],
                           [8, 3, 5, 1, 6, 7, 4, 2, 9],
                           [2, 1, 4, 9, 3, 5, 7, 6, 8],
                           [7, 6, 8, 5, 1, 3, 9, 4, 2],
                           [3, 4, 2, 6, 8, 9, 1, 5, 7],
                           [5, 9, 1, 7, 2, 4, 3, 8, 6],
                           [9, 8, 6, 3, 5, 1, 2, 7, 4],
                           [1, 2, 3, 4, 7, 8, 6, 9, 5],
                           [4, 5, 7, 3, 9, 6, 8, 1, 3]], int)
        solve = Third_Task()
        result = solve.function(matrix)
        self.assertEqual(False, result)


if __name__ == '__main__':
    unittest.main()
