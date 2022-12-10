"""
9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
Add a method to the Battery class called upgrade_battery(). This method
should check the battery size and set the capacity to 65 if it isn’t already. Make
an electric car with a default battery size, call get_range() once, and then
call get_range() a second time after upgrading the battery. You should see an
increase in the car’s range.
"""

class Car:
    "A simple attempt to represent a car."

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        "Return a neatly formatted descriptive name."
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=84):
        """Initialize the battery's attributes. """
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def ge_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 60:
            range = 150
        elif self.battery_size == 84:
            range = 225
        
        print(f"This car can go about {range} miles on a full charge.")
    
    def upgrade_battery(self):
        if self.battery_size == 65:
            self.battery_size = 84
        else:
            print("The battery is already upgrade.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attribute of the parent class.
            Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


print("\nMake an electric car, and check the battery:")
my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()

print("\nUpgrade the battery, and check it again:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

print("\nTry upgrading the battery a second time.")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()