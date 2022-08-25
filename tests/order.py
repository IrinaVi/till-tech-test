from cafe_data import cafe_data

class Order():
    def __init__(self):
        self.order = {}

    def add_to_order(self, menu_item, num_of_items):
        if menu_item in cafe_data["prices"].keys() and isinstance(num_of_items, int):
            self.order[menu_item] = num_of_items
        else:
            raise Exception("Please choose only items from the menu and specify the correct number of items")

    def total_order(self):
        return self.order
