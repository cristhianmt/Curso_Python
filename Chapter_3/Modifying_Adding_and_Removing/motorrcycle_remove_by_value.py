"""
Somethings you won't know the position of the value you want to remove
from a list. If you only know the value of the item you want to remove, 
you can use the remove() method. 
"""

print("remove")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove("honda")
print(motorcycles)


print("\n")
"""We can also use the remove() method to work with a value that's being
removed form a list
"""
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")