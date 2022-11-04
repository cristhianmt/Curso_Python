"""
6-5. Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
• Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
• Use a loop to print the name of each river included in the dictionary.
• Use a loop to print the name of each country included in the dictionary.
"""

rivers = {
    'nile': 'egypt',
    'mississippi': 'missouri',
    'yellow': 'huang he'
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

print("\nRiver name")
for river in rivers.keys():
    print(f"{river.title()}")

print("\nCountry name")
for country in rivers.values():
    print(f"{country.title()}")
