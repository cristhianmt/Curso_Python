"""
8-11. Archived Messages: Start with your work from Exercise 8-10. 
Call the function send_messages() with a copy of the list of messages. 
After calling the function, print both of your lists to show that the 
original list has retained its messages.
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

show_messages(unprinted_message[:], sent_messages)
send_message(sent_messages)
print(f"\nCheck the list is full and copy to sent_messages: {unprinted_message}")
print(f"Check the list is full: {sent_messages}")