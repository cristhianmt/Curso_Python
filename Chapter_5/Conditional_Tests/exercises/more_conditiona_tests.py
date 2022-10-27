"""
5-2. More Conditional Tests: You don’t have to limit the number of tests you create
to 10. If you want to try more comparisons, write more tests and add them
to conditional_tests.py. Have at least one True and one False result for each of
the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less
han, greater than or equal to, and less than or equal to

"""
a = 'skyline'
b = 'skyline'

if a == b:
    print('Both cars are equals')
else:
    print('Both cars are different')

car = 'skyline'
print(car.lower() == 'skyline')

print("\nNumbers")
number = 176
print(number > 12)
print(number < 12)
print(number >= 112)
print(number <= 12)
