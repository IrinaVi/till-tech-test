import unittest
from till import Till
from unittest.mock import patch, Mock, MagicMock

class TestTill(unittest.TestCase):

    def test(self):
        fake_order = MockClass()
        fake_order.order = MagicMock(return_value={'Cappucino': 2})

        till = Till()
        #till.calculate_total(fake_order.order)
        #till.calculate_tax()
        self.assertEqual(fake_order.order, {'Cappucino': 2})

if __name__ == '__main__':
    unittest.main()