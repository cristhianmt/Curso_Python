"""
Equivalent Function Calls
Because positional arguments, keyword arguments, and default values can
all be used together, you’ll often have several equivalent ways to call a function.
Consider the following definition for describe_pet() with one default
value provided:
"""


def describe_pet(pet_name, animal_type='dog'):
    # Display information about a pet.
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


    # A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')
# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
