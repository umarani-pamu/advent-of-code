import unittest

from partb import new_nicestring

class TestDayOne(unittest.TestCase):

    def test_one(self):
        actual =new_nicestring("qjhvhtzxzqqjkmpb")
        expected = "nice string"    
        self.assertEqual(actual, expected)

    def test_two(self):
        actual = new_nicestring("xxyxx")
        expected = "nice string" 
        self.assertEqual(actual, expected)

    def test_two(self):
        actual = new_nicestring("uurcxstgmygtbstg")
        expected = "naughty" 
        self.assertEqual(actual, expected)

    def test_two(self):
        actual = new_nicestring("ieodomkazucvgmuy")
        expected = "naughty" 
        self.assertEqual(actual, expected) 
    
        
if __name__ == '__main__':
    unittest.main()