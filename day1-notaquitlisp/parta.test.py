import unittest

from parta import whatfloor

class TestDayOne(unittest.TestCase):

    def test_one(self):
        actual = whatfloor("(())")
        expected = 0
        self.assertEqual(actual, expected)

    def test_two(self):
        actual = whatfloor("()()")
        expected = 0
        self.assertEqual(actual, expected)
    
    def test_three(self):
        actual = whatfloor("(((")
        expected = 3
        self.assertEqual(actual, expected)

    def test_four(self):
        actual = whatfloor("(()(()(")
        expected = 3
        self.assertEqual(actual, expected)
    
    def test_five(self):
        actual = whatfloor("))(((((")
        expected = 3
        self.assertEqual(actual, expected)        
    
    def test_six(self):
        actual = whatfloor("())")
        expected = -1
        self.assertEqual(actual, expected)

    def test_seven(self):
        actual = whatfloor("))(")
        expected = -1
        self.assertEqual(actual, expected)  

    def test_eight(self):
        actual = whatfloor(")))")
        expected = -3
        self.assertEqual(actual, expected)

    def test_nine(self):
        actual = whatfloor(")())())")
        expected = -3
        self.assertEqual(actual, expected)          
if __name__ == '__main__':
    unittest.main()