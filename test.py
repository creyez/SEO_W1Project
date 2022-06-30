import unittest
from lolWL import testFuction


class TestFileName(unittest.TestCase):
    def test_function1(self):
        input1, input2 = testFuction()
        self.assertNotEqual(input1, None)

#     def test_function2(self):
#         self.assertEqual(2 + 1, 3)
#         self.assertEqual(2.1 + 1.2, 3.3)

if __name__ == '__main__':
    unittest.main()
