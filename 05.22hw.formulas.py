#1. Calculator for BMI (Body Mass Index):
# Write a program that asks the user for their height and weight and then calculates and displays
# their Body Mass Index (BMI). The formula for calculating BMI is BMI = weight (kg) / (height (m) * height (m)).

height = float(input("1. Your height in m: "))
weight = float(input("Your weight in kg: "))
bmi = round(weight / height**2, 2)

print(f"You BMI is {bmi}")
print()


#2. Time Converter:
# Write a program that converts the number of minutes into the format "hours:minutes." The user should input
# the number of minutes, and the program should display the corresponding time in the format "hours:minutes."

minutes = int(input("2. Input minutes: "))
hours = minutes//60
minutes = minutes % 60

print(hours,":",minutes)
print(f"{hours}:{minutes}")
print()


#3. Temperature Converter:
# Write a program that converts temperature from degrees Celsius to degrees Fahrenheit. The user should input
# the temperature in degrees Celsius, and the program should display the corresponding temperature in
# degrees Fahrenheit. The conversion formula is F = C * 9/5 + 32, where F is the temperature in degrees
# Fahrenheit, and C is the temperature in degrees Celsius.

temperature_c = int(input("3. Input temperature in °C: "))
temperature_F = round((temperature_c * (9/5)) + 32)

print(f"Temperature in °F: {temperature_F}")
print()


#4. Hypotenuse Calculation:
# Write a program that asks the user for the lengths of the two legs of a right triangle and then calculates
# and displays the length of the hypotenuse. You can use the Pythagorean theorem for calculating the hypotenuse:
# hypotenuse^2 = leg1^2 + leg2^2.

import math
side_a = float(input("4. Input side A: "))
side_b = float(input("Input side B: "))
hypotenuse = round(math.sqrt(side_a**2 + side_b**2), 1)

print(f"Side C(hypotenuse): {hypotenuse}")
print()


#5. Discount Calculator:
# Write a program that asks the user for the cost of a product and the percentage discount and then displays
# the final cost of the product after applying the discount. The program should apply the discount to the original
# cost of the product and display the final cost.

cost = float(input("5. Enter the cost of the product: $"))
discount_percentage = float(input("Enter the discount percentage: %"))
discount_amount = (discount_percentage / 100) * cost
final_cost = cost - discount_amount

print(f"The final cost after {discount_percentage}% discount is: ${final_cost:.2f}")
print()


#6. Average Value Calculator:
# Write a program that asks the user for three numbers and then calculates and displays their arithmetic average
# (the sum of the numbers divided by their count).

num1 = float(input("6. Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
average = (num1 + num2 + num3) / 3

print(f"Average: {average:.2f}")
print()


#7. Rectangle Perimeter and Area:
# Write a program that asks the user for the length and width of a rectangle and then calculates and displays its
# perimeter and area. The formulas for calculating the perimeter and area are as follows:
# perimeter = 2 * (length + width), area = length * width.

length = float(input("7. Input length: "))
width = float(input("Input width: "))
perimeter_rectangle = round(2 * (length + width), 2)
area_rectangle = round(length * width, 2)

print("perimeter:", perimeter_rectangle)
print("area:", area_rectangle)
print()


#8. Currency Converter:
# Write a program that converts an amount of money from one currency to another. The user should input the amount and
# the source currency, as well as the target currency for conversion. The program should display the converted amount.

currency1_name = input("8. Input currency1 name: ")
currency2_name = input("Input currency2 name: ")
exchange_rate = float(input("Input exchange rate: "))
currency1 = float(input("Input amount of currency1: "))
currency2 = round(currency1 * exchange_rate, 2)

print(currency1, currency1_name,  "=", currency2, currency2_name)


print()


#9. Annual Income Calculator:
# Write a program that asks the user for their monthly income and then calculates and displays their annual income.
# The program should multiply the monthly income by 12 to obtain the annual income.

income_month = int(input("9. Input your monthly income: "))
income_year = income_month * 12

print("You annual income is:", income_year)
print()


#10. Circle Area Calculator:
# Write a program that asks the user for the radius of a circle and then calculates and displays its area.
# The formula for calculating the area of a circle is area = pi * radius^2.

import math
circle_radius = float(input("10. Input circle radius: "))
circle_area = round(math.pi * circle_radius ** 2, 2)

print("Circle area is:", circle_area)