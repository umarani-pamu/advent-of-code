import unittest

from partb import roboversion

class TestDayOne(unittest.TestCase):

    def test_one(self):
        actual =roboversion("^v")
        expected = 3
        self.assertEqual(actual, expected)

    def test_two(self):
        actual = roboversion("^>v<")
        expected = 3
        self.assertEqual(actual, expected)
        
    def test_three(self):
        actual = roboversion("^v^v^v^v^v")
        expected = 11
        self.assertEqual(actual, expected)    

if __name__ == '__main__':
    unittest.main()