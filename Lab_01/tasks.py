
"""
Lab 01 — Python Basics

Complete all tasks below.

Topics:
- variables
- basic data types
- input and output
- type conversion
- arithmetic operators
- basic PEP 8
"""


# ============================================================
# Task 1 — Personal Information
# ============================================================

print("Task 1 — Personal Information")

# TODO:
# Ask the user to enter their name.

name = input("Enter your name: ")

# TODO:
# Ask the user to enter their age.
# Remember that input() returns a string.

age = int(input("Enter your age: "))

# TODO:
# Print:
# Hello, <name>!
# Next year you will be <age + 1> years old.

print(f"Hello, {name}!")
print(f"Next year you will be {age + 1} years older")




# ============================================================
# Task 2 — Rectangle
# ============================================================

print("Task 2 — Rectangle")

# TODO:
# Ask the user to enter width and height.

width = float(input("Enter width: "))
height = float(input("Enter height: "))

# TODO:
# Calculate the area.

area = width * height

# TODO:
# Calculate the perimeter.

perimeter = 2 * (width + height)


# TODO:
# Print the results.
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")


print()


# ============================================================
# Task 3 — Temperature Converter
# ============================================================

print("Task 3 — Temperature Converter")

# Formula:
# Fahrenheit = Celsius * 9 / 5 + 32

# TODO:
# Read Celsius temperature.

celsius = float(input("Enter Celcius: "))

# TODO:
# Calculate Fahrenheit temperature.

fahrenheit = celsius * 9 / 5 + 32

# TODO:
# Print the result.
print(f"{celsius}°C is equal to {fahrenheit}°F")



# ============================================================
# Task 4 — Purchase Calculator
# ============================================================

print("Task 4 — Purchase Calculator")

# TODO:
# Ask for the number of items.

quantity = int(input("Enter quantity: "))


# TODO:
# Ask for the price of one item.

price = float(input("Enter price per item: "))

# TODO:
# Calculate the total price.

total_price = quantity * price

# TODO:
# Apply a 10% discount.
discounted_price = total_price - (total_price * 0.10)

# TODO:
print(f"Total price: ${total_price}")
print(f"Discounted price (10% off): ${discounted_price}")


# ============================================================
# Task 5 — Arithmetic Operators
# ============================================================

print("Task 5 — Arithmetic Operators")

a = 17
b = 5

# TODO:
# Print the result of each operation:
#
# a + b
# a - b
# a * b
# a / b
# a // b
# a % b
# a ** b


print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")

# ============================================================
# Task 6 — Data Types
# ============================================================

print("Task 6 — Data Types")

integer_value = 42
float_value = 3.14
complex_value = 2 + 3j
text_value = "Python"
boolean_value = True

# TODO:
# Use type() to print the type of every variable above.
#
# Example:
print(type(integer_value))
print(type(float_value))
print(type(complex_value ))
print(type(text_value))
print(type(boolean_value))


# ============================================================
# Task 7 — Comparisons and Boolean Logic
# ============================================================

print("Task 7 — Comparisons and Boolean Logic")

age = 22
is_master_student = True

# TODO:
# Print the result of the following expressions:
#
# age >= 18
# age < 30
# age == 22
# age != 25
#
# age >= 18 and is_master_student
# age < 18 or is_master_student
# not is_master_student


print(age >= 18)
print(age < 30)
print(age == 22)
print(age != 25)
print(age >= 18 and is_master_student)
print(age < 18 or is_master_student)
print(not is_master_student)
#
# Predict each result before running the program.



# ============================================================
# Task 8 — Python Collections
# ============================================================

print("Task 8 — Python Collections")

# TODO:
# Create:
#
# 1. A list containing three programming languages.
# 2. A tuple containing three numbers.
# 3. A set containing several city names.
# 4. A dictionary describing a student with:
#       name
#       age
#       university

programming_languages = ["Python", "Golang", "Java"]
numbers = (7,8,9)
cities = set(["Lagos","Abuja","Port-Hacourt"])
student = {
    "name":"Moses Idiong",
    "age": 25,
    "university": "Novosibirsk State University"
}

# TODO:
# Print all four variables.
print(programming_languages)
print(numbers)
print(cities)
print(student)
#
# TODO:
# Use type() to print the type of each collection.
print(type(programming_languages))
print(type(numbers))
print(type(cities))
print(type(student))


# ============================================================
# Task 9 — Indexing and Slicing
# ============================================================

print("Task 9 — Indexing and Slicing")

numbers = [0, 1, 2, 3, 4, 5, 6, 7]

# TODO:
# Print the first element.
print(numbers[0])

# TODO:
# Print the last element.
print(numbers[7])

# TODO:
# Print elements from index 1 up to index 4.
print(numbers[1:4])
# Expected:
# [1, 2, 3]

# TODO:
# Print every second element.
#
# Expected:
# [0, 2, 4, 6]
print(numbers[::2])


word = "Python"

# TODO:
# Print the first character.
print(word[0])

# TODO:
# Print the last character.
print(word[5])

# TODO:
# Print:
# Pyt


print()


# ============================================================
# Task 10 — Dictionaries and Membership
# ============================================================

print("Task 10 — Dictionaries and Membership")

student = {
    "name": "Anna",
    "age": 22,
    "city": "Novosibirsk",
}

# TODO:
# Print the student's name.
print(student["name"])

# TODO:
# Print the student's age.
print(student["age"])

# TODO:
# Check whether "age" exists in the dictionary.
# Print the result.
print("age" in student)

# TODO:
# Check whether "email" exists in the dictionary.
# Print the result.
print("email" in student)


numbers = [10, 20, 30, 40]

# TODO:
# Check whether 20 is in numbers.
print(20 in numbers)

# TODO:
# Check whether 50 is in numbers.
print(50 in numbers)


# ============================================================
# Task 11 — Formatted Output
# ============================================================

print("Task 11 — Formatted Output")

# TODO:
# Ask the user to enter the radius of a circle.

radius = float(input("Enter the Raduis: "))

# Use:
area = 3.14159 * radius ** 2


# TODO:
# Print the radius and area using an f-string.
#
# Example:
# Radius: 10.0
# Area: 314.16
#
# Print the area with exactly two digits after the decimal point.
#
# Hint:
# {value:.2f}
print(f"Radius: {radius}")
print(f"Area: {area:.2f}")


# ============================================================
# Task 12 — Trip Cost Calculator
# ============================================================

print("Task 12 — Trip Cost Calculator")

# A car consumes a certain number of liters of fuel
# for every 100 kilometers.

# TODO:
# Ask the user to enter:
#
# distance in kilometers
# fuel consumption in liters per 100 km
# fuel price per liter

distance = float(input("Enter distance: "))
fuel_consumption = float(input("Enter fuel consumption: "))
fuel_price = float(input("Enter Fuel price per liter: "))

# TODO:
# Calculate how many liters of fuel are required.
#
# Formula:
liters_needed = distance / 100 * fuel_consumption

# TODO:
# Calculate the total cost of the trip.

# Calculate the total cost of the trip.
trip_cost = liters_needed * fuel_price


# TODO:
# Print something similar to:
#
# Distance: 450.0 km
# Fuel required: 36.00 liters
# Trip cost: 2160.00
#
# Use f-strings and two decimal places where appropriate.
print(f"Distance: {distance:.2f} liters")
print(f"Fuel required: {liters_needed:.2f} liters")
print(f"Total trip cost: {trip_cost:.2f}")
