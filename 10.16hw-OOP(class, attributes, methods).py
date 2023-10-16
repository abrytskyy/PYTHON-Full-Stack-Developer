#1. Create a class called Student with attributes name and grades. Implement a method named is_excellent that returns
# True if the student's average grade is above 4.5, and False otherwise.
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    def is_excellent(self):
        avarage_grade = sum(self.grades)/len(self.grades)
        return avarage_grade > 4.5

student1 = Student("John", [4.0, 4.5, 5.0, 4.8, 4.7])
student2 = Student("Jim", [4.0, 4.5, 3.0, 3.8, 3.7])
print(student1.is_excellent())
print(student2.is_excellent())



#2. Develop a class called Employee with attributes name and salary. Implement a method named is_executive that returns
# True if the employee's salary is above $150,000, and False otherwise.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def is_executive(self):
        return self.salary > 150000
employee1 = Employee("John Doe", 160000)
employee2 = Employee("Jim Elvis", 140000)
print(employee1.is_executive())
print(employee2.is_executive())



#3. Create a class called BankAccount with attributes balance and account_number. Implement a method named is_overdrawn
# that returns True if the balance is negative, and False otherwise.

class BankAccount:
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number
    def is_overdrawn(self):
        return self.balance < 0

account1 = BankAccount(-1000, "123456")
account2 = BankAccount(1000, "123456")
print(account1.is_overdrawn())
print(account2.is_overdrawn())
