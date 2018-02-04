import unittest
import binary

class BinarySearchTest(unittest.TestCase):
    def test_binary_search_1(self):
        """test binary search with the search value in the middle of
        odd length array
        """
        actual = binary.binary_search([1,2,3],2)
        expected = 1
        self.assertEqual(actual,expected)

if __name__ == '__main__':
    unittest.main(exit=False)
