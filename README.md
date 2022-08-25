# Till tech test

## Project Description
This project aims to help cafe and restaurant owners. They can use this app to count total and tax for an order, as well as get a nicely formatted receipt for their customers.


## Project approach
I used Python as the main language for this project. Unittest for testing, pylint for a better code quality and Coverage.py to check test coverage. 

The program consists of three classes which helps to separate the areas of functionality:

1. Order - this class represents customer's order and has two methods:
`add_to_order` - allows users to add the menu item and number of items to their order.
`total_order` - returns customer's order with chosen menu items and the amount of each items ordered in a form of dictionary.

3. Till - this class is responsible for calculating the bill and has three methods:
`calculate_total` - takes an order as an argument and calculates the total amount the customer needs to pay.
`calculate_tax` - calculates the tax for the order
`get_total_and_tax` - returns total and tax for the given order in a form of a Python dictionary. 

4. Receipt - this class is responsible only for the nice formatting of the final receipt and has two methods:
`format_receipt` - takes the order from the Order class, total and tax from the Till class and formats it into the nice format for a customer
`get_final_receipt` - returns the formatted receipt which can be passed to a customer.


## Table of Contents
The program consists of three files with classes:
* order.py
* till.py
* receipt.py

Four files with tests:
* test_integration.py
* test_till.py
* test_receipt.py
* test_order.py

Supporting files:
* design.md
* cafe_data.py

## Project dependencies
1. Download and install Python  
https://www.python.org/downloads/

2. To run the tests use `python` command followed by the test file you would like to run, for example:
`python tests/test_till.py`


## How to use the project
First, create an object from the Order, Till and Receipt classes:  

`order = Order()`  
`till = Till()`  
`receipt = Receipt()`  

Then, add your order using add_to_order method and calculate total and tax (don't forget to pass the order to this method):

`order.add_to_order('Single Espresso', 3)`  
`till.calculate_total(order.total_order())`  
`till.calculate_tax()`  

To get the receipt, call the following methods:
`receipt.format_receipt(order.total_order(),till.get_total_and_tax())`  
`receipt.get_final_receipt`  