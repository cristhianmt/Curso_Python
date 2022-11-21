"""
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.
"""


def make_shirt(text, size='large'):
    print(f"The size of the shirt is {size}.")
    print(f"The text should be printed is '{text.title()}'.")


make_shirt(text='i love python')
make_shirt(text='i love linux', size='small')

