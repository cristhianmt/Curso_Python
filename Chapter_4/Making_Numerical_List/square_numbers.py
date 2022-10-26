"""
You can create almost any set of numbers you want to using the range()
function. For example, consider how you might make a list of the first 10
square numbers (that is, the square of each integer from 1 through 10). In
Python, two asterisks (**) represent exponents. Here’s how you might put
the first 10 square numbers into a list:
"""

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)


print("\n")
"""
Simple statics with a List off numbers
"""

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
