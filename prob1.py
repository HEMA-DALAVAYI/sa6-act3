'''
Objective: Write a Python program that uses a lambda function to compute the sum
of the digits of a given number.
Hint: You may need to convert the number to a string to iterate over its digits, 
then back to integers to sum them.

'''

from functools import reduce

number = str(56)
list = []
for i in range(len(number)):
    list.append(int(number[i]))
    
digits_add =reduce(lambda x, y: x + y, list)
print(digits_add)
