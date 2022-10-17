
"""
Extra whitespace can be confusing in your programs. To programmers,
'python' and 'python ' look pretty much the same. But to a program, they
are two different strings. Python detects the extra space in 'python ' and
considers it significant unless you tell it otherwise.
It’s important to think about whitespace, because often you’ll want to
compare two strings to determine whether they are the same. For example,
one important instance might involve checking people’s usernames when
they log in to a website. Extra whitespace can be confusing in much simpler
situations as well. Fortunately, Python makes it easy to eliminate extra
whitespace from data that people enter.
Python can look for extra whitespace on the right and left sides of a
string. To ensure that no whitespace exists at the right side of a string, use
the rstrip() method:
"""

favorite_language = 'python '
print(favorite_language)

print(favorite_language.rstrip())


print("\n")

"""
You can also strip whitespace from the left side of a string using the
lstrip() method, or from both sides at once using strip():
"""
favorite_language = ' python '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

