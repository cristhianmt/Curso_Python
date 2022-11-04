"""
6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
• Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output.
"""

glossary = {
    'dictionaries': 'is a collection of key-value pairs.',
    'if': 'is an expression that can be evaluated as True or False',
    'list': 'is a collection of items in a particular order.',
    'string': 'is a series of characters',
    '#': 'indicates a comment.',

}

word = glossary['dictionaries']
print(f"\n Dictionaries: {word}")


word = glossary['if']
print(f"\n If: {word}")

word = glossary['list']
print(f"\n List: {word}")

word = glossary['string']
print(f"\n String: {word}")

word = glossary['#']
print(f"\n #: {word}")
