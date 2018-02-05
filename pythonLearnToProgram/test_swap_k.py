import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    def test_swap_k_1(self):
        """test with empty list"""
        actual = []
        a1.swap_k(actual,0)
        expected = []
        self.assertEqual(actual, expected)

    def test_swap_k_2(self):
        """test with 1 item list"""
        actual = [1]
        a1.swap_k(actual,0)
        expected = [1]
        self.assertEqual(actual, expected)

    def test_swap_k_3(self):
        """test with 2 item list"""
        actual = [1,2]
        a1.swap_k(actual,1)
        expected = [2,1]
        self.assertEqual(actual, expected)

    def test_swap_k_4(self):
        """test with odd number of items, k is odd"""
        actual = [1,2,3]
        a1.swap_k(actual,1)
        expected = [3,2,1]
        self.assertEqual(actual, expected)

    def test_swap_k_5(self):
        """test with odd number of items, k is even"""
        actual = [1,2,3,4,5]
        a1.swap_k(actual,2)
        expected = [4,5,3,1,2]
        self.assertEqual(actual, expected)

    def test_swap_k_6(self):
        """test with even number of items, k is odd"""
        actual = [1,2,3,4,5,6,7,8]
        a1.swap_k(actual,3)
        expected = [6,7,8,4,5,1,2,3]
        self.assertEqual(actual, expected)

    def test_swap_k_7(self):
        """test with even number of items, k is even"""
        actual = [1,2,3,4,5,6,7,8]
        a1.swap_k(actual,2)
        expected = [7,8,3,4,5,6,1,2]
        self.assertEqual(actual, expected)

    def test_swap_k_8(self):
        """test with even number of items, k is n/2"""
        actual = [1,2,3,4,5,6,7,8]
        a1.swap_k(actual,4)
        expected = [5,6,7,8,1,2,3,4]
        self.assertEqual(actual, expected)

    def test_swap_k_9(self):
        """test with odd number of items, k is (n-1)/2"""
        actual = [1,2,3,4,5,6,7,8,9]
        a1.swap_k(actual,4)
        expected = [6,7,8,9,5,1,2,3,4]
        self.assertEqual(actual, expected)
        
if __name__ == '__main__':
    unittest.main(exit=False)
