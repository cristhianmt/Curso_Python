"""
If you know the position of the item you want to remove from a list, you can
use the del statement:
"""

print("del statement")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)



print("\n")
"""
Removing an Item Using the pop() Method
The pop() method removes the last item in a list
"""
print("pop method")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorycle = motorcycles.pop()
print(motorcycles)
print(popped_motorycle)



print("\n")
"""
How might this pop() method be useful? Imagine that the motorcycles
in the list are stored in chronological order, according to when we owned
them.
"""
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")


print("\n")
"""
You can use pop() to remove an item form any position in a list by including 
the index of the item you want to remove in parentheses
"""
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned as a {first_owned.title()}.")


"""
If you’re unsure whether to use the del statement or the pop() method,
here’s a simple way to decide: when you want to delete an item from a list
and not use that item in any way, use the del statement; if you want to use an
item as you remove it, use the pop() method.
"""