"""
Using get() to Access Values
Using keys in square brackets to retrieve the value you’re interested in from a
dictionary might cause one potential problem: if the key you ask for doesn’t
exist, you’ll get an error.
"""

# Get an error
# alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])
# KeyError: 'points'


alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned')
print(point_value)