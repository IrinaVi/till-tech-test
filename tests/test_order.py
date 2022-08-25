from order import Order
import unittest

class TestOrder(unittest.TestCase):

    def test_items_get_added_to_order(self):
        order1 = Order()
        order1.add_to_order('Cappucino', 2)
        self.assertEqual(order1.total_order(), {'Cappucino': 2})

        order2 = Order()
        order2.add_to_order('Affogato', 3)
        order2.add_to_order('Cafe Latte', 1)
        order2.add_to_order('Chocolate Chip Muffin', 2)
        self.assertEqual(order2.total_order(), {'Affogato': 3, 'Cafe Latte': 1, 'Chocolate Chip Muffin': 2})

    def test_error_handling(self):
        order1 = Order()
        with self.assertRaises(Exception) as exc:
            order1.add_to_order('test', 2)
        self.assertEqual(str(exc.exception), "Please choose only items from the menu and specify the correct number of items")

        with self.assertRaises(Exception) as exc:
            order1.add_to_order('', 2)
        self.assertEqual(str(exc.exception), "Please choose only items from the menu and specify the correct number of items")

if __name__ == '__main__':
    unittest.main()