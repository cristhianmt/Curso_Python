"""
Numerical Comparisons
You can also test to see if two numbers are not equal. For example, the
following code prints a message if the given answer is not correct:
"""
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")


# Using and to Check Multiple Conditions


print("\nUsing and to Check Multiple Conditions")
age = 19
print(age < 21)

print("\n")
print(age <= 21)

print("\n")
print(age > 21)

print("\n")
print(age >= 21)

print("\nUsing or to check multiple conditions")
age_0 = 22
age_1 = 18

print(age_0 >= 21 or age_1 >= 21)

age_0 = 18
print(age_0 >= 21 or age_1 >= 21)


print("\nUsing or to check multiple conditions")
request_toppings = ['mushrooms','onions','pineapple']
print('mushrooms' in request_toppings)
print('pepperoni' in request_toppings)

