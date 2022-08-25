from cafe_data import cafe_data

class Receipt():

    def __init__(self):
        self.final_receipt = ''

    def format_receipt(self, order, total_and_tax):
        order_info = ''
        for key,value in order.items():
            order_info += f'\n {key} {value} x {cafe_data["prices"][key]}'
        total = total_and_tax['total']
        tax = total_and_tax['tax']

        self.final_receipt = f"{order_info} \n Total: ${total} \n Tax: ${tax}"
        print(self.final_receipt)

    def get_final_receipt(self):
        return self.final_receipt