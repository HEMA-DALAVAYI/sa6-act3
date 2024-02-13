'''
Objective: Write a Python program that uses a lambda function to compute the sum
of the digits of a given number.
Hint: You may need to convert the number to a string to iterate over its digits, 
then back to integers to sum them.

'''

from functools import reduce

number = str(56)

digits_add =reduce(lambda x, y: int(x) + int(y), number)
print(digits_add)
