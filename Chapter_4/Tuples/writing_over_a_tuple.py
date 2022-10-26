"""
Although you can’t modify a tuple, you can assign a new value to a variable
that represents a tuple. For example, if we wanted to change the dimensions
of this rectangle, we could redefine the entire tuple:
"""
dimensions = (200,50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)