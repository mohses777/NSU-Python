"""
NSU Python — Lab 04
while Loops, Typing, Identity, and Functions

Complete Tasks 1–13.
Tasks 14–15 are optional bonus tasks.

Use only concepts covered in Lecture 04 and earlier lectures.
"""


# ============================================================
# Task 1 — Countdown with while
# ============================================================
# Ask the user for a positive integer.
#
# Use a while loop to print from that number down to 1.
# Then print:
#   Go!
#
# Example:
# Input: 5
# Output:
# 5
# 4
# 3
# 2
# 1
# Go!
#
# Make sure the loop variable changes.

# Write your code below:

number = int(input("Enter a positive integer: "))

while number > 0:
    print(number)
    number -= 1

print("Go!")



# ============================================================
# Task 2 — Repeat until zero
# ============================================================
# Repeatedly ask the user to enter an integer.
#
# Stop when the user enters 0.
#
# Before 0 is entered:
#   count how many non-zero numbers were entered;
#   calculate their sum.
#
# At the end print:
#   Count: ...
#   Sum: ...
#
# Example:
# Input: 5, -2, 7, 0
# Count: 3
# Sum: 10

# Write your code below:

count = 0
total = 0

number = int(input("Enter an integer (0 to stop): "))

while number != 0:
    count += 1
    total += number
    number = int(input("Enter an integer (0 to stop): "))

print(f"Count: {count}")
print(f"Sum: {total}")




# ============================================================
# Task 3 — Valid input with while True
# ============================================================
# Repeatedly ask the user for an integer from 1 to 10.
#
# If the value is outside this range:
#   print "Invalid value"
#   ask again.
#
# When the user enters a valid value:
#   print "Accepted"
#   stop the loop with break.
#
# Required:
# Use:
#   while True
#   break

# Write your code below:

while True:
    number = int(input("Enter an integer from 1 to 10: "))
    
    if 1 <= number <= 10:
        print("Accepted")
        break
    else:
        print("Invalid value")



# ============================================================
# Task 4 — continue in a while loop
# ============================================================
# Use a while loop to process numbers from 1 through 20.
#
# Skip numbers divisible by 3 using continue.
# Print all other numbers.
#
# IMPORTANT:
# Update the loop variable correctly so you do not create
# an infinite loop.

# Write your code below:

num = 0

while num < 20:
    num += 1
    if num % 3 == 0:
        continue
    print(num)



# ============================================================
# Task 5 — Search with loop else
# ============================================================
numbers = [4, 8, 12, 16, 21, 24]

# Search for the first odd number.
#
# If an odd number is found:
#   print "First odd number: <value>"
#   stop using break.
#
# If the loop finishes without finding any odd number:
#   print "All values are even"
#
# Required:
# Use:
#   for
#   break
#   else

# Write your code below:

for num in numbers:
    if num % 2 != 0:
        print(f"First odd number: {num}")
        break
else:
    print("All values are even")



# ============================================================
# Task 6 — Multiplication table with nested loops
# ============================================================
# Use nested for loops to print a 5 x 5 multiplication table.
#
# Rows: 1 through 5
# Columns: 1 through 5
#
# Example first row:
# 1 2 3 4 5
#
# Example second row:
# 2 4 6 8 10
#
# Hint:
# Build each row using print(..., end=" ") and print().

# Write your code below:

for row in range(1, 6):
    for col in range(1, 6):
        print(row * col, end=" ")
    print()


# ============================================================
# Task 7 — Dynamic typing
# ============================================================
# Create a variable named value.
#
# First assign:
#   42
# Print the value and its type.
#
# Then assign:
#   3.14
# Print the value and its type.
#
# Then assign:
#   "Python"
# Print the value and its type.
#
# Finally assign:
#   [1, 2, 3]
# Print the value and its type.
#
# Observe that the same variable name can refer to objects
# of different types during program execution.

# Write your code below:
value = 42
print(value, type(value))

value = 3.14
print(value, type(value))

value = "Python"
print(value, type(value))

value = [1, 2, 3]
print(value, type(value))



# ============================================================
# Task 8 — Equality, identity, and references
# ============================================================
a = [10, 20]
b = [10, 20]
c = a

# Before running the program, predict:
#
# a == b
# a is b
# a == c
# a is c
#
# Print all four results.
#
# Then print:
#   id(a)
#   id(b)
#   id(c)
#
# Finally:
#   append 30 to c
#   print a
#   print b
#   print c
#
# Explain to yourself why a changes but b does not.

# Write your code below:

print("a == b:", a == b)
print("a is b:", a is b)
print("a == c:", a == c)
print("a is c:", a is c)

print("id(a):", id(a))
print("id(b):", id(b))
print("id(c):", id(c))

c.append(30)
print("a:", a)
print("b:", b)
print("c:", c)



# ============================================================
# Task 9 — Function: is_even
# ============================================================
# Write a function:
#
#   is_even(number)
#
# It should return:
#   True  if number is even
#   False otherwise
#
# Then call it with:
#   4
#   7
#   0
#
# Print the returned results.
#
# IMPORTANT:
# The function must return the Boolean result.
# Do not print from inside the function.

# Write your code below:

def is_even(number):
    return number % 2 == 0

print(is_even(4))
print(is_even(7))
print(is_even(0))



# ============================================================
# Task 10 — Function: calculate_discount
# ============================================================
# Write a function:
#
#   calculate_discount(price, percent)
#
# It should return the final price after the discount.
#
# Formula:
# final_price = price - price * percent / 100
#
# Test it with:
#   calculate_discount(1000, 15)
#   calculate_discount(250, 20)
#
# Print each returned result.

# Write your code below:


def calculate_discount(price, percent):
    return price - price * percent / 100

print(calculate_discount(1000, 15))
print(calculate_discount(250, 20))


# ============================================================
# Task 11 — return versus print
# ============================================================
# The function below is not useful if later code needs
# to reuse the calculated value:
#
# def rectangle_area(width, height):
#     print(width * height)
#
# Rewrite it so that it RETURNS the area.
#
# Then:
#   store the result for width=5, height=4
#   print the result
#   calculate result * 2 and print it
#
# Goal:
# Demonstrate why return is different from print.

# Write your code below:


def rectangle_area(width, height):
    return width * height

area = rectangle_area(5, 4)

print(area)
print(area * 2)



# ============================================================
# Task 12 — Function returning multiple values
# ============================================================
# Write a function:
#
#   min_max(numbers)
#
# It receives a list of numbers.
#
# Use loops and conditions to find:
#   the minimum value
#   the maximum value
#
# Return both values.
#
# Do NOT use:
#   min()
#   max()
#
# Test with:
# values = [7, 2, 9, -1, 5, 12, 3]
#
# Unpack the result into:
#   smallest
#   largest
#
# Then print them.

# Write your code below:

def min_max(numbers):
    smallest = numbers[0]
    largest = numbers[0]

    for num in numbers:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    return smallest, largest


values = [7, 2, 9, -1, 5, 12, 3]
smallest, largest = min_max(values)

print(f"Smallest: {smallest}")
print(f"Largest: {largest}")


# ============================================================
# Task 13 — Integrated task: validated average
# ============================================================
# Write a function:
#
#   average(total, count)
#
# Rules:
#   if count == 0:
#       return None
#   otherwise:
#       return total / count
#
# Then write a loop that asks the user for count until
# the user enters a value >= 0.
#
# Ask once for total.
#
# Call average(total, count).
#
# If the returned result is None:
#   print "Cannot calculate average"
#
# Otherwise:
#   print the average with 2 decimal places.
#
# Required:
# Use:
#   function
#   while loop
#   condition
#   return
#   is None

# Write your code below:

def average(total, count):
    if count == 0:
        return None
    return total / count


while True:
    count = int(input("Enter count: "))
    if count >= 0:
        break

total = float(input("Enter total: "))

result = average(total, count)

if result is None:
    print("Cannot calculate average")
else:
    print(f"Average: {result:.2f}")



# ============================================================
# BONUS Task 14 — Guess the number
# ============================================================
# Use:
# secret_number = 37
#
# Repeatedly ask the user to guess the number.
#
# Print:
#   Too low
#   Too high
#   Correct
#
# Stop only when the guess is correct.
#
# Also count how many attempts were needed.
#
# Required:
# Use a while loop.

# Write your code below:

secret_number = 37
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Correct")
        break

print(f"Attempts needed: {attempts}")



# ============================================================
# BONUS Task 15 — Function-based number statistics
# ============================================================
# Write a function:
#
#   number_statistics(numbers)
#
# It should use a loop to count:
#   positive numbers
#   negative numbers
#   zeros
#
# Return all three counts.
#
# Test with:
# data = [3, -1, 0, 8, -5, 0, 2, -9]
#
# Print:
#   Positive: ...
#   Negative: ...
#   Zero: ...
#
# Do not use list comprehensions.

# Write your code below:


def number_statistics(numbers):
    positive = 0
    negative = 0
    zeros = 0

    for num in numbers:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
        else:
            zeros += 1

    return positive, negative, zeros


data = [3, -1, 0, 8, -5, 0, 2, -9]
pos, neg, zero = number_statistics(data)

print(f"Positive: {pos}")
print(f"Negative: {neg}")
print(f"Zero: {zero}")


# ============================================================
# Task 16 — Sum of even numbers with while
# ============================================================
# Ask the user for a positive integer n.
#
# Use a while loop to calculate the sum of all even numbers
# from 1 through n.
#
# Example:
# Input: 10
# Even sum: 30
#
# Because:
# 2 + 4 + 6 + 8 + 10 = 30
#
# Required:
# Use a while loop.
#
# Write your code below:
n = int(input("Enter a positive integer: "))

even_sum = 0
current = 1

while current <= n:
    if current % 2 == 0:
        even_sum += current
    current += 1

print(f"Even sum: {even_sum}")


# ============================================================
# Task 17 — Find the first divisible number
# ============================================================
numbers = [11, 17, 25, 28, 35, 41]

# Find the first number that is divisible by 7.
#
# If found:
#   print "Found: <number>"
#   stop the loop.
#
# If no number is divisible by 7:
#   print "Not found"
#
# Required:
# Use:
#   for
#   break
#   else
#
# Write your code below:

for num in numbers:
    if num % 7 == 0:
        print(f"Found: {num}")
        break
else:
    print("Not found")



# ============================================================
# Task 18 — Simple menu with while True
# ============================================================
# Create this menu:
#
# 1 - Say hello
# 2 - Show a number
# 3 - Exit
#
# Repeatedly ask the user to choose an option.
#
# If the user enters 1:
#   print "Hello!"
#
# If the user enters 2:
#   ask for a number and print it.
#
# If the user enters 3:
#   print "Goodbye!"
#   stop the program.
#
# For any other value:
#   print "Invalid option"
#
# Required:
# Use:
#   while True
#   if / elif / else
#   break
#
# Write your code below:

while True:
    print("\n1 - Say hello")
    print("2 - Show a number")
    print("3 - Exit")
    
    choice = input("Choose an option: ")

    if choice == "1":
        print("Hello!")
    elif choice == "2":
        val = input("Enter a number: ")
        print(val)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option")



# ============================================================
# Task 19 — Count positive values
# ============================================================
numbers = [5, -2, 0, 8, -4, 11, 0, -1, 7]

# Use a loop to count how many values are:
#
#   positive
#   negative
#   zero
#
# Print:
#
# Positive: ...
# Negative: ...
# Zero: ...
#
# Do not use list comprehensions.
#
# Write your code below:


positive = 0
negative = 0
zero = 0

for num in numbers:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

print(f"Positive: {positive}")
print(f"Negative: {negative}")
print(f"Zero: {zero}")


# ============================================================
# Task 20 — Number of digits
# ============================================================
# Ask the user for a positive integer.
#
# Use a while loop to count how many digits the number has.
#
# Example:
# Input: 58372
# Digits: 5
#
# Hint:
# Integer division by 10 removes the last digit.
#
# Example:
# 58372 // 10 -> 5837
#
# Do not convert the number to a string.
#
# Write your code below:

number = int(input("Enter a positive integer: "))

digits = 0

while number > 0:
    digits += 1
    number //= 10

print(f"Digits: {digits}")



# ============================================================
# Task 21 — Function: absolute_value
# ============================================================
# Write a function:
#
#   absolute_value(number)
#
# It should return the absolute value of the number.
#
# Examples:
#
# absolute_value(5)   -> 5
# absolute_value(-8)  -> 8
# absolute_value(0)   -> 0
#
# Do NOT use:
#   abs()
#
# Test the function with:
#   10
#   -7
#   0
#
# Print the returned values.
#
# Write your code below:

def absolute_value(number):
    if number < 0:
        return -number
    return number


print(absolute_value(10))
print(absolute_value(-7))
print(absolute_value(0))


# ============================================================
# Task 22 — Function: largest_of_three
# ============================================================
# Write a function:
#
#   largest_of_three(a, b, c)
#
# It should return the largest of the three numbers.
#
# Do NOT use:
#   max()
#
# Test with:
#
# largest_of_three(4, 9, 2)
# largest_of_three(10, 3, 10)
# largest_of_three(-1, -5, -3)
#
# Print the returned results.
#
# Write your code below:

def largest_of_three(a, b, c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest

print(largest_of_three(4, 9, 2))
print(largest_of_three(10, 3, 10))
print(largest_of_three(-1, -5, -3))



# ============================================================
# Task 23 — Find a value and its position
# ============================================================
numbers = [12, 7, 19, 4, 7, 25]

# Ask the user for a number to search for.
#
# Find the FIRST occurrence of that number.
#
# If found, print:
#
# Found at position: ...
#
# Positions should start from 1.
#
# Example:
# Searching for 19:
# Found at position: 3
#
# If the number does not exist:
# print:
# Not found
#
# Do not use:
#   index()
#   in
#
# Use a loop and break.
#
# Write your code below:
target = int(input("Enter a number to search for: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        print(f"Found at position: {i + 1}")
        found = True
        break

if not found:
    print("Not found")


# ============================================================
# Task 24 — Password attempts
# ============================================================
# Use:
#
# correct_password = "python123"
#
# Give the user at most 3 attempts to enter the correct
# password.
#
# If the password is correct:
#   print "Access granted"
#   stop immediately.
#
# After 3 incorrect attempts:
#   print "Access denied"
#
# Required:
# Use:
#   while
#   break
#
# Write your code below:

correct_password = "python123"
attempts = 0
access_granted = False

while attempts < 3:
    password = input("Enter password: ")
    attempts += 1

    if password == correct_password:
        print("Access granted")
        access_granted = True
        break

if not access_granted:
    print("Access denied")



# ============================================================
# Task 25 — Function: count_even
# ============================================================
# Write a function:
#
#   count_even(numbers)
#
# It receives a list of integers.
#
# Count how many values are even and return the count.
#
# Test with:
#
# values = [4, 7, 10, 13, 16, 19, 20]
#
# Expected result:
# 4
#
# The function must return the result.
#
# Write your code below:

def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count


values = [4, 7, 10, 13, 16, 19, 20]
result = count_even(values)
print(result)



# ============================================================
# Task 26 — Reverse counting pattern
# ============================================================
# Ask the user for a positive integer n.
#
# Print this pattern using nested loops.
#
# Example for n = 5:
#
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
#
# Required:
# Use nested loops.
#
# Hint:
# Think about:
#   outer loop -> controls the row
#   inner loop -> prints values inside the row
#
# Write your code below:

n = int(input("Enter a positive integer: "))

for row in range(1, n + 1):
    for col in range(row, 0, -1):
        print(col, end=" ")
    print()



# ============================================================
# Task 27 — Function: classify_number
# ============================================================
# Write a function:
#
#   classify_number(number)
#
# It should return one of these strings:
#
#   "Positive even"
#   "Positive odd"
#   "Negative even"
#   "Negative odd"
#   "Zero"
#
# Examples:
#
# classify_number(8)   -> "Positive even"
# classify_number(-3)  -> "Negative odd"
# classify_number(0)   -> "Zero"
#
# Test the function with several numbers.
#
# Write your code below:

def classify_number(number):
    if number == 0:
        return "Zero"
    elif number > 0:
        if number % 2 == 0:
            return "Positive even"
        else:
            return "Positive odd"
    else:
        if number % 2 == 0:
            return "Negative even"
        else:
            return "Negative odd"

print(classify_number(8))
print(classify_number(7))
print(classify_number(-4))
print(classify_number(-3))
print(classify_number(0))



# ============================================================
# Task 28 — Running total until limit
# ============================================================
# Repeatedly ask the user to enter positive numbers.
#
# Add each number to a running total.
#
# Stop when the total becomes greater than or equal to 100.
#
# Print:
#
# Total: ...
# Numbers entered: ...
#
# Example:
#
# 20
# 35
# 10
# 40
#
# Total: 105
# Numbers entered: 4
#
# Required:
# Use a while loop.
#
# Write your code below:
total = 0
count = 0

while total < 100:
    number = int(input("Enter a positive number: "))
    total += number
    count += 1

print(f"Total: {total}")
print(f"Numbers entered: {count}")


# ============================================================
# BONUS Task 29 — Prime number checker
# ============================================================
# Write a function:
#
#   is_prime(number)
#
# A prime number:
#   is greater than 1
#   has no divisors except 1 and itself
#
# Examples:
#
# is_prime(2)  -> True
# is_prime(7)  -> True
# is_prime(8)  -> False
# is_prime(1)  -> False
#
# Use a loop to test possible divisors.
#
# Required:
# Use:
#   function
#   for loop
#   break
#   return
#
# Do not use any external libraries.
#
# Write your code below:

def is_prime(number):
    if number <= 1:
        return False

    prime = True
    for divisor in range(2, number):
        if number % divisor == 0:
            prime = False
            break

    return prime

print(is_prime(2))
print(is_prime(7))
print(is_prime(8))
print(is_prime(1))



# ============================================================
# BONUS Task 30 — Mini calculator
# ============================================================
# Write a function:
#
#   calculate(a, b, operation)
#
# operation can be:
#
#   "+"
#   "-"
#   "*"
#   "/"
#
# Return the result of the operation.
#
# If the user tries to divide by zero:
#   return None
#
# Then create a program that repeatedly:
#
#   asks for two numbers
#   asks for an operation
#   calls calculate()
#   prints the result
#
# After each calculation ask:
#
# Continue? yes/no
#
# Stop when the user enters:
#   no
#
# Required:
# Use:
#   function
#   return
#   while loop
#   conditions
#
# Write your code below:

def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return None
        return a / b
    else:
        return None


while True:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    result = calculate(a, b, operation)

    if result is None:
        print("Error: Invalid operation or division by zero")
    else:
        print(f"Result: {result}")

    choice = input("Continue? yes/no: ")
    if choice.lower() == "no":
        break
