import unittest

from parta import nicestring

class TestDayOne(unittest.TestCase):

    def test_one(self):
        actual =nicestring("ugknbfddgicrmopn")
        expected = "nice string"    
        self.assertEqual(actual, expected)

    def test_two(self):
        actual = nicestring("jchzalrnumimnmhp")
        expected = "nice string" 
        self.assertEqual(actual, expected)

    def test_two(self):
        actual = nicestring("aaa")
        expected = "naughty" 
        self.assertEqual(actual, expected)

    def test_two(self):
        actual = nicestring("haegwjzuvuyypxyu")
        expected = "naughty" 
        self.assertEqual(actual, expected) 
    
    def test_two(self):
        actual = nicestring("dvszwmarrgswjxmb")
        expected = "naughty" 
        self.assertEqual(actual, expected)
        
if __name__ == '__main__':
    unittest.main()