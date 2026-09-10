"""
Lab 02 — Python Basics II

Complete all tasks below.

Topics:
- built-in functions
- assignment and augmented assignment
- operator precedence
- type conversion
- strings
- print() options
- collections
- mutable and immutable objects
- formatted output
- basic PEP 8
- reading common errors

Do not use:
- if
- for
- while
- user-defined functions
"""


# ============================================================
# Task 1 — Built-in Functions
# ============================================================

print("Task 1 — Built-in Functions")

values = [12, 7, 19, 5, 14]

# TODO:
# Using built-in functions, calculate and print:
#
# number of values
# smallest value
# largest value
# total
# mean
#
# Do not calculate these manually.


count = len(values)
smallest = min(values)
largest = max(values)
total = sum(values)
mean = sum(values) / len(values)

# TODO:
# Print the results using f-strings.


print(f"{count}")
print(f"{smallest}")
print(f"{largest}")
print(f"{total}")
print(f"{mean:.2f}")


# ============================================================
# Task 2 — Absolute Value and Rounding
# ============================================================

print("Task 2 — Absolute Value and Rounding")

temperature_change = -7.438
measurement = 19.87654

# TODO:
# Print the absolute value of temperature_change.
#
# Expected numerical value:
# 7.438
print(abs(temperature_change))

# TODO:
# Round measurement to:
#
# 1 decimal place
# 2 decimal places
# 3 decimal places
#
# Use round().

print(round(measurement, 1))
print(round(measurement, 2))
print(round(measurement, 3))



# ============================================================
# Task 3 — Assignment and Augmented Assignment
# ============================================================

print("Task 3 — Assignment and Augmented Assignment")

balance = 1000.0

# Perform the following operations using augmented assignment:
#
# 1. Add 250 to the balance.
# 2. Subtract 120.
# 3. Multiply the remaining balance by 1.05.
#
# TODO:
# Replace the normal assignments below with +=, -=, and *=.

balance += 250
balance -= 120
balance *= 1.05

# TODO:
# Print the final balance with two decimal places.

print(f"{balance:.2f}")


# ============================================================
# Task 4 — Operator Precedence
# ============================================================

print("Task 4 — Operator Precedence")

# Before running the program, predict each result.

expression_1 = 2 + 3 * 4
expression_2 = (2 + 3) * 4
expression_3 = 20 / 5 + 3
expression_4 = 20 / (5 + 3)
expression_5 = 2 ** 3 ** 2

# TODO:
# Print each expression and its result.
#
# Example:
# 2 + 3 * 4 = 14
print(f"2 + 3 * 4 = {expression_1}")
print(f"(2 + 3) * 4 = {expression_2}")
print(f"20 / 5 + 3 = {expression_3}")
print(f"20 / (5 + 3) = {expression_4}")
print(f"2 ** 3 ** 2 = {expression_5}")



# ============================================================
# Task 5 — Time Conversion
# ============================================================

print("Task 5 — Time Conversion")

# TODO:
# Ask the user to enter a number of seconds.

total_seconds = input("Enter a number of seconds: ")

# TODO:
# Convert the input to int.
total_seconds = int(total_seconds)

# TODO:
# Calculate:
#
# whole minutes
# remaining seconds
#
# Example:
# 135 seconds -> 2 minutes and 15 seconds
#
# Hint:
# // and %

minutes = total_seconds // 60
remaining_seconds = total_seconds % 60

# TODO:
# Print:
# 135 seconds = 2 minute(s) and 15 second(s)

print(f"{total_seconds} seconds = {minutes} minute(s) and {remaining_seconds} second(s)")


# ============================================================
# Task 6 — Conversion Is Not Always Reversible
# ============================================================

print("Task 6 — Type Conversion")

value = 17.95

# TODO:
# Convert value to int and print it.
#
# Question:
# Does int() round the value?

integer_value = int(value)
print(integer_value)

# TODO:
# Convert integer_value back to float and print it.

float_value = int(integer_value)
print(float_value)

# TODO:
# Convert integer_value to str and print:
#
# Value as text: <value>
# Type: <type>
#
# Use type() for the second line.

text_value = str(float_value)
print(f"Value as text: {text_value}")
print(f"Type {type(text_value)}")


# ============================================================
# Task 7 — Basic String Operations
# ============================================================

print("Task 7 — Basic String Operations")

first_name = input("First name: ")
last_name = input("Last name: ")

# TODO:
# Create full_name using string concatenation.

full_name = first_name + " " + last_name

# TODO:
# Print:
#
# Full name: <full_name>
# Number of characters: <length>
# First character: <first character>
# Last character: <last character>
# First three characters: <slice>
print(full_name)
print(len(full_name))
print(full_name[0])
print(full_name[-1])
print(full_name[:3])

# TODO:
# Print full_name three times using string repetition.
print(full_name * 3)


# ============================================================
# Task 8 — Useful print() Options
# ============================================================

print("Task 8 — Useful print() Options")

language = "Python"
course = "AI and Big Data Analytics"
university = "NSU"

# TODO:
# Print the three values on one line separated by:
#
#  |
#
# Expected:
# Python | AI and Big Data Analytics | NSU
#
# Use sep=

print(language,course,university, sep=" | ")


# TODO:
# Use two print() calls and end= so that the result is:
#
# Python Programming
#
# Do not write "Python Programming" as one string.

print("Python", end=" ")
print("Programming")


# ============================================================
# Task 9 — Collections and Choosing Data Structures
# ============================================================

print("Task 9 — Collections")

student_name = "Anna"
student_age = 22
student_skills = ["Python", "Mathematics", "Machine Learning"]
student_university = "NSU"

# TODO:
# Create a dictionary named student with the keys:
#
# name
# age
# skills
# university

student = {
    "name": "Anna",
    "age": 22,
    "skills": ["Python", "Mathematics","Machine Learning"],
    "university": "NSU"
}

# TODO:
# Print:
#
# student's name
# student's university
# first skill
# number of skills
#
# Use dictionary access, indexing, and len().
print(student["name"])
print(student["university"])
print(student["skills"][0])
print(len(student["skills"]))


# ============================================================
# Task 10 — Mutable and Immutable Objects
# ============================================================

print("Task 10 — Mutable and Immutable Objects")

# List example — mutable

numbers = [10, 20, 30]
same_numbers = numbers

# TODO:
# Change the first item in numbers to 99.
#
# Then print both:
#
# numbers
# same_numbers
#
# Observe what happened.

numbers[0] = 99

print(numbers)
print(same_numbers)


# String example — immutable

text = "Python"
same_text = text

# TODO:
# Create a new string by adding " Course" to text.
#
# Then print:
#
# text
# same_text
#
# Compare this result with the list example.

text = text + "Course"
print(text)
print(same_text)


# ============================================================
# Task 11 — Small Statistics Report
# ============================================================

print("Task 11 — Small Statistics Report")

scores = [78, 92, 85, 69, 88]

# TODO:
# Calculate:
#
# number of scores
# minimum score
# maximum score
# total score
# mean score
#
# Use built-in functions.

score_count = len(scores)
minimum_score = min(scores)
maximum_score = max(scores)
total_score = sum(scores)
mean_score = sum(scores) / len(scores)

# TODO:
# Print a clean report:
#
# Number of scores: 5
# Minimum: 69
# Maximum: 92
# Mean: 82.40
#
# Format the mean to exactly two decimal places.

print(f"Number of scores: {score_count}")
print(f"Minimum: {minimum_score}")
print(f"Maximum: {maximum_score}")
print(f"Mean: {mean_score}")



# ============================================================
# Task 12 — PEP 8 Cleanup
# ============================================================

print("Task 12 — PEP 8 Cleanup")

# The following code works, but it is difficult to read.
#
# TODO:
# Rewrite it using:
#
# meaningful variable names
# snake_case
# spaces around operators
# intermediate variables
# formatted output
#
# Keep the same calculation.

price = 1250
quantity = 3
discount = 10

final_price = price*quantity-discount/100*price*quantity
print("Final:",final_price)


# ============================================================
# Optional Challenge — Student Score Summary
# ============================================================

print("Optional Challenge — Student Score Summary")

# Create a small program using only concepts from Sections 1–2.
#
# Ask the user for:
#
# student name
# three test scores
#
# Store the three scores in a list.
#
# Calculate:
#
# minimum score
# maximum score
# mean score
#
# Print a clean summary similar to:
#
# Student: Anna
# Scores: [78.0, 85.0, 91.0]
# Minimum: 78.00
# Maximum: 91.00
# Mean: 84.67
#
# Use:
# input()
# float()
# list
# min()
# max()
# sum()
# len()
# f-strings


# ============================================================
# Task 13 — Multiple Assignment
# ============================================================

print("Task 13 — Multiple Assignment")

# TODO:
# Assign these three values using ONE statement:
#
# x = 10
# y = 20
# z = 30

x, y, z = 10, 20, 30

# TODO:
# Print x, y, and z.
print(x,y,z)


# TODO:
# Swap a and b using one Python statement.

a = 5
b = 10


# Expected after swapping:
# a = 10
# b = 5

a, b = b, a


print(a,b)


# ============================================================
# Task 14 — String Methods
# ============================================================

print("Task 14 — String Methods")

text = "  Python Programming Course  "

# TODO:
# Print the text:
#
# 1. without surrounding spaces
# 2. in lowercase
# 3. in uppercase
# 4. with "Course" replaced by "Lab"

# TODO:
# Check and print whether the cleaned text:
#
# starts with "Python"
# ends with "Course"
#
# Use:
# strip()
# lower()
# upper()
# replace()
# startswith()
# endswith()

clean_text = text.strip()

print(clean_text)
print(clean_text.lower())
print(clean_text.upper())
print(clean_text.replace("Course", "Lab"))

# ============================================================
# Task 15 — Boolean Expressions
# ============================================================

print("Task 15 — Boolean Expressions")

age = 22
score = 85
is_master_student = True

# TODO:
# Print the result of:

# age >= 18
# score >= 60
# score >= 60 and is_master_student
# score < 60 or age < 18
# not is_master_student

print(age >= 18)
print(score >= 60)
print(score >= 60 and is_master_student)
print(score < 60 or age < 18)
print(not is_master_student)

# TODO:
# Predict and then print:

# bool(0)
# bool(1)
# bool("")
# bool("Python")
# bool([])
# bool([1, 2])

print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Python"))
print(bool([]))
print(bool([1, 2]))



# ============================================================
# Task 16 — Membership
# ============================================================

print("Task 16 — Membership")

numbers = [10, 20, 30]
text = "Python Programming"
student = {
    "name": "Anna",
    "age": 22,
}

# TODO:
# Print the result of:

# 20 in numbers
# 50 not in numbers
# "Python" in text
# "Java" not in text
# "age" in student
# "email" in student


print(20 in numbers)
print(50 not in numbers)
print("Python" in text)
print("Java" not in text)
print("age" in student)
print("email" in student)





# ============================================================
# Task 17 — Time Decomposition
# ============================================================

print("Task 17 — Time Decomposition")

# Ask the user to enter a duration in seconds.
#
# Example:
# 9374
#
# Convert it into:
# hours
# minutes
# seconds
#
# Expected:
# 9374 seconds = 2 hour(s), 36 minute(s), 14 second(s)
#
# Use only:
# int()
# //
# %
# arithmetic
# f-strings

# TODO:
# Read total_seconds from the user.

total_seconds = int(input("Enter a number in seconds: "))


# TODO:
# Calculate all four values.

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

# TODO:
# Print the formatted result.
print(f"{total_seconds} seconds = {hours} hour(s), {minutes} minute(s), {seconds} second(s)")




# ============================================================
# Task 18 — Order Invoice
# ============================================================

print("Task 18 — Order Invoice")

# A customer buys three different products.
#
# Ask for:
# product 1 price and quantity
# product 2 price and quantity
# product 3 price and quantity
#
# Calculate:
# subtotal for every product
# total before tax
# tax = 5%
# final total
#
# Example output:
#
# Product 1: 1200.00
# Product 2: 750.00
# Product 3: 400.00
# --------------------
# Subtotal: 2350.00
# Tax: 117.50
# Total: 2467.50
#
# Do not use if, loops, or functions.

price_1 = float(input("Product 1 Price: "))
quantity_1 = int(input("Product 1 Quantity: "))

price_2 = float(input("Product 2 Price: "))
quantity_2 = int(input("Product 2 Quantity: "))

price_3 = float(input("Product 3 Price: "))
quantity_3 = int(input("Product 3 Quantity: "))

# TODO:
# Read all six values.

product_1_total = price_1 * quantity_1
product_2_total = price_2 * quantity_2
product_3_total = price_3 * quantity_3



# TODO:
# Perform the calculations.
subtotal = product_1_total + product_2_total + product_3_total
tax = 0.05 * subtotal
final_total = subtotal + tax

# TODO:
# Print a clean invoice using f-strings.

print(f"Product 1: {product_1_total:.2f}")
print(f"Product 2: {product_2_total:.2f}")
print(f"Product 3: {product_3_total:.2f}")
print("--------------------")
print(f"Subtotal: {subtotal:.2f}")
print(f"Tax: {tax:.2f}")
print(f"Total: {final_total:.2f}")


# ============================================================
# Task 19 — Coordinate Analysis
# ============================================================

print("Task 19 — Coordinate Analysis")

# Ask the user for two points:
#
# (x1, y1)
# (x2, y2)
#
# Store each point as a tuple.
#
# Calculate:
#
# difference in x
# difference in y
# squared distance
# distance
#
# Formula:
#
# distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#
# Print both points and the calculated distance.


# TODO:
# Read the four coordinates.
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))


# TODO:
# Create the two tuples.
point_1 = (x1 , y1)
point_2 = (x2, y2)


# TODO:
# Perform the calculations.
delta_x = point_2[0] - point_1[0]
delta_y = point_2[1] - point_1[1]
distance_squared = (delta_x ** 2) + (delta_y ** 2)
distance = distance_squared ** 0.5

# TODO:
# Print the result with two decimal places.
print(f"Distance {distance:.2f}")


# ============================================================
# Task 20 — Working with Complex Numbers
# ============================================================

print("Task 20 — Complex Numbers")

# Section 2 includes Python's basic data types.
# One numerical type that is easy to forget is complex.
#
# Given:

z1 = 3 + 4j
z2 = 2 - 1j

# TODO:
# Print:
#
# z1
# z2
# type(z1)
# z1 + z2
# z1 - z2
# z1 * z2
# z1 / z2
#
# Also print:
#
# z1.real
# z1.imag
#
# Predict the type of each arithmetic result before running it.


print(f"z1: {z1}")
print(f"z2: {z2}")
print(type(z1))
print(f"z1 + z2: {z1 + z2}")
print(f"z1 - z2: {z1 - z2}")
print(f"z1 * z2: {z1 * z2}")
print(f"z1 / z2: {z1 / z2}")
print(z1.real)
print(z1.imag)


# ============================================================
# Task 21 — Student Data Record
# ============================================================

print("Task 21 — Student Data Record")

# Ask the user for:
#
# name
# age
# university
# first score
# second score
# third score
#
# Store the scores in a list.
#
# Store all student information in a dictionary:
#
# {
#     "name": ...,
#     "age": ...,
#     "university": ...,
#     "scores": [...]
# }
#
# Then calculate:
#
# number of scores
# minimum score
# maximum score
# mean score
#
# Print a formatted student report.
#
# Do not use loops.


# TODO:
# Read the values.

student_name = input("Enter your name: ")
student_age = int(input("Enter your age: "))
university = input("Enter your university: ")

score_1 = float(input("Enter first score: "))
score_2 = float(input("Enter second score: "))
score_3 = float(input("Enter third score: "))

# TODO:
# Create scores.

scores = [score_1,score_2,score_3]

# TODO:
# Create student.

student = {
    "name": student_name,
    "age": student_age,
    "university": university,
    "scores": scores
}



# TODO:
# Calculate the statistics.
score_count = len(student["scores"])
minimum_score = min(student["scores"])
maximum_score = max(student["scores"])
mean_score = sum(student["scores"]) / len(student["scores"])

# TODO:
# Print a clean report.

print(f"Name: {student["name"]}")
print(f"Age: {student["age"]}")
print(f"University: {student["university"]}")
print(f"score_count: {score_count}")
print(f"minimum_score: {minimum_score}")
print(f"maximum_score: {maximum_score}")
print(f"mean_score: {mean_score:.2f}")


# ============================================================
# Task 22 — Debug the Program
# ============================================================

print("Task 22 — Debug the Program")

# The program below is supposed to calculate the average
# of three scores entered by the user.
#
# It currently contains several problems.
#
# Find and fix them.
#
# Do NOT use if, try-except, loops, or functions.
#
# Think about:
# - input() types
# - variable names
# - arithmetic
# - operator precedence
# - PEP 8
# - formatted output


# score1=input("Score 1: ")
# Score2=input("Score 2: ")
# score3=input("Score 3: ")
# total=score1+Score2+score3
# average=total/3
# print("Average:"+average)


# TODO:
# Rewrite the program correctly below.


score_1 = int(input("Score 1: "))
score_2 = int(input("Score 2: "))
score_3 = int(input("Score 3: "))

total = score_1 + score_2 + score_3
average = total / 3

print(f"Total: {total}")
print(f"Average: {average:.2f}")

