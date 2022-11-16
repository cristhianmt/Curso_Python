"""
In this example, when we enter 21 at the prompt, Python interprets the number as 
a string, but the value is then converted to a numerical representation by int() 1. 
Now Python can run the conditional test: it compares age (which now represents the
 numerical value 21) and 18 to see if age is greater than or equal to 18. This test evaluates to True.
How do you use the int() function in an actual program? Consider a program that 
determines whether people are tall enough to ride a roller coaster:
"""
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou'are tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
