import unittest
from Vitaliy_Test import First_Task

class TestFirstTask(unittest.TestCase):
    def test_first(self):
        solve=First_Task()
        result=solve.function(1,0.001)
        self.assertEqual(2.718, result)
    def test_second(self):
        solve=First_Task()
        result=solve.function(2,0.001)
        self.assertEqual(7.388, result)
    def test_third(self):
        solve=First_Task()
        result=solve.function(3,0.001)
        self.assertEqual(20.085, result)


if __name__ == '__main__':
    unittest.main()
