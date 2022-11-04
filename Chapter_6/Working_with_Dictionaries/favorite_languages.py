"""
A Dictionary of Similar Objects
The previous example involved storing different kinds of information about
one object, an alien in a game. You can also use a dictionary to store one
kind of information about many objects. For example, say you want to poll a
number of people and ask them what their favorite programming language
is. A dictionary is useful for storing the results of a simple poll, like this:
"""

favorite_language = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'rust',
    'phil': 'python',
}

language = favorite_language['sarah']
print(f"Sarah's favorite language is {language}")
