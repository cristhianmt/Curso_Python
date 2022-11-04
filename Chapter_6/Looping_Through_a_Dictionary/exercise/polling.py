"""
6-6. Polling: Use the code in favorite_languages.py (page 96).
• Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
• Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll.
"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("\n")

friends = ['phil', 'sarah', 'daniels']

for name in friends:
    if name in favorite_languages.keys():
        print(f"Thank you {name.title()} to responded the poll  ")
    else:
        print(f"{name.title()}, What's your favorite language programming?")