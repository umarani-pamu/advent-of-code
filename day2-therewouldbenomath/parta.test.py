import unittest

from partb import calculate_wrapping

class TestDayOne(unittest.TestCase):

    def test_one(self):
        actual =calculate_wrapping(2,3,4)
        expected = 58
        self.assertEqual(actual, expected)

    def test_two(self):
        actual = calculate_wrapping(1,1,10)
        expected = 43
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()