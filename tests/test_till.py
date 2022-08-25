import unittest
from till import Till
from unittest.mock import patch, Mock, MagicMock

class TestTill(unittest.TestCase):

    def test_tax_and_total(self):
        fake_order_class1 = Mock()
        fake_order_class1.total_order.return_value = {'Cappucino': 2}
        till = Till()
        till.calculate_total(fake_order_class1.total_order())
        till.calculate_tax()
        self.assertEqual(till.get_total_and_tax(), {'total': 7.7, 'tax': 0.67})

        fake_order_class2 = Mock()
        fake_order_class2.total_order.return_value = {'Affogato': 3, 'Cafe Latte': 1, 'Chocolate Chip Muffin': 2}
        till = Till()
        till.calculate_total(fake_order_class2.total_order())
        till.calculate_tax()
        self.assertEqual(till.get_total_and_tax(), {'total': 57.25, 'tax': 4.95})

if __name__ == '__main__':
    unittest.main()
