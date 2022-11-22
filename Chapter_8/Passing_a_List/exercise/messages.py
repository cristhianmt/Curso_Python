"""
8-9. Messages: Make a list containing a series of short text 
messages. Pass the list to a function called show_messages(), 
which prints each text message.
"""


def show_messages(texts):
    for text in texts:
        msg = f"{text}"
        print(msg)


message = ['I love python', 'I love linux', 'I love debian']
show_messages(message)
