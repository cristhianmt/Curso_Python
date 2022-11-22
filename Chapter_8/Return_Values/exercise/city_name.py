"""
8-6. City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the values
that are returned.
"""


def describe_city(city, country):
    city  = f" {city.title()} is in {country.title()}."
    return city

name = describe_city('santiago', 'chile')
print(name)

name = describe_city('sidney', 'australia')
print(name)
name = describe_city('montreal', 'canada')
print(name)
