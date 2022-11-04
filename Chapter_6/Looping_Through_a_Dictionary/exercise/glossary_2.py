"""
6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 99) by replacing your series of print()
calls with a loop that runs through the dictionary’s keys and values. When
you’re sure that your loop works, add five more Python terms to your glossary.
When you run your program again, these new words and meanings should
automatically be included in the output.
"""

glossary = {
    'dictionaries': 'is a collection of key-value pairs.',
    'if': 'is an expression that can be evaluated as True or False',
    'list': 'is a collection of items in a particular order.',
    'string': 'is a series of characters',
    '#': 'indicates a comment.',
}

for name, language in glossary.items():
    print(f"\n {name.title()}: {language.title()}.")
