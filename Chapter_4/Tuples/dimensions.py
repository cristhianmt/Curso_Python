"""
Defining a Tuple
A tuple looks just like a list, except you use parentheses instead of square
brackets. Once you define a tuple, you can access individual elements by
using each item’s index, just as you would for a list.
For example, if we have a rectangle that should always be a certain size, we
can ensure that its size doesn’t change by putting the dimensions into a tuple:
"""

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])


# let's see what happens if we try to change one of the items in the tuple dimensions
dimensions[0] = 250
"""
This code tries to change the value of the first dimension, but Python
returns a type error. Because we’re trying to alter a tuple, which can’t be
done to that type of object, Python tells us we can’t assign a new value to
an item in a tuple:
"""
