##1. Classes design

┌────────────────────────────┐              ┌──────────────────────────┐
│                            │              │                          │
│  class Till                │              │ class Order              │
│                            │              │                          │
│  - calculates the total    │              │ - adds item to the order │
│                            │              │                          │
│  - calculate tax           │              │ - return order           │
│                            ├─────────────►│                          │
│  - prints receipt          │              │                          │
│                            │◄─────────────┤                          │
└────────────────────────────┘              └──────────────────────────┘

##2. Methods:
class Order
1. Init method: initializes am order dictionary, where the key is a cafe item and the value is the number of items
2. add_to_order(cafe_item, num_of_items): takes an item and adds it to the order
3. total_order(): returns the total order

class Till
takes an order as an argument
1. Init method: initializes 
2. calculate_total: loops through the order and adds the price to the total
3. calculate tax: substitudes tax from total
4. print receipt: prints the receipt