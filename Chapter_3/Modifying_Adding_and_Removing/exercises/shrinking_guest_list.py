"""
3-7. Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print a
message to that person letting them know you’re sorry you can’t invite them
to dinner.
• Print a message to each of the two people still on your list, letting them
know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end of
your program.
"""


guest_list = ['bob', 'alice', 'tom', 'kelly']

print("I found out that i can invite only two people for dinner.\n")


remove_people_1 = guest_list.pop(0)
print(f"Sorry {remove_people_1} i can't invite you to dinner\n")

remove_people_2 = guest_list.pop(0)
print(f"Sorry {remove_people_2} i can't invite you to dinner\n")

print(f"Please {guest_list[0]} come to dinner.")
print(f"Please {guest_list[1]} come to dinner.")

del guest_list[:]
print(f"I have an empty list ")
print(f"{guest_list}")
