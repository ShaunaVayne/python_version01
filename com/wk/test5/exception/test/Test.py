# 测试类
# 跟java的junit单元测试类似,test_xxx表示方法,鼠标放在哪里执行哪个方法, 对应java的@Test
import unittest

from com.wk.test5.exception.mydict import mydict

class TestDict(unittest.TestCase):
    def setUp(self):
        print('start')
    def test_init(self):
        d = mydict(a = 1, b = 'test');
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))
    def test_key(self):
        d = mydict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')
    def test_attr(self):
        d = mydict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')
    def test_keyError(self):
        d = mydict()
        with self.assertRaises(KeyError):
            value = d['empty']
    def test_attrerror(self):
        d = mydict()
        with self.assertRaises(AttributeError):
            value = d.empty
    def tearDown(self):
        print('end')
if __name__ == '__main__':
    unittest.main()

