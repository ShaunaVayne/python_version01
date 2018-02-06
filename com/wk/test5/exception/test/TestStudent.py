# 测试类
import unittest

from com.wk.test5.exception.test.Student import Student

class TestStudent(unittest.TestCase) :
    def test_80_100(self):
        s1 = Student('wangkun',75)
        s2 = Student('vayne', 80)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(),'A')
    def test_invalid(self):
        s1 = Student('xiaoming', -1)
        s2 = Student('xiaohong', 102)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()
if __name__ == '__main__':
    unittest.main()