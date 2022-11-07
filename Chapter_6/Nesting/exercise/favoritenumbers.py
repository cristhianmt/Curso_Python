"""
6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 98) so
each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers.
"""

favorite_numbers = {
    'david': [24, 4, 75, ],
    'anna': [53, 5, 23, 36, ],
    'paul': [44, 23, 456, 23, ],
    'carl': [55, 567, 12, 45, ],
    'andy': [35, 13, 5612, 745, 34, ],
}

for name, numbers in favorite_numbers.items():
    print(f"Here are the favorites numbers about {name.title()}: ")
    for number in numbers:
        print(f"\t{str(number)}")
