"""
Modifying an Attribute’s Value Through a Method
It can be helpful to have methods that update certain attributes for you. Instead of accessing the attribute directly, you pass the new value to a method that handles the updating internally.
"""


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        log_name = f"{self.year} {self.make} {self.model}"
        return log_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage
       

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

print("\nModifying an attribute's value through a method")
my_new_car.update_odometer(24)
my_new_car.read_odometer()