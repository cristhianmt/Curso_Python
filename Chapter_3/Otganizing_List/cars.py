"""
Python’s sort() method makes it relatively easy to sort a list. Imagine we
have a list of cars and want to change the order of the list to store them
alphabetically.
"""
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)



"""
You can also sort this list in reverse-alphabetical order by passing the
argument reverse=True to the sort() method.
"""
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
