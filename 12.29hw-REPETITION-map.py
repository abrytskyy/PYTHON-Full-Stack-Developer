#21 Apply the map function to concatenate each string in the list with its reverse.
#(1)
my_list = ["abc", "def", "123", "python"]
result = list(map(lambda x: x + x[::-1], my_list))
print(result)

#(2)
my_list = ["abc", "def", "123", "python"]
def concat(x):
    return x + x[::-1]
result = list(map(concat, my_list))
print(result)



#22 Use map to calculate the factorial of each number in the list.
#(1)
number_list = [2, 4, 3]
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
res = list(map(factorial, number_list))
print(res)

#(2)
from functools import reduce
number_list = [3, 4, 5, 6]
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)
factorials = list(map(factorial, number_list))
print(factorials)



#23 Apply map to convert each string representation of a number in the list to a Roman numeral.
string_numbers = ["7", "42", "99", "201"]
def int_to_roman(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num
roman_numerals = list(map(lambda x: int_to_roman(int(x)), string_numbers))
print(roman_numerals)



#24 Use map to transform each element in the list into its string representation and add the prefix "Element_".
original_list = [1, 2, 3, 4]
transformed_list = list(map(lambda x: "Element_" + str(x), original_list))
print(transformed_list)



#25 Apply the map function to calculate the sum of digits in each number in the list.
numbers_list = [3, -500, 20]
result = list(map(lambda x: len(str(abs(x))),numbers_list))
print(result)



#26 Use map to replace each string in the list with its hash value.
string_list = ["apple", "banana", "cherry", "date"]
hashed_list = list(map(lambda x: hash(x), string_list))
print(hashed_list)



#27 Apply map to remove spaces from each string in the list.
string_list = ["apple pie", "banana split", "cherry tart", "date cookie"]
no_spaces_list = list(map(lambda x: x.replace(" ", ""), string_list))
print(no_spaces_list)



#28 Use map to convert each number in the list to its hexadecimal representation.
number_list = [10, 20, 30, 255]
hex_representation = list(map(hex, number_list))
print(hex_representation)



#29 Apply the map function to multiply each even number in the list by 3 and each odd number by 2.
number_list = [3, 5, -9, 4, -6]
result_list = list(map(lambda x: x * 3 if x % 2 == 0 else x * 2, number_list))
print(result_list)



#30 Use map to concatenate each element of the list with its index in the format "Index: Element".
element_list = ["apple", "banana", "cherry", "date"]
result_list = list(map(lambda i, x: f"{i}: {x}", range(len(element_list)), element_list))
print(result_list)