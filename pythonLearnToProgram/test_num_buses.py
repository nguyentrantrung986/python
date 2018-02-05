import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    def test_num_buses_1(self):
        """Test with n = 0"""
        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(actual,expected)

    def test_num_buses_2(self):
        """Test with n > 0 and n < 50"""
        actual = a1.num_buses(33)
        expected = 1
        self.assertEqual(actual,expected)

    def test_num_buses_3(self):
        """Test with n = 50"""
        actual = a1.num_buses(50)
        expected = 1
        self.assertEqual(actual,expected)

    def test_num_buses_4(self):
        """Test with n > 50"""
        actual = a1.num_buses(71)
        expected = 2
        self.assertEqual(actual,expected)

    def test_num_buses_5(self):
        """Test with n much greater than 50"""
        actual = a1.num_buses(1001)
        expected = 21
        self.assertEqual(actual,expected)
        
if __name__ == '__main__':
    unittest.main(exit=False)
