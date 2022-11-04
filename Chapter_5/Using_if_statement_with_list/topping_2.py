"""
Checking That a List Is Not Empty
We’ve made a simple assumption about every list we’ve worked with so far:
we’ve assumed that each list has at least one item in it. Soon we’ll let users
provide the information that’s stored in a list, so we won’t be able to assume
that a list has any items in it each time a loop is run. In this situation, it’s
useful to check whether a list is empty before running a for loop.
As an example, let’s check whether the list of requested toppings is
empty before building the pizza. If the list is empty, we’ll prompt the user
and make sure they want a plain pizza. If the list is not empty, we’ll build
the pizza just as we did in the previous examples:
"""

request_toppings = []

if request_toppings:
    for request_topping in request_toppings:
        print(f"Adding {request_topping}")
    else:
        print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")