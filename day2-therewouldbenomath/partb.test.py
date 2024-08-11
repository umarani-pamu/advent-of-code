import unittest

from partb import calculate_ribbon

class TestDayOne(unittest.TestCase):

    def test_one(self):
        actual =calculate_ribbon(2,3,4)
        expected = 34
        self.assertEqual(actual, expected)

    def test_two(self):
        actual = calculate_ribbon(1,1,10)
        expected = 14
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()