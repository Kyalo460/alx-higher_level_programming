#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    a = number % -10
else:
    a = number % 10
if number > 5:
    print(f"Last digit of {number} is {a} and is greater that 5")
elif number == 0:
    print(f"Last digit of {number} is {a} and is 0")
elif number < 6:
    print(f"Last digit of {number} is {a} and is less than 6 and not 0")
