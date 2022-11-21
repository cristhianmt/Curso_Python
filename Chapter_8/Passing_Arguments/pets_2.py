"""
Keyword Arguments
A keyword argument is a name-value pair that you pass to a function. You
directly associate the name and the value within the argument, so when you
pass the argument to the function, there’s no confusion (you won’t end up
with a harry named Hamster). Keyword arguments free you from having
to worry about correctly ordering your arguments in the function call, and
they clarify the role of each value in the function call.
Let’s rewrite pets.py using keyword arguments to call describe_pet():
"""


def describe_pet(animal_type, pet_name):
    # Display information about a pet.
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(animal_type='dog', pet_name='willie')
