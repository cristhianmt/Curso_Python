"""
Slicing a List
To make a slice, you specify the index of the first and last elements you want
to work with. As with the range() function, Python stops one item before the
second index you specify. To output the first three elements in a list, you
would request indices 0 through 3, which would return elements 0, 1, and 2.
The following example involves a list of players on a team:
"""
players = ['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[0:4])
print(players[0:4])
print(players[0:4])
print(players[-3:])