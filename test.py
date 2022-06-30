import unittest
from lolWL import testFuction


class test(unittest.TestCase):
    def test_function1(self):
        self.assertEqual(testFuction(0), 0)

#     def test_function2(self):
#         self.assertEqual(2 + 1, 3)
#         self.assertEqual(2.1 + 1.2, 3.3)

if __name__ == '__main__':
    unittest.main()
