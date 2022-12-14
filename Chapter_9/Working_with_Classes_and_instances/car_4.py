"""
We can extend the method update_odometer() to do additional work every
time the odometer reading is modified. Let’s add a little logic to make sure
no one tries to roll back the odometer reading:
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
        """Set the odometer reading to the given value.\
            Reject the change if it attemps to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
       

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

print("\nModifying an attribute's value through a method")
my_new_car.update_odometer(24)
my_new_car.read_odometer()