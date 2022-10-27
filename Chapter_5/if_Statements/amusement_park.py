"""
The if-elif-else Chain
Often, you’ll need to test more than two possible situations, and to evaluate
these you can use Python’s if-elif-else syntax. Python executes only one
block in an if-elif-else chain. It runs each conditional test in order, until
one passes. When a test passes, the code following that test is executed and
Python skips the rest of the tests.
Many real-world situations involve more than two possible conditions.
For example, consider an amusement park that charges different rates for
different age groups:
• Admission for anyone under age 4 is free.
• Admission for anyone between the ages of 4 and 18 is $25.
• Admission for anyone age 18 or older is $40.
How can we use an if statement to determine a person’s admission rate?
The following code tests for the age group of a person and then prints an
admission price message:
"""

age = 12
if age < 4:
    print("Your admission cost is $0.")
    price = 0
elif age < 18:
    print("Your admission cost is $25.")
    price = 25
else:
    print("Your admission cost is $40.")
    price = 40

print(f"Your admission cost is ${price}.")


print("\nUsing Multiple elif Blocks")
age = 64
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")

print("\nOmitting the else Block")
age = 65
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}.")
