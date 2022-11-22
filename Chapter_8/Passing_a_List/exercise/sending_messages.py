"""
8-10. Sending Messages: Start with a copy of your program from 
Exercise 8-9. Write a function called send_messages() that prints each 
text message and moves each message to a new list called sent_messages 
as it’s printed. After calling the function, print both of your lists to 
make sure the messages were moved correctly.
"""


def show_messages(unprinted_message, sent_messages):
    while unprinted_message: 
        current_text = unprinted_message.pop()
        print(f"Printing texts: {current_text}")
        sent_messages.append(current_text)

def send_message(sent_messages):
    print("\nThe following text have been printed")
    for sent_message in sent_messages:
        print(sent_message)

unprinted_message = ['I love python', 'I love linux', 'I love debian']
sent_messages = []

show_messages(unprinted_message, sent_messages)
send_message(sent_messages)
print(f"\nCheck the list is empty: {unprinted_message}")
print(f"Check the list is full: {sent_messages}")
