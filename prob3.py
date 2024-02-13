'''
Problem 3: Find Maximum
Objective: Implement a function that takes a list of numbers and 
a lambda function as arguments. The lambda function should compare two 
numbers and return the greater of the two. Use this lambda function to find
the maximum number in the list without using the built-in max() function.
Hint: Initialize your maximum with the first element of the list and then 
iterate over the list, using the lambda function to update the maximum.

'''

numbers = [1, 45, 65, 78, 100]
compare = (lambda x, y: x > y)

def find_max(numbers, compare):
    max = numbers[0]
    for x in numbers:
        if compare(x, max):
            max = x
    return max

print(find_max(numbers,compare))