#21. Use filter to select from the list only numbers that are powers of two.
number_list = [1, 2, 4, 8, 16, 5, 32, 64]
powers_of_two = list(filter(lambda x: x%2 == 0, number_list))
print(powers_of_two)


#22. Apply filter to choose strings in which all characters are unique.
string_list = ["python", "java", "unique", "algorithm", "hello"]
def unique_characters(s):
    return len(set(s)) == len(s)
unique_strings = list(filter(lambda x: unique_characters(x), string_list))
print(unique_strings)

#with map
string_list = ["python", "java", "unique", "algorithm", "hello"]
def unique_characters(s):
    return len(set(s)) == len(s)
unique_strings = list(map(lambda x: x if unique_characters(x) is True else '-', string_list))
print(unique_strings)


#23. Use filter to retain only elements in the list that are palindromes.
string_list = ["level", "python", "radar", "madam", "hello"]
palindromes = list(filter(lambda x: x == x[::-1], string_list))
print(palindromes)

#with map
string_list = ["level", "python", "radar", "madam", "hello"]
palindromes = list(map(lambda x: x if x == x[::-1] else '-', string_list))
print(palindromes)


#24. Apply filter to select numbers that are the product of two different elements in the list.
number_list = [2, 3, 4, 5, 6, 8, 10]
product_numbers = list(filter(lambda x: any(x == a * b for a in number_list for b in number_list if a != b), number_list))
print(product_numbers)


#25. Use filter to keep only strings with more than one vowel.
string_list = ["hello", "try", "example", "myth", "ai"]
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
filtered_strings = list(filter(lambda x: count_vowels(x) > 1, string_list))
print(filtered_strings)


#26. Apply filter to select elements in the list whose indices are prime numbers.
element_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
prime_elements = list(filter(lambda x: is_prime(element_list.index(x)), element_list))
print(prime_elements)


#27. Use filter to retain only strings containing the word "python" in any case.
string_list = ["Java is great", "I love Python", "Java is not Python", "pythonic", "pythonista"]
palindromes = list(filter(lambda x: "python" in x.lower(), string_list))
print(palindromes)


#28. Apply filter to select numbers that are the sum of two previous elements in the list.
number_list = [1, 2, 3, 4, 5, 9, 7, 8, 9]
filtered_indexes = list(filter(lambda x: number_list[x] == number_list[x - 1] + number_list[x - 2] if x >= 2 else False, range(len(number_list))))
result = []
for index in filtered_indexes:
    result.append(number_list[index])
print(result)


#29. Use filter to keep only strings in which all words start with the same letter.
string_list = ["apple banana", "cherry chocolate", "dog duck", "python programming"]
filtered_strings = list(filter(lambda x: all(x[0].lower() == word[0].lower() for word in x.split()), string_list))
print(filtered_strings)


#30. Apply filter to select elements in the list that are cubes of integers.
number_list = [1, 8, '27', 64, 5, 125, 216, "python", 343]
cubes_of_integers = list(filter(lambda x: isinstance(x, int) and x == int(x ** (1/3)) ** 3, number_list))
print(cubes_of_integers)
