from category import Category
from product import Product
from ball import Ball
from footware import Footware
class Store:
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories # category


    def __str__(self):
        output = f"{self.name}\n"
        for i, cat in enumerate(self.categories):
            output += f" [{i + 1}] {cat.name}\n"
        
        output += f" [{i + 2}] Exit"
        
        return output

    def __repr__(self):
        return f"Store(\"{self.name}\", {self.categories})"


store = Store("My Shop", [Category("Running", [Footware("some Shoe Product", 23, "Red", 12), Product("some Boot Product", 34), Product("some Sock Product", 90)]), Category("Baseball"), Category("Basketball", [Ball("Wilson Super Charge", 900, False)])])
selection = 0

while selection != len(store.categories) + 1:
    print(store)
    try:
        selection = int(input("Select the number of a department. "))
        if selection == len(store.categories) + 1:
            print(f"Thank's for shopping at {store.name}")
        elif selection > 0 and selection <= len(store.categories):
            print(f"{store.categories[selection - 1]}")
    except ValueError:
        print("Please enter your choice as a number.")







# print(repr(store))
