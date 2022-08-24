class Order():
    def __init__(self):
        self.order = {}

    def add_to_order(self, menu_item, num_of_items):
        self.order[menu_item] = num_of_items

    def total_order(self):
        return self.order