#1. Create a class called Calculator that takes two numbers in the constructor and
# has a method called "call" that performs addition.
# class Calculator():
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def __call__(self, *args, **kwargs):
#         return self.a + self.b
#
# c1 = Calculator(5, 8)
# print(c1())



#2. Extend the Calculator class so that the "call" method can perform various arithmetic operations
# (addition, subtraction, multiplication, division).
# class Calculator():
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __call__(self, operation='+'):
#         if operation == '+':
#             return self.a + self.b
#         elif operation == '-':
#             return self.a - self.b
#         elif operation == '*':
#             return self.a * self.b
#         elif operation == '/':
#             if self.b != 0:
#                 return self.a / self.b
#             else:
#                 return "Error: Division by zero"
#         else:
#             return "Error: Unsupported operation"
#
# c1 = Calculator(5, 8)
# print(c1())
# print(c1('-'))
# print(c1('*'))
# print(c1('/'))


#3. Create a class called StringRepeater that takes a string in the constructor and has a method
# called "call" that repeats the string a certain number of times.

# class StringRepeater():
#     def __init__(self, string):
#         self.string = string
#
#     def __call__(self, times, *args, **kwargs):
#         return self.string * times
# sr = StringRepeater("Hello ")
# print(sr(3))

# class StringRepeater():
#     def __init__(self, string):
#         self.string = string
#
#     def __call__(self, *args, **kwargs):
#         return self.string * args[0]
# sr = StringRepeater("Hello ")
# print(sr(3))



#4. Write a class called Power that takes a number and exponent in the constructor, and the "call" method returns
# the number raised to the specified exponent.
# class Power():
#     def __init__(self, number, exponent):
#         self.number = number
#         self.exponent = exponent
#
#     def __call__(self, *args, **kwargs):
#         return self.number**self.exponent
#
# p = Power(3, 4)
# print(p())

#without __init__:
# class Power():
#     def __call__(self, *args, **kwargs):
#         return args[0]**args[1]
#
# p = Power()
# print(p(3, 5))



#5. Implement a class called ListFilter that takes a list and a predicate function in the constructor.
# The "call" method should return a new list containing only the elements for which the predicate returns True.
class ListFilter():
    def __init__(self, list, function):
        self.list = list
        self.function = function

    def __call__(self, *args, **kwargs):
        return [el for el in self.list if self.function(el)]

def is_even(num):
    return num % 2 == 0

lf = ListFilter([1, 2, 3, 4, 5, 6], is_even)
print(lf())

def is_str(text):
    return type(text) == str

lf1 = ListFilter(["hello", 1, True, 'world'], is_str)
print(lf1())


