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
        till1.calculate_total(order1.total_order())
        till1.calculate_tax()
        receipt1.format_receipt(order1.total_order(), till1.get_total_and_tax())
        self.assertEqual(receipt1.get_final_receipt(), "\n Single Espresso 3 x 2.05 \n Total: $6.15 \n Tax: $0.53")

        order2 = Order()
        till2 = Till()
        receipt2 = Receipt()
        order2.add_to_order('Americano', 1)
        order2.add_to_order('Tiramisu', 1)
        till2.calculate_total(order2.total_order())
        till2.calculate_tax()
        receipt1.format_receipt(order2.total_order(), till2.get_total_and_tax())
        self.assertEqual(receipt1.get_final_receipt(), "\n Americano 1 x 3.75\n Tiramisu 1 x 11.4 \n Total: $15.15 \n Tax: $1.31")

if __name__ == '__main__':
    unittest.main()