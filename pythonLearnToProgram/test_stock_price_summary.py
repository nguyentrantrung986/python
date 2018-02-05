import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    def test_stock_price_summary_1(self):
        """Test with empty list"""
        actual = a1.stock_price_summary([])
        expected = (0.0, 0.0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_2(self):
        """Test with list of one negative number"""
        actual = a1.stock_price_summary([-1.3])
        expected = (0.0, -1.3)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_3(self):
        """Test with list of one positive number"""
        actual = a1.stock_price_summary([27])
        expected = (27.0, 0.0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_4(self):
        """Test with list of one positive number and one negative number"""
        actual = a1.stock_price_summary([33.1, -21.7])
        expected = (33.1, -21.7)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_5(self):
        """Test with list of zero"""
        actual = a1.stock_price_summary([0,0.0,0.0,0])
        expected = (0.0, 0.0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_6(self):
        """Test with list of negative, positive and zero numbers"""
        actual = a1.stock_price_summary([-22.1, 0.003, 0, 3.5, 0.0, -2.3, 0, 9.8])
        expected = (13.303, -24.4)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_7(self):
        """Test with list of numbers with many floating point"""
        actual = a1.stock_price_summary([-2.71663, 0.00092, -3.5888239, 1.44449])
        expected = (1.44541, -6.3054539)
        self.assertEqual(actual, expected)
        
if __name__ == '__main__':
    unittest.main(exit=False)
