import unittest

from partb import sayposition

class TestDayOne(unittest.TestCase):

    def test_one(self):
        actual = sayposition(")")
        expected = 1
        self.assertEqual(actual, expected)

    def test_two(self):
        actual = sayposition("()())")
        expected = 5
        self.assertEqual(actual, expected)
    
    def test_four(self):
        actual = sayposition("((((())))))")
        expected = 11
        self.assertEqual(actual, expected)    
             
if __name__ == '__main__':
    unittest.main()