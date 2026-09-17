"""
NSU Python — Lab 03
Conditions and for Loops

Complete Tasks 1–12.
Tasks 13–14 are optional bonus tasks.

Use only concepts covered in Lecture 03.
"""


# ============================================================
# Task 1 — Positive, negative, or zero
# ============================================================
# Ask the user to enter an integer.
# Print exactly one of:
#   Positive
#   Negative
#   Zero
#
# Example:
# Input: -7
# Output: Negative

# Write your code below:

number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# ============================================================
# Task 2 — Age category
# ============================================================
# Ask the user for their age.
#
# Print:
#   Child      -> age < 13
#   Teenager   -> 13–17
#   Adult      -> 18–64
#   Senior     -> 65 or older
#
# Test boundary values: 12, 13, 17, 18, 64, 65.

# Write your code below:

age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age <= 17:
    print("Teenager")
elif age <= 64:
    print("Adult")
else:
    print("Senior")



# ============================================================
# Task 3 — Grade classifier
# ============================================================
# Ask the user for a score.
#
# First check whether the score is between 0 and 100 inclusive.
#
# For a valid score:
#   A    -> 90–100
#   B    -> 75–89
#   C    -> 60–74
#   Fail -> below 60
#
# For an invalid score print:
#   Invalid score

# Write your code below:

score = int(input("Enter your score: "))

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("A")
elif score >= 75:
    print("B")
elif score >= 60:
    print("C")
else:
    print("Fail")


# ============================================================
# Task 4 — Access decision
# ============================================================
# Ask the user for:
#   age
#   whether they have a ticket: yes/no
#
# A person may enter only if:
#   age >= 18 AND they have a ticket.
#
# Print one of:
#   Access granted
#   Ticket required
#   Must be 18 or older

# Write your code below:

age = int(input("Enter your age: "))
has_ticket = input("Do you have a ticket? (yes/no): ")

if age >= 18 and has_ticket == "yes":
    print("Access granted")
elif has_ticket == "no":
    print("Ticket required")
else:
    print("Must be 18 or older")


# ============================================================
# Task 5 — Even numbers with range()
# ============================================================
# Print all even numbers from 2 through 30.
#
# Required:
# Use range(start, stop, step).

# Write your code below:

for number in range(2, 31, 2):
    print(number)



# ============================================================
# Task 6 — Sum of multiples of 3
# ============================================================
# Calculate and print the sum of all multiples of 3
# from 3 through 99.
#
# Required:
# Use a for loop and an accumulator.
#
# Expected result:
# 1683

# Write your code below:

total = 0
for number in range(3, 100, 3):
    total += number

print(total)


# ============================================================
# Task 7 — Count number categories
# ============================================================
numbers = [4, -2, 0, 7, -5, 9, 0, -1, 8]

# Count how many values are:
#   positive
#   negative
#   zero
#
# Print all three counts.
# Do not manually count the values.
# Write your code below:

positive_count = 0
negative_count = 0
zero_count = 0

for number in numbers:
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    else:
        zero_count += 1

print("Positive:", positive_count)
print("Negative:", negative_count)
print("Zero:", zero_count)


# ============================================================
# Task 8 — Count vowels
# ============================================================
# Ask the user to enter a word or short text.
# Count how many vowels it contains.
#
# Treat uppercase and lowercase equally.
# Vowels: a e i o u
#
# Example:
# Input: Artificial Intelligence
# Output: 10
#
# Hint:
# Iterate directly over the string.

# Write your code below:

text = input("Enter a word or text: ")
vowel_count = 0

for char in text.lower():
    if char in "aeiou":
        vowel_count += 1

print(vowel_count)



# ============================================================
# Task 9 — Student results
# ============================================================
scores = [85, 42, 67, 91, 58, 73, 100, 39]

# Count:
#   passed students: score >= 60
#   failed students: score < 60
#
# Also print the average score.
#
# Required:
# Use a loop to calculate the total.
#
# Expected:
# Passed: 5
# Failed: 3
# Average: 69.38

# Write your code below:

passed = 0
failed = 0
total = 0

for score in scores:
    total += score
    if score >= 60:
        passed += 1
    else:
        failed += 1

average = total / len(scores)

print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Average: {average:.2f}")




# ============================================================
# Task 10 — Search and stop
# ============================================================
names = ["Anna", "Boris", "Sasha", "Maria", "Oleg", "Dina"]

# Ask the user for a name.
# Search the list using a for loop.
#
# If found:
#   print "Found"
#   stop immediately with break
#
# If not found:
#   print "Not found"
#
# Do not use:
#   if target in names
#
# Hint:
# A Boolean variable such as found = False can help.

# Write your code below:

target = input("Enter a name to search for: ")
found = False

for name in names:
    if name == target:
        found = True
        break

if found:
    print("Found")
else:
    print("Not found")



# ============================================================
# Task 11 — Skip invalid scores
# ============================================================
raw_scores = [78, -5, 91, 120, 66, 0, 88, 101, 54]

# Valid scores are from 0 to 100 inclusive.
#
# Use continue to skip invalid scores.
# For valid scores:
#   print each valid score
#   calculate the average of valid scores
#
# At the end print:
#   Valid scores: ...
#   Average: ...
#
# Required:
# Use continue.

# Write your code below:

total = 0
valid_count = 0

for score in raw_scores:
    if score < 0 or score > 100:
        continue

    print(score)
    total += score
    valid_count += 1

average = total / valid_count

print(f"Valid scores: {valid_count}")
print(f"Average: {average:.2f}")



# ============================================================
# Task 12 — Dictionary iteration
# ============================================================
student_scores = {
    "Anna": 92,
    "Boris": 58,
    "Sasha": 76,
    "Maria": 49,
    "Oleg": 84,
}

# Iterate using .items().
#
# Print:
#   Anna: Pass
#   Boris: Fail
#   ...
#
# Score >= 60 means Pass.
# Then print how many students passed.

# Write your code below:

passed_count = 0

for student, score in student_scores.items():
    if score >= 60:
        print(f"{student} Passed")
        passed_count += 1
    else:
        print(f"{student} Failed")

print(f"Students Passed : {passed_count}")


# ============================================================
# BONUS Task 13 — FizzBuzz
# ============================================================
# Print numbers 1 through 30.
#
# If divisible by both 3 and 5 -> FizzBuzz
# If divisible only by 3       -> Fizz
# If divisible only by 5       -> Buzz
# Otherwise print the number.
#
# Hint:
# Check the most specific condition first.

# Write your code below:

for number in range(1, 31):
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)



# ============================================================
# BONUS Task 14 — Limited login attempts
# ============================================================
correct_pin = "4821"

# Give the user at most 3 attempts to enter the PIN.
#
# Use:
#   for
#   range()
#   break
#
# Correct PIN:
#   Access granted
#
# Three wrong attempts:
#   Access denied
#
# Do NOT use a while loop.

# Write your code below:

success = False

for attempt in range(3):
    pin = input("Enter your PIN: ")
    if pin == correct_pin:
        print("Access granted")
        success = True
        break

if not success:
    print("Access denied")



# ============================================================
# EXTRA Task 15 — Largest of three numbers
# ============================================================
# Ask the user to enter three integers.
#
# Print the largest number.
#
# Do NOT use:
#   max()
#
# Example:
# Input:
# 12
# 7
# 19
#
# Output:
# Largest: 19
#
# Think carefully about equal values.

# Write your code below:

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print(f"Largest: {largest}")



# ============================================================
# EXTRA Task 16 — Number statistics
# ============================================================
numbers = [12, -4, 7, 0, 15, -9, 8, -2, 0, 21]

# Using one for loop, calculate:
#   number of positive values
#   number of negative values
#   number of zeros
#   sum of positive values
#   sum of negative values
#
# Expected:
# Positive: 5
# Negative: 3
# Zero: 2
# Positive sum: 63
# Negative sum: -15
#
# Do not manually calculate the values.

# Write your code below:

pos_count = 0
neg_count = 0
zero_count = 0
pos_sum = 0
neg_sum = 0

for num in numbers:
    if num > 0:
        pos_count += 1
        pos_sum += num
    elif num < 0:
        neg_count += 1
        neg_sum += num
    else:
        zero_count += 1

print(f"Positive: {pos_count}")
print(f"Negative: {neg_count}")
print(f"Zero: {zero_count}")
print(f"Positive sum: {pos_sum}")
print(f"Negative sum: {neg_sum}")



# ============================================================
# EXTRA Task 17 — Highest and lowest score
# ============================================================
scores = [71, 85, 42, 96, 58, 83, 67, 91]

# Find the highest and lowest scores using a for loop.
#
# Do NOT use:
#   max()
#   min()
#   sorted()
#
# Hint:
# Start with:
# highest = scores[0]
# lowest = scores[0]
#
# Expected:
# Highest: 96
# Lowest: 42

# Write your code below:


highest = scores[0]
lowest = scores[0]

for score in scores:
    if score > highest:
        highest = score
    if score < lowest:
        lowest = score

print(f"Highest: {highest}")
print(f"Lowest: {lowest}")



# ============================================================
# EXTRA Task 18 — Temperature analysis
# ============================================================
temperatures = [12, 18, 25, 31, 7, 22, 35, 16, 29, 4]

# Classify every temperature:
#
#   Cold -> below 10
#   Mild -> 10–19
#   Warm -> 20–29
#   Hot  -> 30 or above
#
# Example output:
# 12: Mild
# 18: Mild
# 25: Warm
# ...
#
# After processing all temperatures, print how many
# temperatures belong to each category.

# Write your code below:

cold = 0
mild = 0
warm = 0
hot = 0

for temp in temperatures:
    if temp < 10:
        category = "Cold"
        cold += 1
    elif temp <= 19:
        category = "Mild"
        mild += 1
    elif temp <= 29:
        category = "Warm"
        warm += 1
    else:
        category = "Hot"
        hot += 1

    print(f"{temp}: {category}")

print("\nSummary:")
print(f"Cold: {cold}")
print(f"Mild: {mild}")
print(f"Warm: {warm}")
print(f"Hot: {hot}")



# ============================================================
# EXTRA Task 19 — Running balance
# ============================================================
transactions = [500, -120, -80, 250, -700, 300, -200]

# The starting balance is:
balance = 1000

# Process every transaction in order.
#
# Positive numbers mean money added.
# Negative numbers mean money spent.
#
# After each transaction print the current balance.
#
# Example:
# Transaction: 500
# Balance: 1500
#
# At the end print:
# Final balance: ...
#
# Also count how many transactions were:
#   deposits
#   withdrawals

# Write your code below:

deposits = 0
withdrawals = 0

for t in transactions:
    balance += t

    if t > 0:
        deposits += 1
    elif t < 0:
        withdrawals += 1

    print(f"Transaction: {t}")
    print(f"Balance: {balance}")

print(f"\nFinal balance: {balance}")
print(f"Deposits: {deposits}")
print(f"Withdrawals: {withdrawals}")



# # ============================================================
# # EXTRA Task 20 — Find first number divisible by 7 and 11
# # ============================================================
# # Search numbers from 1 through 500.
# #
# # Find the FIRST number that is divisible by both 7 and 11.
# #
# # Print the number and immediately stop the loop.
# #
# # Required:
# #   for
# #   range()
# #   break
# #
# # Expected:
# # 77

# # Write your code below:

for number in range(1, 501):
    if number % 7 == 0 and number % 11 == 0:
        print(number)
        break



# ============================================================
# EXTRA Task 21 — Limited number guessing
# ============================================================
secret_number = 37

# Give the user at most 5 attempts to guess the secret number.
#
# After each incorrect guess:
#
#   if guess < secret_number:
#       print "Too low"
#
#   if guess > secret_number:
#       print "Too high"
#
# Correct guess:
#   print "Correct"
#   stop immediately
#
# If all 5 attempts are used without success:
#   print "Out of attempts"
#
# Required:
#   for
#   range()
#   if / elif / else
#   break
#
# Do NOT use while.

# Write your code below:

guessed_correctly = False

for attempt in range(5):
    guess = int(input("Enter your guess: "))
    
    if guess == secret_number:
        print("Correct")
        guessed_correctly = True
        break
    elif guess < secret_number:
        print("Too low")
    else:
        print("Too high")

if not guessed_correctly:
    print("Out of attempts")



# ============================================================
# EXTRA Task 22 — Count increases
# ============================================================
values = [10, 14, 13, 18, 22, 20, 25, 25, 30]

# Count how many times a value is greater than
# the value immediately before it.
#
# Comparisons:
# 10 -> 14   increase
# 14 -> 13   no
# 13 -> 18   increase
# ...
#
# Expected:
# Increases: 5
#
# Hint:
# Start looping from index 1:
#
# for i in range(1, len(values)):
#
# Compare:
# values[i]
# values[i - 1]

# Write your code below:


increases = 0

for i in range(1, len(values)):
    if values[i] > values[i - 1]:
        increases += 1

print(f"Increases: {increases}")


# ============================================================
# EXTRA Task 23 — Prime number check
# ============================================================
# Ask the user to enter an integer greater than 1.
#
# Determine whether the number is prime.
#
# A prime number is divisible only by 1 and itself.
#
# Examples:
# 7  -> Prime
# 12 -> Not prime
# 29 -> Prime
#
# Required:
# Use a for loop to test divisors.
#
# Do NOT use any library.
#
# Hint:
# Try dividing by numbers from 2 up to number - 1.
# If one divides exactly, the number is not prime.

# Write your code below:

number = int(input("Enter an integer greater than 1: "))
is_prime = True

for divisor in range(2, number):
    if number % divisor == 0:
        is_prime = False
        break

if is_prime:
    print("Prime")
else:
    print("Not prime")



# ============================================================
# EXTRA Task 24 — Multiplication table
# ============================================================
# Print a multiplication table from 1 to 5.
#
# Expected format:
#
# 1 2 3 4 5
# 2 4 6 8 10
# 3 6 9 12 15
# 4 8 12 16 20
# 5 10 15 20 25
#
# Required:
# Use nested for loops.
#
# Hint:
#
# for row in range(...):
#     for column in range(...):
#         ...

# Write your code below:

for row in range(1, 6):
    for column in range(1, 6):
        print(row * column, end=" ")
    print()
