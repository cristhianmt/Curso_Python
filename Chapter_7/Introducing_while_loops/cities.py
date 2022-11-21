"""
Using break to Exit a Loop
To exit a while loop immediately without running any remaining code in
the loop, regardless of the results of any conditional test, use the break statement.
The break statement directs the flow of your program; you can use it
to control which lines of code are executed and which aren’t, so the program
only executes code that you want it to, when you want it to.
For example, consider a program that asks the user about places they’ve
visited. We can stop the while loop in this program by calling break as soon
as the user enters the 'quit' value:
"""

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}")