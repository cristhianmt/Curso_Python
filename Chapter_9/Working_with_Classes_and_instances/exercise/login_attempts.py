"""
9-5. Login Attempts: Add an attribute called login_attempts to your User class
from Exercise 9-3 (page 162). 

Write a method called increment_login_attempts()
that increments the value of login_attempts by 1. 
Write another method called
reset_login_attempts() that resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.
"""


class User:

    def __init__(self, first_name, last_name, email):
        self.fn = first_name
        self.ln = last_name
        self.e = email
        self.login_attempts = 0

    def describe_user(self):
        print(
            f"The name user is {self.fn.title()} {self.ln.title()} and the email is {self.e}")

    def greet_user(self):
        print(f"Hi {self.fn}, nice to see you!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


andrea = User('andrea', 'gomez', 'agomez@gmail.com')
andrea.describe_user()
andrea.greet_user()

print("\n")
miguel = User('miguel', 'tenoch', 'mtecnoch@gmail.com')
miguel.describe_user()
miguel.greet_user()

print("\nIncrement login ")
andrea.increment_login_attempts()
andrea.increment_login_attempts()
andrea.increment_login_attempts()
andrea.increment_login_attempts()
print(f"Login attempts: {str(andrea.login_attempts)}")

print("\nResetting login ")
andrea.reset_login_attempts()
print(f"Login attempts: {str(andrea.login_attempts)}")

