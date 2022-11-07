"""
6-7. People: Start with the program you wrote for Exercise 6-1 (page 98). Make
two new dictionaries representing different people, and store all three dictionaries
in a list called people. Loop through your list of people. As you loop through
the list, print everything you know about each person.
"""
people_1 = {
    'first_name': 'david',
    'last_name': 'bombal',
    'city': 'uk',
}
people_2 = {
    'first_name': 'john',
    'last_name': 'hammond',
    'city': 'usa',
}
people_3 = {
    'first_name': 'marcelo',
    'last_name': 'savitar',
    'city': 'uk',
}

peoples = [people_1, people_2,people_3]

for person in peoples:
    full_name = f"{person['first_name'].title()} {person['last_name'].title()}"
    city = person['city'].title()

    print(f"\tFull name: {full_name.title()}")
    print(f"\tCity: {city.title()}\n")
