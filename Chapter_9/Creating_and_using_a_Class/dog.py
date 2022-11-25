"""
Creating and Using a Class
You can model almost anything using classes. Let’s start by writing a simple
class, Dog, that represents a dog—not one dog in particular, but any dog. What
do we know about most pet dogs? Well, they all have a name and an age. We
also know that most dogs sit and roll over. Those two pieces of information
(name and age) and those two behaviors (sit and roll over) will go in our Dog
class because they’re common to most dogs. This class will tell Python how
to make an object representing a dog. After our class is written, we’ll use it to
make individual instances, each of which represents one specific dog.
Creating the Dog Class
Each instance created from the Dog class will store a name and an age, and
we’ll give each dog the ability to sit() and roll_over():
"""


class Dog:
    # A simple attempt to model a dog.
    """
    The __init__() method 2 is a special method
    that Python runs automatically whenever we create a new instance based
    on the Dog class.
    """

    def __init__(self, name, age):
        # Initialize name and age attribute.
        self.name = name
        self.age = age

    def sit(self):
        # Simulate a dog sitting in response to a command.
        print(f"{self.name} is now sitting. ")

    def roll_over(self):
        # Simulate rolling over in response to a command.
        print(f"{self.name} rolled over.")


print("\nMaking an Instance from a Class")
my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

print("\nCalling Methods")
my_dog.sit()
my_dog.roll_over()