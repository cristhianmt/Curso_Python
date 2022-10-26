"""
Copying a List
Often, you’ll want to start with an existing list and make an entirely new list
based on the first one. Let’s explore how copying a list works and examine
one situation in which copying a list is useful.
To copy a list, you can make a slice that includes the entire original list
by omitting the first index and the second index ([:]). This tells Python to
make a slice that starts at the first item and ends with the last item, producing
a copy of the entire list.
For example, imagine we have a list of our favorite foods and want to
make a separate list of foods that a friend likes. This friend likes everything
in our list so far, so we can create their list by copying ours:
"""

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]


my_foods.append('cannoli')
friend_foods.append('ace cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)




# This doesn't work:
friend_foods = my_foods
