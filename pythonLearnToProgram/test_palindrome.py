import unittest
import palindrome_v3

class TestPalindrome(unittest.TestCase):
    
    def test_palindrome_1(self):
        """Test is_palindrome with an empty string ''"""
        actual = palindrome_v3.is_palindrome_v3('')
        expected = True
        self.assertEqual(actual,expected)

    def test_palindrome_2(self):
        """Test is_palindrome with a string of length 1"""
        actual = palindrome_v3.is_palindrome_v3('a')
        expected = True
        self.assertEqual(actual,expected)

    def test_palindrome_3(self):
        """Test is_palindrome_v3 with a string of length 2"""
        actual = palindrome_v3.is_palindrome_v3('ab')
        expected = False
        self.assertEqual(actual,expected)

    def test_palindrome_4(self):
        """Test is_palindrome_v3 with a string of length 2"""
        actual = palindrome_v3.is_palindrome_v3('11')
        expected = True
        self.assertEqual(actual,expected)

    def test_palindrome_5(self):
        """Test is_palindrome_v3 with a string of odd length > 2"""
        actual = palindrome_v3.is_palindrome_v3('ad1')
        expected = False
        self.assertEqual(actual,expected)

    def test_palindrome_6(self):
        """Test is_palindrome_v3 with a string of odd length > 2"""
        actual = palindrome_v3.is_palindrome_v3('racecar')
        expected = True
        self.assertEqual(actual,expected)

    def test_palindrome_7(self):
        """Test is_palindrome_v3 with a string of even length > 2"""
        actual = palindrome_v3.is_palindrome_v3('pendent')
        expected = False
        self.assertEqual(actual,expected)

    def test_palindrome_8(self):
        """Test is_palindrome_v3 with a string of even length > 2"""
        actual = palindrome_v3.is_palindrome_v3('HannaH')
        expected = True
        self.assertEqual(actual,expected)
        
if __name__ == '__main__':
    unittest.main(exit=False)
