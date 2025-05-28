import unittest
import sys
import os

# Add the parent directory to the Python path so we can import the palindrome module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_simple_palindrome(self):
        """Test a simple palindrome without spaces"""
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("madam"))
        
    def test_palindrome_with_spaces(self):
        """Test palindromes with spaces and mixed case"""
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(is_palindrome("hello world"))

if __name__ == '__main__':
    unittest.main()
