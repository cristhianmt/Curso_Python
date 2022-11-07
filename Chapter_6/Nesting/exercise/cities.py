"""
6-11. Cities: Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the information
you have stored about it.
"""

cities = {
    'washington': {
        'country': 'usa',
        'population': 712.816,
        'fact': 'Center of Entertainment.',
    },
    'montreal': {
        'country': 'canada',
        'population': 1.79,
        'fact': 'Cirque de Soleil',
    },
    'sidney': {
        'country': 'australia',
        'population': 5.312,
        'fact': 'The Magic Of Vivid Sydney',
    },
}

for city, information in cities.items():
    print(f"The information about {city.title()}")
    country = information['country']
    population = information['population']
    fact = information['fact']

    print(f"\n{city.title()} is in {country.title()}")
    print(f"\tIt has a population of about: {population}.")
    print(f"\tThe important fact are {fact}. ")
