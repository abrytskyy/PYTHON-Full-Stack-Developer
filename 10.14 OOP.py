#1. Create a class named Person with attributes name and age, and methods for setting and retrieving these attributes
# using setattr and getattr.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        return getattr(self, "name", False)
    def get_age(self):
        return getattr(self, "age", False)
    def set_name(self, name):
        setattr(self, "name", name)

tom = Person("Tom", 30)
#change name:
tom.set_name("Jim")
print(tom.get_name())
print(tom.get_age())



#2. Create a class named Rectangle with attributes width and height. Write a method that calculates the area of the
# rectangle using getattr.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_area(self):
        return getattr(self, "width", False) * getattr(self, "height", False)

    def get_area1(self):
        return self.width * self.height
rectangle = Rectangle(10, 5)
print(rectangle.get_area())
print(rectangle.get_area1())
print(rectangle.__dict__)



#3. Create a class named Employee with attributes name and salary. Write a method to delete the salary attribute
# using delattr.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def del_salary(self):
        delattr(self, "salary")
employee = Employee("John", 2500)
print(employee.__dict__)
employee.del_salary()
print(employee.__dict__)

employee1 = Employee("Tom", 2700)
print(employee1.__dict__)
print(employee.__dict__, employee1.__dict__)



#4. Create a class named Circle with attributes radius and pi (a constant). Write a method to calculate the area of the
# circle using getattr to access radius and pi.
class Circle:
    PI = 3.14
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        #return getattr(Circle, "PI") * getattr(self, "radius", False)**2
       
