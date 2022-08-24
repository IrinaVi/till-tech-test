##1. Classes design

<<<<<<< HEAD
┌─────────────────────────────────┐                   ┌─────────────────────────────────┐
│                                 │                   │                                 │
│  class Till                     │                   │  class Order                    │
│                                 │                   │                                 │
│  - calculates the total for the │                   │                                 │
│                                 │                   │  - adds a menu item to the order│
│order                            │                   │                                 │
│                                 ├──────────────────►│  - returns order                │
│ - calculates tax                │                   │                                 │
│                                 │◄──────────────────┤                                 │
│ - returns total, amount of tax  │                   │                                 │
└───────────────────┬─────────────┘                   └───────────────────┬─────────────┘
                    │    ┌───────────────────────────────────┐            │
                    │    │                                   │            │
                    │    │   class Receipt                   │            │
                    └───►│                                   │◄───────────┘
                         │  - takes an order,total price,tax │
                         │                                   │
                         │price list and returns formatted   │
                         │                                   │
                         │receipt                            │
                         └───────────────────────────────────┘

##2. Methods:
class Order
1. Init method: initializes an order dictionary, where the key is a menu item and the value is the number of items
2. add_to_order(menu_item, num_of_items): takes an item and the number of items, adds it to the order
3. total_order(): returns the total order in a form of a python dictionary

class Till
takes an order as an argument
1. Init method: constructs the class with an argument, which is the object of the order class
2. calculate_total: loops through the order and adds the price to the total
3. calculate tax: substitudes tax from total
4. total_and_tax: returns total for the order and tax

class Receipt
1. Init method: takes and order, total price
2. receipt method: returns receipt in the requested format:
menu item - number of items - price per item
tax deducted 
total for the order
