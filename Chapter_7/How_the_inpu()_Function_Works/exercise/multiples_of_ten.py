"""
7-3. Multiples of Ten: Ask the user for a number, and then report whether the
number is a multiple of 10 or not.
"""
number = input("Give me a number: ")
number = int(number)

if number % 10 == 0:
    print(f"{number} Is multiple of 10")
else:
    print(f"{number} Is not multiple of 10")
