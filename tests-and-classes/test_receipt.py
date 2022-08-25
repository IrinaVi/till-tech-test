import unittest
from receipt import Receipt
from unittest.mock import patch, Mock, MagicMock

class Testreceipt(unittest.TestCase):

    def test_tax_and_total(self):
        fake_order_class1 = Mock()
        fake_order_class1.total_order.return_value = {'Muffin Of The Day': 5}
        fake_till1 = Mock()
        fake_till1.get_total_and_tax.return_value = {'total': 22.75, 'tax': 1.97}
        receipt1 = Receipt()
        receipt1.format_receipt(fake_order_class1.total_order(), fake_till1.get_total_and_tax())
        self.assertMultiLineEqual(receipt1.get_final_receipt(),
                         "\n Muffin Of The Day 5 x 4.55 \n Total: $22.75 \n Tax: $1.97")

        fake_order_class2 = Mock()
        fake_order_class2.total_order.return_value = {'Choc Mousse': 2, 'Cortado': 3}
        fake_till2 = Mock()
        fake_till2.get_total_and_tax.return_value = {'total': 30.05, 'tax': 2.6}
        receipt2 = Receipt()
        receipt2.format_receipt(fake_order_class2.total_order(), fake_till2.get_total_and_tax())
        self.assertMultiLineEqual(receipt2.get_final_receipt(),
                         "\n Choc Mousse 2 x 8.2\n Cortado 3 x 4.55 \n Total: $30.05 \n Tax: $2.6")

if __name__ == '__main__':
    unittest.main()