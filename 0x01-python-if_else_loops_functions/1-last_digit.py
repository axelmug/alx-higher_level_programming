#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    print(f"Last digit of {number} is {number%10} and is greater than 5 \n")
elif number == 0:
    print(f"Last digit of {number} is {number%10} and is 0 \n")
elif number :
    print(f"Last digit of {number} is {number%10} and is less than 6 and not 0\n")
