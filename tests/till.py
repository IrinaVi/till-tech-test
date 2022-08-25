from cafe_data import cafe_data

class Till():
    tax = 8.64

    def __init__(self):
        self.total_and_tax = {}
        self.total = 0

    def calculate_total(self, order):
        for key, value in order.items():
            self.total += cafe_data["prices"][key] * value
        self.total_and_tax['total'] = round((self.total),2)

    def calculate_tax(self):
        tax = round((self.total/100) * 8.64, 2)
        self.total_and_tax['tax'] = tax

    def get_total_and_tax(self):
        return self.total_and_tax
