"""
3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
"""

guest_list = ['bob', 'alice', 'tom', 'kelly']

print("I found a bigger table to invite guest.")
guest_list.insert(0,'carl')
guest_list.insert(2,'david')
guest_list.insert(-1,'frank')

print(
    f"Hi {guest_list}, i would like to invite to a dinner tomorrow.")
