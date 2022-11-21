"""
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping, print
a message saying you’ll add that topping to their pizza.
"""

prompt = "\nPlease enter the name of your topping that you want to add to your pizza: "
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"I'd like to add {topping.title()} to my pizza")