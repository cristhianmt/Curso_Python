"""
9-2. Three Restaurants: Start with your class from Exercise 9-1. 
Create three different instances from the class, 
and call describe_restaurant() for each instance.
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

rincon =  Restaurant('El rincon enchilado', 'mexican breakfast')
rincon.describe_restaurant()
rincon.open_restaurant()

print("\n")
alcatraz = Restaurant('El alactraz', 'italian food')
alcatraz.describe_restaurant()
alcatraz.open_restaurant()

print("\n")
sazon = Restaurant('Nuestro sazon','australia food')
sazon.describe_restaurant()
sazon.open_restaurant()