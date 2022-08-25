from cafe_data import cafe_data

class Receipt():

    def receipt(self, order, total_and_tax):
        welcome_message = f'Welcome to {cafe_data["shopName"]}! '
        order_info = ''
        for key,value in order.items():
            order_info += f'\n {key} {value} x {cafe_data["prices"][key]}'
        total = total_and_tax['total']
        tax = total_and_tax['tax']

        full_receipt = f'{welcome_message} {order_info} \n Total: ${total} \n Tax: ${tax}'
        print(full_receipt)