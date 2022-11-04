"""
Checking for Special Items
This chapter began with a simple example that showed how to handle a special
value like 'bmw', which needed to be printed in a different format than
other values in the list. Now that you have a basic understanding of conditional
tests and if statements, let’s take a closer look at how you can watch
for special values in a list and handle those values appropriately.
Let’s continue with the pizzeria example. The pizzeria displays a message
whenever a topping is added to your pizza, as it’s being made. The code
for this action can be written very efficiently by making a list of toppings the
customer has requested and using a loop to announce each topping as it’s
added to the pizza:
"""

request_toppings = ['mushrooms', 'green peppers', 'extra chess']

for request_topping in request_toppings:
    if request_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {request_topping}")

print("\nFinished making your pizza!")
