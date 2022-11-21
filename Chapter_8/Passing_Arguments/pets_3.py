"""
Default Values
When writing a function, you can define a default value for each parameter. If an argument for a parameter is provided in the function call, Python uses the argument value. If not, it uses the parameter’s default value. So when you define a default value for a parameter, you can exclude the corresponding argument you’d usually write in the function call. Using default values can simplify your function calls and clarify the ways your functions are typically used.
For example, if you notice that most of the calls to describe_pet() are being used to describe dogs, you can set the default value of animal_type to 'dog'. Now anyone calling describe_pet() for a dog can omit that information:
"""


def describe_pet(pet_name, animal_type='dog'):
    # Display information about a pet.
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('willie')
