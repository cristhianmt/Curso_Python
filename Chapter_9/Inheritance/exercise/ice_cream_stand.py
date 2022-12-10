"""
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote in
Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version of the class
will work; just pick the one you like better. Add an attribute called flavors that
stores a list of ice cream flavors. Write a method that displays these flavors.
Create an instance of IceCreamStand, and call this method.
"""


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self): 
        print(f"Welcome to {self.restaurant_name}.")
        print(f"Cuisine type is {self.cuisine_type}.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []   
    def display(self):
        for flavor in self.flavors:
            print(f" - {flavor.title()}")

el_rincon =  IceCreamStand('El rincon enchilado', 'Ice cream')
el_rincon.flavors = ['strawberry', 'vanilla']
el_rincon.describe_restaurant()
el_rincon.display()
