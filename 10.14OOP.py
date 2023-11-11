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
        #return self.PI * self.radius **2
        return Circle.PI * self.radius**2
circle = Circle(15)
print(circle.area())



#5. Create a class named Student with attributes name, age, and grades. Write a method to add a grade to the grades
# list using getattr and setattr.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []
    def add_grade(self, grade):
        self.grades.append(grade)
student1 = Student("John", 20)

student1.add_grade(85)
student1.add_grade(92)
student1.add_grade(78)

print(student1.__dict__)



#6. Create a class named BankAccount with attributes balance and account_number. Implement the methods deposit and
# withdraw, as well as a method get_balance, which returns the balance.
class BankAccount:
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
    def withdraw(self, amount):
        if 0< amount <= self.balance:
            self.balance -= amount
    def get_balance(self):
        return self.balance
account = BankAccount(30000, "12345678")
print(account.get_balance())


class BankAccount:
    def __init__(self, account_number, balance = 0):
        self.balance = balance
        self.account_number = account_number
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
    def withdraw(self, amount):
        if 0< amount <= self.balance:
            self.balance -= amount
    def get_balance(self):
        return self.balance
account = BankAccount("12345678", 30000)
print(account.get_balance())



#7. Develop a class named Book with attributes title and author. Implement a method get_info that returns information
# about the book.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_info(self):
        return f"Title: {self.title} by {self.author}"
book = Book("Python1", "T. Geddis")
print(book.get_info())


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"Title: {self.title} by {self.author}"

book = Book("Python1", "T. Geddis")
print(book)