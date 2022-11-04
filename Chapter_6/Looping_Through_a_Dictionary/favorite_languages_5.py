"""
Looping Through All Values in a Dictionary
If you are primarily interested in the values that a dictionary contains, you
can use the values() method to return a sequence of values without any
keys. For example, say we simply want a list of all languages chosen in our
programming language poll, without the name of the person who chose
each language:
"""
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())


print("\n SET")
"""
This approach pulls all the values from the dictionary without checking
for repeats. This might work fine with a small number of values, but in a
poll with a large number of respondents, it would result in a very repetitive
list. To see each language chosen without repetition, we can use a set. A set
is a collection in which each item must be unique:
"""
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())