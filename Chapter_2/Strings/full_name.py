"""
To insert a variable’s value into a string, place the letter f immediately
before the opening quotation mark 1. Put braces around the name or
names of any variable you want to use inside the string. Python will replace
each variable with its value when the string is displayed.
These strings are called f-strings. The f is for format, because Python
formats the string by replacing the name of any variable in braces with its
value. The output from the previous code is:
"""

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}" 
print(full_name)
print(f"Hello, {full_name.title()}!")