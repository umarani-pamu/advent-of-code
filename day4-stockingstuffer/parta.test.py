import unittest

from parta import find_adventcoin

class TestDayOne(unittest.TestCase):

    def test_one(self):
        actual =find_adventcoin("abcdef")
        expected = 609043
        self.assertEqual(actual, expected)

    def test_two(self):
        actual = find_adventcoin("pqrstuv")
        expected = 1048970
        self.assertEqual(actual, expected)
        
if __name__ == '__main__':
    unittest.main()