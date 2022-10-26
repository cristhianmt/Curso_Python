"""
Using range() to Make a List of Numbers
If you want to make a list of numbers, you can convert the results of range()
directly into a list using the list() function. When you wrap list() around a
call to the range() function, the output will be a list of numbers.
In the example in the previous section, we simply printed out a series of
numbers. We can use list() to convert that same set of numbers into a list:
"""

numbers = list(range(1, 6))
print(numbers)

even_number = list(range(2, 11, 2))
print(even_number)
