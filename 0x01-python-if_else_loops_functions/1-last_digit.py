#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = -1 * number
    last_digit = -1 * (number % 10)
else:
    last_digit = number % 10
print(f"Last digit of {number} is {last_digit} and is", end=" ")
if last_digit > 5:
    print("greater than 5")
elif last_digit == 0:
    print("0")
elif last_digit < 6 and last_digit != 0:
    print("less than 6 and not 0")
