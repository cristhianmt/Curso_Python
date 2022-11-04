"""
Modifying Values in a Dictionary
To modify a value in a dictionary, give the name of the dictionary with the
key in square brackets and then the new value you want associated with
that key. For example, consider an alien that changes from green to yellow
as a game progresses:
"""

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color']='yellow'
print(f"The alien is now {alien_0['color']}.")