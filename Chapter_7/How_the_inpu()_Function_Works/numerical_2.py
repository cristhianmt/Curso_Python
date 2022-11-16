"""
The user enters the number 21, but when we ask Python for the value of
age, it returns '21', the string representation of the numerical value entered.
We know Python interpreted the input as a string because the number is
now enclosed in quotes. If all you want to do is print the input, this works
well. But if you try to use the input as a number, you’ll get an error:

>>> age = input("How old are you? ")
How old are you? 21
1 >>> age >= 18
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
2 TypeError: '>=' not supported between instances of 'str' and 'int'
"""

age = input("How old are you? ")
print(age)
age = int(age)
print(age >= 18)
