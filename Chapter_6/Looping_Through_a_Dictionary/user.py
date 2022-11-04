"""
Looping Through a Dictionary
A single Python dictionary can contain just a few key-value pairs or millions
of pairs. Because a dictionary can contain large amounts of data, Python
lets you loop through a dictionary. Dictionaries can be used to store information
in a variety of ways; therefore, several different ways exist to loop
through them. You can loop through all of a dictionary’s key-value pairs,
through its keys, or through its values.

Looping Through All Key-Value Pairs
Before we explore the different approaches to looping, let’s consider a new
dictionary designed to store information about a user on a website. The
following dictionary would store one person’s username, first name, and
last name:
"""

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
