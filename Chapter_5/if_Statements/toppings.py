"""
Testing Multiple Conditions
The if-elif-else chain is powerful, but it’s only appropriate to use when you
just need one test to pass. As soon as Python finds one test that passes, it
skips the rest of the tests. This behavior is beneficial, because it’s efficient
and allows you to test for one specific condition.
However, sometimes it’s important to check all conditions of interest. In
this case, you should use a series of simple if statements with no elif or else
blocks. This technique makes sense when more than one condition could
be True, and you want to act on every condition that is True.
Let’s reconsider the pizzeria example. If someone requests a two-topping
pizza, you’ll need to be sure to include both toppings on their pizza:
"""
request_toppings = ['mushrooms','extra cheese']
if 'mushrooms' in request_toppings:
    print("Adding mushrooms")
if 'pepperoni' in request_toppings:
    print("Adding pepperoni")
if 'extra cheese' in request_toppings:
    print("Adding extra cheese")

print("\nFinished making your pizza!")


"""
This code would not work properly if we used an if-elif-else block,
because the code would stop running after only one test passes. Here’s
what that would look like:
"""
print("\n")
request_toppings = ['mushrooms','extra cheese']
if 'mushrooms' in request_toppings:
    print("Adding mushrooms")
elif 'pepperoni' in request_toppings:
    print("Adding pepperoni")
elif 'extra cheese' in request_toppings:
    print("Adding extra cheese")

print("\nFinished making your pizza!")