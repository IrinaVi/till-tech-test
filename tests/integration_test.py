from tests.order import Order
from tests.till import Till
from cafe_app.receipt import Receipt

def test():
    order = Order()
    order.add_to_order('Cappucino', 2)
    order.add_to_order('Tiramisu', 3)
    till = Till(order)
    total = till.total_and_tax
    receipt = Receipt(order, total)
    assert receipt == "Cappucino 2 x 3.85 \n Tiramisu 3 x 11.40.\n Tax: $3.6\nTotal: $41.9"