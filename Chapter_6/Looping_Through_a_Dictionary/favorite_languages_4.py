"""
Looping Through a Dictionary’s Keys in a Particular Order
Looping through a dictionary returns the items in the same order they
were inserted. Sometimes, though, you’ll want to loop through a dictionary
in a different order.
One way to do this is to sort the keys as they’re returned in the for loop.
You can use the sorted() function to get a copy of the keys in order:
"""
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
