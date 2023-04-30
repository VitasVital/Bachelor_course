import unittest
from timeit import Timer
from Vitaliy_Test import Second_Task

class TestSecondTask(unittest.TestCase):
    def test_a_fun(self):
        solve = Second_Task()
        result = solve.a_function("Пример простого текста")
        self.assertEqual("ремирП оготсорп атскет", result)
    def test_b_fun(self):
        solve = Second_Task()
        result = solve.b_function("Пример простого текста")
        self.assertEqual("ремирП оготсорп атскет", result)
    def xtest_c_fun(self):
        f = open("file1.txt", encoding="utf-8")
        text = f.read()
        f.close()
        solve = Second_Task()
        resulta = solve.a_function(text)
        resultb = solve.b_function(text)
        f.close()
        self.assertEqual(resulta, resultb)

    def test_time(self):
        f = open("file1.txt", encoding="utf-8")
        text = f.read()
        f.close()
        solve = Second_Task()
        t1 = Timer(lambda: solve.a_function(text))
        tt1=t1.timeit(number=1)
        print("Time a func ",tt1)
        t2 = Timer(lambda: solve.b_function(text))
        tt2=t2.timeit(number=1)
        print("Time b func",tt2)


if __name__ == '__main__':
    unittest.main()
