"""
9-3. Users: Make a class called User. Create 
two attributes called first_name and last_name, 
and then create several other attributes that are 
typically stored in a user profile. Make a method 
called describe_user() that prints a summary of the user’s 
information. Make another method called greet_user() that
 prints a personalized greeting to the user.
Create several instances representing different 
users, and call both methods for each user.
"""

class User:

    def __init__(self,first_name, last_name, email):
        self.fn = first_name
        self.ln = last_name
        self.e = email

    def describe_user(self):
        print(f"The name user is {self.fn.title()} {self.ln.title()} and the email is {self.e}")

    def greet_user(self):
        print(f"Hi {self.fn}, nice to see you!")

andrea = User('andrea', 'gomez', 'agomez@gmail.com')
andrea.describe_user()
andrea.greet_user()

print("\n")
miguel = User('miguel', 'tenoch', 'mtecnoch@gmail.com' )
miguel.describe_user()
miguel.greet_user()