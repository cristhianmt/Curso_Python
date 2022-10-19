"""
2-4 Names cases: Use a variable to represent a person's name, and then print
that person's name in lowercase, uppercase, and title case. 
"""

from cProfile import label


first_name = "bl3ak"
last_name = "storm"
full_name = f" {first_name} {last_name}"
print(full_name.lower())
print(full_name.upper())
print(full_name.title())
