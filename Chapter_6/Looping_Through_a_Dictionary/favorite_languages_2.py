"""
Looping Through All the Keys in a Dictionary
The keys() method is useful when you don’t need to work with all of the values
in a dictionary. Let’s loop through the favorite_languages dictionary and
print the names of everyone who took the poll:
"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name in favorite_languages.keys():
    print(name.title())

print("\n")
# or
for name in favorite_languages:
    print(name.title())

