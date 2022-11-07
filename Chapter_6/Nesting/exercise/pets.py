"""
6-8. Pets: Make several dictionaries, where each dictionary represents a different
pet. In each dictionary, include the kind of animal and the owner’s name.
Store these dictionaries in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet.
"""

pets = []

pet = {
    'kind_pet': 'dog',
    'name_pet': 'neon',
    'owner_name': 'david'
}
pets.append(pet)

pet = {
    'kind_pet': 'cat',
    'name_pet': 'salsa',
    'owner_name': 'john'
}
pets.append(pet)


pet = {
    'kind_pet': 'fish',
    'name_pet': 'blue',
    'owner_name': 'bob'
}
pets.append(pet)

for pet in pets:
    print(f"Here is what i know about {pet['name_pet']}")
    for key, value in pet.items():
        print(f"\t {key}: {value}")
