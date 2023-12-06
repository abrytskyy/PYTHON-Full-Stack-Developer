#Declare the class Cart in the program, objects of which are created with the command:

#cart = Cart()
#Each object of the Cart class should have a local property:
# goods - a list of objects to buy (objects of the classes Table, TV, Notebook, and Cup).
# Initially, this list should be empty.

#Declare the following methods in the Cart class:

# add(self, gd) - adding a product represented by the object gd to the cart;
# remove(self, indx) - removing a product from the cart by index indx;
# get_list(self) - obtaining products from the cart as a list of strings:

# ['<name_1>: <price_1>',
# '<name_2>: <price_2>',
# ...
# '<name_N>: <price_N>']
# Declare the following classes in the program to describe products:
#
# Table - tables;
# TV - televisions;
# Notebook - notebooks;
# Cup - cups.
# Objects of these classes should be created with the command:

# gd = ClassName(name, price)
# Each object of the product classes should contain local properties:
#
# name - name;
# price - price.
# Create an object cart of the Cart class in the program. Add to it two TVs (TV), one table (Table),
# two notebooks (Notebook), and one cup (Cup). Invent names and prices yourself.
class Cart:
    goods = []

    def add(self, gd):
        Cart.goods.append(gd)

    def remove(self, indx):
        del Cart.goods[indx]

    def get_list(self):
        return [f'{product.name}: {product.price}' for product in Cart.goods]

class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price

cart = Cart()
cart.add(TV("Samsung 4K Smart TV", 899.99))
cart.add(TV("LG OLED TV", 1499.99))
cart.add(Table("Oak Dining Table", 499.99))
cart.add(Notebook("Dell XPS 13", 1199.99))
cart.add(Notebook("MacBook Pro", 1799.99))
cart.add(Cup("Yeti Rambler Mug", 29.99))

for product in cart.get_list():
    print(product)

#or
#print(*cart.get_list(), sep="\n")