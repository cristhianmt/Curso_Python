"""
Looping through all key-value pairs works particularly well for dictionaries
like the favorite_languages.py example on page 96, which stores the
same kind of information for many different keys. If you loop through the
favorite_languages dictionary, you get the name of each person in the dictionary
and their favorite programming language. Because the keys always
refer to a person’s name and the value is always a language, we’ll use the
variables name and language in the loop instead of key and value. This will
make it easier to follow what’s happening inside the loop:
"""
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
for name, language in favorite_languages.items():
    print(f"\n {name.title()}'s favorite language is {language.title()}.")
