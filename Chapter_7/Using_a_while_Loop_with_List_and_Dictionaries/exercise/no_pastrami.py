"""
7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches.
"""

sandwich_orders = ['veggie', 'grilled cheese', 'pastrami',
                   'turkey', 'pastrami', 'roast beef', 'pastrami']
finished_sandwich = []
print("The deli has run out of pastrami")

while sandwich_orders and 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    current_sandwich = sandwich_orders.pop()
    print(f"\nI'm working on your {current_sandwich} sandwich.")
    finished_sandwich.append(current_sandwich)

for sandwich in finished_sandwich:
    print(f"\nI made your {sandwich} sandwich.")
