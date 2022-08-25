from order import Order
from till import Till
from receipt import Receipt
import unittest

class TestOrder(unittest.TestCase):

    def test_items_get_added_to_order(self):
        order1 = Order()
        till1 = Till()
        receipt1 = Receipt()
        order1.add_to_order('Single Espresso', 3)
        till1.calculate_total(order1.order)
        till1.calculate_tax()
        total_and_tax = till1.get_total_and_tax()
        result = receipt1.receipt(order1.order, total_and_tax)
        self.assertEqual(result, '')



if __name__ == '__main__':
    unittest.main()