#1. Develop a class Car with attributes make and model. Implement a method change_make that allows you to change
# the car's manufacturer.

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def change_make(self, new_make):
        self.make = new_make

my_car = Car("Toyota", "Camry")
Car("Toyota", "Camry")
print(my_car.make, my_car.model)

my_car.change_make("Honda")
print(my_car.make, my_car.model)


#2. Create a class Rectangle with attributes width and height. Implement a method get_perimeter that returns
# the perimeter of the rectangle.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_perimeter(self):
        perimeter = 2*(self.width + self.height)
        return perimeter

my_rectangle = Rectangle(3, 5)
print(my_rectangle.width, my_rectangle.height, my_rectangle.get_perimeter())




# 3. Design a class Circle with an attribute radius. Implement a method get_area that returns the area of the circle.
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = math.pi * self.radius**2
        return round(area,2)
print(Circle(5).get_area())


