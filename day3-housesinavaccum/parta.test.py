import unittest

from parta import countuniquehouses

class TestDayOne(unittest.TestCase):

    def test_one(self):
        actual =countuniquehouses(">")
        expected = 2
        self.assertEqual(actual, expected)

    def test_two(self):
        actual = countuniquehouses("^>v<")
        expected = 4
        self.assertEqual(actual, expected)
        
    def test_three(self):
        actual = countuniquehouses("^v^v^v^v^v")
        expected = 2
        self.assertEqual(actual, expected)    

if __name__ == '__main__':
    unittest.main()