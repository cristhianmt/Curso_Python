"""
Using as to Give a Function an Alias
If the name of a function you’re importing might conflict with an existing
name in your program, or if the function name is long, you can use a
short, unique alias—an alternate name similar to a nickname for the function.
You’ll give the function this special nickname when you import the
function.
Here we give the function make_pizza() an alias, mp(), by importing make
_pizza as mp. The as keyword renames a function using the alias you provide:
"""

from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers',
                 'green peppers', 'extra cheese')