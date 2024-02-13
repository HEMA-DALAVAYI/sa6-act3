'''
Problem 2: Custom Sort Order
Objective: Given a list of strings, use a lambda function to sort 
the list in ascending order based on the length of the strings. 
In case of a tie, sort the strings alphabetically.
Hint: The sorted() function's key parameter can take a lambda function 
that returns a tuple indicating the primary and secondary sort keys.

'''
list = ['happy' , 'birthday', 'to', 'me']

# len(x) indicates that the items in list should first be sorted by their lengths
# with x it indicates that the items in list should be sorted alphabetically as second priority 
# if there comes a tie

ordered_list = sorted( list, key = lambda x : (len(x) , x))
print(ordered_list)